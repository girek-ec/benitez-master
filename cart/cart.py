from decimal import Decimal
from django.conf import settings
from Vortice.models import Prod_prenda
from coupons.models import Coupon


class Cart:
    def __init__(self, request):
        """
        Inicializa el carrito.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        # store current applied coupon
        self.coupon_id = self.session.get('coupon_id')

    def __iter__(self):
        """
        Iterar sobre los artículos en el carrito y obtener los productos.
        de la base de datos.
        """
        product_ids = {item_key.split('_')[0] for item_key in self.cart.keys()}  # Solo extraemos los IDs de productos
        products = Prod_prenda.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            for item_key, item in cart.items():
                # Asegurarse de que solo actualizamos los productos relacionados con este ID
                if item_key.startswith(str(product.id)):
                    item['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Cuenta todos los artículos en el carrito.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, size=None, override_quantity=False):
        """
        Añade un producto al carrito o actualiza su cantidad.
        """
        product_id = str(product.id)
        item_key = f"{product_id}_{size}" if size else product_id # Clave única para cada talla

        if item_key not in self.cart:
            self.cart[item_key] = {'quantity': 0,
                                   'price': str(product.price),
                                   'size': size }  # Guardar la talla

        if override_quantity:
            self.cart[item_key]['quantity'] = quantity
        else:
            self.cart[item_key]['quantity'] += quantity

        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product, size=None):
        """
        Quitar un producto del carrito.
        """
        product_id = str(product.id)
        item_key = f"{product_id}_{size}" if size else product_id  # Clave única para cada talla

        if item_key in self.cart:
            del self.cart[item_key]
            self.save()

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        """
        Devuelve el precio total del carrito antes del descuento.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def get_shipping_cost(self):
        """
        Calcula el costo de envío basado en el precio total sin descuento.
        """
        total = self.get_total_price()
        return Decimal(0) if total > Decimal('100.00') else Decimal('5.00')

    def get_shipping_cost_after_discount(self):
        """
        Calcula el costo de envío basado en el subtotal después del descuento.
        """
        subtotal = self.get_total_price_after_discount()
        return Decimal(0) if subtotal > Decimal('100.00') else Decimal('5.00')

    @property
    def coupon(self):
        if self.coupon_id:
            try:
                return Coupon.objects.get(id=self.coupon_id)
            except Coupon.DoesNotExist:
                pass
        return None

    def get_discount(self):
        """
        Calcula el descuento basado en el cupón aplicado.
        """
        if self.coupon:
            return (self.coupon.discount / Decimal(100)) * self.get_total_price()
        return Decimal(0)

    def get_total_price_after_discount(self):
        """
        Calcula el precio total después de aplicar el descuento.
        """
        return self.get_total_price() - self.get_discount()

    def get_total_price_with_shipping(self):
        """
        Calcula el total del carrito incluyendo el costo de envío después del descuento.
        """
        return self.get_total_price_after_discount() + self.get_shipping_cost_after_discount()

