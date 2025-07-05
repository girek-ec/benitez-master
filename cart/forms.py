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
        # ✅ Parámetros personalizados que vienen desde la vista
        has_sizes = kwargs.pop('has_sizes', True)
        is_unique = kwargs.pop('is_unique', False)

        super().__init__(*args, **kwargs)

        if is_unique:
            # Solo 1 unidad, ocultamos selector y forzamos override=True
            self.fields['quantity'].choices = [(1, '1')]
            self.fields['quantity'].initial = 1
            self.fields['quantity'].widget = forms.HiddenInput()

            self.fields['size'].choices = PRODUCT_SIZE_UNICA
            self.fields['size'].initial = 'U'
            self.fields['size'].widget = forms.HiddenInput()
            self.fields['size'].required = False

            # Forzamos override para que no sume cantidad, sino que reemplace (1)
            self.fields['override'].initial = True

        else:
            # Configuración normal para otros productos
            self.fields['quantity'].choices = PRODUCT_QUANTITY_CHOICES
            if has_sizes:
                self.fields['size'].choices = PRODUCT_SIZE_CHOICES
            else:
                self.fields['size'].choices = PRODUCT_SIZE_UNICA