from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "image"]



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Require email

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]  # Fields to show in the form