from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from Vortice.models import *
from coupons.forms import CouponApplyForm
from .cart import Cart
from .forms import CartAddProductForm


# Agregar producto al carrito
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Prod_prenda, id=product_id)

    # Bind del formulario con la información de tallas
    form = CartAddProductForm(request.POST, has_sizes=product.has_sizes,is_unique=product.is_unique )# ← lo añadimos aquí

    if form.is_valid():
        # Si es producto único y ya está en el carrito, no añadir de nuevo
        if product.is_unique and any(item['product'].id == product.id for item in cart):
            messages.warning(request, "Este producto exclusivo ya está en tu carrito.")
            return redirect('cart:cart_detail')




        cd = form.cleaned_data
        size = cd['size'] if product.has_sizes else 'U'  # Si no tiene tallas, usa "Única"

        print(f"Añadiendo producto {product_id}, Cantidad: {cd['quantity']}, Override: {cd['override']}, Talla: {size}")

        cart.add(product=product,
                 size=size,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    else:
        print("Formulario no válido")
        messages.error(request, "No se pudo añadir el producto (formulario inválido).")


    return redirect('cart:cart_detail')


# Eliminar producto del carrito
@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Prod_prenda, id=product_id)
    size = request.POST.get('size', 'U')  # Obtén la talla del formulario, usa "U" si no hay

    cart.remove(product, size=size)

    return redirect('cart:cart_detail')


# Ver detalle del carrito
def cart_detail(request):
    cart = Cart(request)

    # Calcular subtotal antes del envío
    subtotal = cart.get_total_price_after_discount()

    # Aplicar costo de envío si el subtotal es menor a $100
    shipping_cost = 0 if subtotal > 100 else 5

    # Total con envío
    total_with_shipping = subtotal + shipping_cost

    for item in cart:
        product = get_object_or_404(Prod_prenda, id=item['product'].id)  # Obtener el producto

        item['update_quantity_form'] = CartAddProductForm(
            initial={
                'quantity': item['quantity'],
                'override': True,
                'size': item.get('size', 'U')  # Usar "U" si no hay talla

            },
            has_sizes=product.has_sizes,  # Pasar si el producto tiene tallas
            is_unique=product.is_unique  # Añade este parámetro
        )
        print(f"Formulario para el ítem: {item['update_quantity_form'].initial}")

    coupon_apply_form = CouponApplyForm()

    contexto = {
        'vortice': Vortice.objects.all().first(),
        'secciones': Seccion_Cliente.objects.all(),
        'colecciones': Coleccion.objects.all(),
        #'imag_prenda_articulos': Imag_prenda_articulo.objects.all(),
        'tipo_articulos_menu': Tipo_articulo.objects.all(),
        'notificaciones': Notificaciones.objects.all().first(),
        'cart': cart,
        'coupon_apply_form': coupon_apply_form,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'total_with_shipping': total_with_shipping,

    }
    return render(request, 'cart/detail.html',contexto )

