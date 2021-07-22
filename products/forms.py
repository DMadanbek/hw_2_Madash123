from django import forms
from products.models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields='__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : 'введите цену'
                }

            ),
            'discount': forms. NumberInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Введите скидку'
                }
            ),
            'category': forms.Select(
                attrs= {
                    'class': 'form-control'
                }

            'tags': forms.

            ),


        }
