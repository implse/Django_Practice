from django import forms

from .models import Product

# Create a ModelForm
class ProductForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Product
        fields = ['product', 'purchase', 'sale', 'qty', 'gender', 'note']
