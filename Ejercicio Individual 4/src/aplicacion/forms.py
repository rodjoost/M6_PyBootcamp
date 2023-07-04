from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label="Nombre de Usuario", widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={"class":"form-control"}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label="Confirme contraseña", widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}