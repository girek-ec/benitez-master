from pathlib import Path
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

from Vortice.models import *
from .models import OrderItem, Order
from .forms import OrderCreateForm
from .tasks import order_created
from cart.cart import Cart
from decimal import Decimal

def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)

            # Capturar datos del cliente
            order.first_name = form.cleaned_data['first_name']
            order.last_name = form.cleaned_data['last_name']
            order.email = form.cleaned_data['email']
            order.address = form.cleaned_data['address']
            order.postal_code = form.cleaned_data['postal_code']
            order.city = form.cleaned_data['city']
            order.detail = form.cleaned_data['detail']

            # Aplicar descuento del cupón si existe
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
                discount_amount = cart.get_discount()
            else:
                discount_amount = Decimal(0)

            # Calcular subtotal después del descuento
            subtotal = cart.get_total_price() - discount_amount

            # Calcular costo de envío
            shipping_cost = Decimal(0) if subtotal > 100 else Decimal(5)

            # Total final con descuentos y envío
            total_price = subtotal + shipping_cost
            order.total_price = total_price
            order.shipping_cost = shipping_cost

            order.save()

            for item_key, item in cart.cart.items():
                product_id, _, size = item_key.partition('_')
                product = get_object_or_404(Prod_prenda, id=product_id)

                # Si el producto no tiene talla, asignar talla única
                size = size if size else 'U'

                OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=item['price'],
                    quantity=item['quantity'],
                    size=size
                )

            # Limpiar el carrito
            cart.clear()

            # Iniciar tarea asincrónica  aqui la desactiveeee
            #order_created.delay(order.id)

            # Establecer el orden en la sesión
            request.session['order_id'] = order.id

            # Redirigir para el pago
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()

    contexto = {
        'vortice': Vortice.objects.all().first(),
        'secciones': Seccion_Cliente.objects.all(),
        'colecciones': Coleccion.objects.all(),
        #'imag_prenda_articulos': Imag_prenda_articulo.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'notificaciones': Notificaciones.objects.all().first(),
        'cart': cart,
        'form': form,

    }


    return render(request,
                  'orders/order/create.html', contexto)


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    vortice = Vortice.objects.all().first()  # Obtén el primer objeto Vortice

    contexto = {
        'vortice': vortice,  # Pasa el objeto Vortice al contexto
        'order': order,
        'discount': order.discount if order.coupon else Decimal(0),
        'shipping_cost': order.shipping_cost,
    }




    return render(request,
                  'admin/orders/order/detail.html',
                  contexto)





@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    vortice = Vortice.objects.all().first()  # Obtén el primer objeto Vortice

    contexto = {
        'vortice': vortice,  # Pasa el objeto Vortice al contexto
        'order': order,
        'discount': order.discount if order.coupon else Decimal(0),
        'shipping_cost': order.shipping_cost,
    }

    # Renderiza la plantilla HTML
    html = render_to_string('orders/order/pdf.html', contexto)

    # Configura la respuesta HTTP para devolver un PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'

    # Ruta al archivo CSS
    css_path = Path(settings.BASE_DIR) / "static" / "css" / "pdf.css"

    # Genera el PDF con WeasyPrint
    weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(
        response,
        stylesheets=[weasyprint.CSS(str(css_path))]
    )

    return response