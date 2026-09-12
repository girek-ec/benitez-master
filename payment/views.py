import urllib
from decimal import Decimal
from email import message

import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404

from Vortice.models import *
from orders.models import Order
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect

from urllib.parse import quote_plus
import urllib.parse
import requests




# Crear la instancia de Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


import requests

def verify_recaptcha(recaptcha_response):
    secret_key = settings.RECAPTCHA_SECRET_KEY  # Guarda tu clave secreta en settings.py
    url = "https://www.google.com/recaptcha/api/siteverify"
    data = {"secret": secret_key, "response": recaptcha_response}
    response = requests.post(url, data=data)
    result = response.json()
    return result.get("success", False)


def payment_process(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)

    # Validar si hay productos en la orden
    if order.items.count() == 0:
        return render(request, 'payment/process.html', {
            'order': order,
            'error_message': "No hay productos en el carrito. Agrega productos para continuar con la compra.",
            'disable_payment': True,  # Nueva variable de contexto
            'vortice': Vortice.objects.all().first(),
            'secciones': Seccion_Cliente.objects.all(),
            'colecciones': Coleccion.objects.all(),
            'tipo_articulos_menu': Tipo_articulo.objects.all(),
            'notificaciones': Notificaciones.objects.all().first(),
        })

    # Resto del código de la vista permanece igual...
    # Cálculos de la orden


    # Cálculos de la orden
    subtotal = order.get_total_cost_before_discount()  # Subtotal antes del descuento
    discount_amount = order.get_discount()  # Monto del descuento aplicado a los productos
    subtotal_after_discount = subtotal - discount_amount  # Subtotal después del descuento en productos

    # Aplicar la lógica correcta para calcular el costo de envío basado en el subtotal con descuento
    shipping_cost = Decimal(0) if subtotal_after_discount > Decimal('100.00') else Decimal('5.00')

    # Calcular el total final después de aplicar descuento y costo de envío
    total_final = subtotal_after_discount + shipping_cost

    # Generar mensaje de WhatsApp
    whatsapp_message = generate_whatsapp_message(order)

    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')

        if not verify_recaptcha(recaptcha_response):
            return render(request, 'payment/process.html', {
                'order': order,
                'error_message': "Por favor, verifica que no eres un robot."
            })

        success_url = request.build_absolute_uri(reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(reverse('payment:canceled'))

        session_data = {
            'mode': 'payment',
            'client_reference_id': order.id,
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []
        }

        # Agregar productos a la sesión de Stripe con tallas
        for item in order.items.all():
            product_name = f"{item.product.nombre_produc} (Talla: {item.size})"
            session_data['line_items'].append({
                'price_data': {
                    'unit_amount': int(item.get_cost() * Decimal('100')),  # Convertir a centavos
                    'currency': 'usd',
                    'product_data': {'name': product_name},
                },
                'quantity': item.quantity,
            })

        # Agregar costo de envío si es mayor a 0
        if shipping_cost > 0:
            session_data['line_items'].append({
                'price_data': {
                    'unit_amount': int(shipping_cost * Decimal('100')),  # Convertir a centavos
                    'currency': 'usd',
                    'product_data': {'name': 'Costo de envío'},
                },
                'quantity': 1,
            })

        # Aplicar descuento si existe
        if order.coupon:
            stripe_coupon = stripe.Coupon.create(
                name=order.coupon.code,
                amount_off=int(discount_amount * Decimal('100')),  # Convertir a centavos
                currency='usd',
                duration='once'
            )
            session_data['discounts'] = [{'coupon': stripe_coupon.id}]

        # Crear sesión de pago en Stripe
        session = stripe.checkout.Session.create(**session_data)

        # Redirigir al formulario de pago de Stripe
        return redirect(session.url, code=303)

    # Renderizar la plantilla con el contexto adecuado
    context = {
        'order': order,
        'subtotal': subtotal,
        'discount_amount': discount_amount,
        'subtotal_after_discount': subtotal_after_discount,
        'shipping_cost': shipping_cost,
        'total_final': total_final,
        'vortice': Vortice.objects.all().first(),
        'secciones': Seccion_Cliente.objects.all(),
        'colecciones': Coleccion.objects.all(),
        #'imag_prenda_articulos': Imag_prenda_articulo.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'notificaciones': Notificaciones.objects.all().first(),
        'whatsapp_message': whatsapp_message,

    }
    return render(request, 'payment/process.html', context)

def payment_completed(request):
    # Limpiar el cupón de la sesión después de completar la compra
    request.session.pop('coupon_id', None)

    # Renderizar la plantilla con el contexto adecuado
    context = {
        'vortice': Vortice.objects.all().first(),
        'secciones': Seccion_Cliente.objects.all(),
        'colecciones': Coleccion.objects.all(),
        #'imag_prenda_articulos': Imag_prenda_articulo.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'notificaciones': Notificaciones.objects.all().first(),

    }
    return render(request, 'payment/completed.html', context)

def payment_canceled(request):
    # Limpiar el cupón de la sesión si el pago es cancelado
    request.session.pop('coupon_id', None)

    # Renderizar la plantilla con el contexto adecuado
    context = {
        'vortice': Vortice.objects.all().first(),
        'secciones': Seccion_Cliente.objects.all(),
        'colecciones': Coleccion.objects.all(),
        #'imag_prenda_articulos': Imag_prenda_articulo.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'notificaciones': Notificaciones.objects.all().first(),
    }
    return render(request, 'payment/canceled.html', context)


def send_whatsapp_and_email(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)

    if order.items.count() == 0 or order.get_total_cost() <= 0:
        return redirect('cart:cart_detail')

    recaptcha_response = request.GET.get('g-recaptcha-response')

    if not recaptcha_response or not verify_recaptcha(recaptcha_response):
        return redirect('payment:process')

    whatsapp_message = generate_whatsapp_message(order)
# Correo desactivado temporalmente porque Gmail SMTP no responde desde el VPS
    try:
        send_order_email(order, order.email)
    except Exception as e:
        print("ERROR EMAIL:", e)

    whatsapp_url = f"https://wa.me/593993239290?text={whatsapp_message}"
    return redirect(whatsapp_url)

def send_order_email(order, customer_email):
    # Generar el mensaje de WhatsApp
    whatsapp_message = generate_whatsapp_message(order)

    # Asunto del correo
    email_subject = f"Nuevo Pedido - Vórtice Ecuador - #{order.id}"

    # Encabezado del correo
    email_message = f"""
    ✨ * Pedido_# {order.id} - Vórtice Ecuador* ✨
    --------------------------------------
    ¡Hola! 👋 Se ha realizado un nuevo pedido en Vórtice Ecuador.

    🛒 *Datos del Cliente:*
    👤 Nombre: {order.first_name} {order.last_name}
    📧 Correo: {order.email}
    📍 Dirección: {order.address}, {order.city}
    📦 Código Postal: {order.postal_code}
    📝 Detalle de domicilio: {order.detail}
    --------------------------------------

    📦 *Detalles del pedido:*
    """

    # Detalles de los productos
    for item in order.items.all():
        email_message += f"\n🔹 *Producto:* {item.product.nombre_produc}"
        email_message += f"\n   🔸 Talla: {item.size}"
        email_message += f"\n   🔸 Cantidad: {item.quantity}"
        email_message += f"\n   🔸 Precio unitario: ${item.product.price:.2f}"
        email_message += f"\n   🔸 Subtotal: ${item.get_cost():.2f}"
        email_message += "\n--------------------------------------"

    # Resumen del pedido
    email_message += f"""
    💰 *Resumen del pedido:*
    🛍️ Subtotal: ${order.get_total_cost_before_discount():.2f}
    """

    if order.coupon:
        email_message += f"🎟️ Descuento ({order.coupon.code}): -${order.get_discount():.2f}"

    email_message += f"""
    🚚 Costo de envío: ${order.shipping_cost:.2f}
    ✅ *Total a pagar:* ${order.get_total_cost():.2f}
    --------------------------------------

    📌 *Por favor, confírmame la disponibilidad de los productos y el proceso de pago.*
    ¡Gracias! 😊

    🛍️ *Vórtice Ecuador - Moda con estilo*

    --------------------------------------
    *Mensaje de WhatsApp generado:*
    {whatsapp_message}
    """

    # Enviar el correo
    send_mail(
        email_subject,
        email_message,
        settings.DEFAULT_FROM_EMAIL,  # Dirección de correo electrónico del remitente
        [customer_email,'vortice.ec@gmail.com'],
        fail_silently=False,  # Correo electrónico del cliente
    )



def generate_whatsapp_message(order):
    # Generar el mensaje principal con los detalles del pedido
    message = f"✨ * Pedido_# {order.id} - Vórtice Ecuador* ✨\n"
    message += "--------------------------------------\n"
    message += "📋 *Datos del Cliente:*\n"
    message += f"👤 Nombre: {order.first_name} {order.last_name}\n"
    message += f"📧 Correo: {order.email}\n"
    message += f"🏠 Dirección: {order.address}\n"
    message += f"📦 Código Postal: {order.postal_code}\n"
    message += f"📍 Detalle de domicilio: {order.detail}\n"
    message += "--------------------------------------\n"
    message += "¡Hola! 👋 Me gustaría realizar un pedido:\n\n"

    # Detalles de los productos
    message += "📦 *Detalles del pedido:*\n"
    for item in order.items.all():
        message += f"🔹 *Producto:* {item.product.nombre_produc}\n"
        message += f"   🔸 Talla: {item.size}\n"
        message += f"   🔸 Cantidad: {item.quantity}\n"
        message += f"   🔸 Precio unitario: ${item.product.price:.2f}\n"
        message += f"   🔸 Subtotal: ${item.get_cost():.2f}\n"
        message += "--------------------------------------\n"

    # Resumen del pedido
    message += "💰 *Resumen del pedido:*\n"
    message += f"🛍️ Subtotal: ${order.get_total_cost_before_discount():.2f}\n"

    if order.coupon:
        message += f"🎟️ Descuento ({order.coupon.code}): -${order.get_discount():.2f}\n"

    message += f"🚚 Costo de envío: ${order.shipping_cost:.2f}\n"
    message += f"✅ *Total a pagar:* ${order.get_total_cost():.2f}\n"
    message += "--------------------------------------\n\n"



    # Mensaje final
    message += "¡Gracias! 😊\n\n"
    message += "🛍️ *Vórtice Ecuador - Moda con estilo*"

    # Codificar el mensaje para WhatsApp
    whatsapp_encoded = urllib.parse.quote(message, encoding='utf-8')

    return whatsapp_encoded


def orden_pedido(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)

    # Cálculos de la orden
    subtotal = order.get_total_cost_before_discount()  # Subtotal antes del descuento
    discount_amount = order.get_discount()  # Monto del descuento aplicado a los productos
    subtotal_after_discount = subtotal - discount_amount  # Subtotal después del descuento en productos
    shipping_cost = Decimal(0) if subtotal_after_discount > Decimal('50.00') else Decimal('5.00')
    total_final = subtotal_after_discount + shipping_cost

    # Renderizar la plantilla con el contexto adecuado
    context = {
        'order': order,
        'subtotal': subtotal,
        'discount_amount': discount_amount,
        'subtotal_after_discount': subtotal_after_discount,
        'shipping_cost': shipping_cost,
        'total_final': total_final,
        'vortice': Vortice.objects.all().first(),
        'secciones': Seccion_Cliente.objects.all(),
        'colecciones': Coleccion.objects.all(),
        #'imag_prenda_articulos': Imag_prenda_articulo.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'notificaciones': Notificaciones.objects.all().first(),
        'bancos' :  Banco.objects.all(),
    }
    return render(request, 'payment/orden_pedido.html', context)
