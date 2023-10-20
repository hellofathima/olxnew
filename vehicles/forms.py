from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from vehicles.models import Autos

class RegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username","email","password1","password2"]
    
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class AutoCreateForm(forms.ModelForm):
    class Meta:
        model=Autos
        fields=["type","brand","year","kmdriven","description","price","phn","image"]

class AutoChangeForm(forms.ModelForm):

    class Meta:
        model=Autos
        exclude=("user",)
