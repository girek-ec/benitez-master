from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupon
from .forms import CouponApplyForm


def start_new_purchase(request):
    # Eliminar el cupón de la sesión al iniciar una nueva compra
    if 'coupon_id' in request.session:
        del request.session['coupon_id']

    # Lógica adicional para iniciar una nueva compra
    # ...

    return redirect('cart:cart_detail')  # Redirigir al carrito o a la página de inicio de compra

@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        # Eliminar cualquier cupón existente en la sesión antes de aplicar uno nuevo
        if 'coupon_id' in request.session:
            del request.session['coupon_id']

        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            # Guardar el cupón en la sesión
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            # Si el cupón no existe o no es válido, no hacer nada (ya se eliminó el cupón anterior)
            pass
    return redirect('cart:cart_detail')


