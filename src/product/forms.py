from django.forms import forms, ModelForm, CharField, TextInput, Textarea, BooleanField, CheckboxInput
from django import forms
from product.models import Variant


class VariantForm(ModelForm):
    class Meta:
        model = Variant
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'active'})
        }

class ProductFilterForm(forms.Form):
    title = forms.CharField(required=False, label='Product Title')
    date = forms.DateField(label='Created At', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    price_from = forms.DecimalField(label='Min Price', required=False)
    price_to = forms.DecimalField(label='Max Price', required=False)