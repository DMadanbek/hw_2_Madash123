from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rfc3986.exceptions import ValidationError

from django_project import settings
from products.models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'введите цену'
                }

            ),
            'discount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите скидку'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            # 'tags': forms.SelectMultiple(

        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=3,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control'
                                   }
                               ))

    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control'
                                   }
                               ))


class RegisterForm(forms.Form):
    username = forms.EmailField(max_length=100, min_length=3,
                                label='Email',
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))

    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control'
                                   }
                               ))
    password1 = forms.CharField(max_length=100,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control'
                                    }
                                ))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).count() > 0:
            raise ValidationError('Пользователь уже существует')
        return username

    def clean_password1(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']

        if password != password1:
            raise ValidationError('Пароли не совпадают!')
        return password1

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            is_active=True
        )
        user.save()
        send_mail(
            message='Test django message',
            subject='Registration test',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.cleaned_data['username']]
        )
        return user
