from django import forms

class ProductVariantForm(forms.Form):
    product_variant = forms.IntegerField()
    quantity = forms.IntegerField(min_value=1)