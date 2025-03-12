from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 24)]

# Opciones de tallas estándar
PRODUCT_SIZE_CHOICES = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    ('XXL', 'Extra Extra Large'),
]

# Opción de talla única
PRODUCT_SIZE_UNICA = [
    ('U', 'Única'),
]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        label="Cantidad",
        coerce=int
    )
    size = forms.ChoiceField(label="Talla", required=False)  # Se definirá dinámicamente
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )

    def __init__(self, *args, **kwargs):
        has_sizes = kwargs.pop('has_sizes', True)  # Recibe si el producto tiene tallas
        super().__init__(*args, **kwargs)

        # Asignar opciones de tallas dinámicamente
        if has_sizes:
            self.fields['size'].choices = PRODUCT_SIZE_CHOICES
        else:
            self.fields['size'].choices = PRODUCT_SIZE_UNICA
