#Form Fields
from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="Enter user name", widget=forms.TextInput(attrs={'class':"form-control",}))
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':"form-control",}))

class RegisterForm(forms.Form):
    username = forms.CharField(label="Enter user name", min_length=8, widget=forms.TextInput(attrs={'class':"form-control",}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control",}))
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':"form-control",}))
    cpwd = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':"form-control",}))

    def clean_username(self):
        if User.objects.filter(username__iexact=self.cleaned_data.get('username')).exists():
            raise ValidationError("Username already taken.")
        return self.cleaned_data.get('username')

    def clean(self):
        data = self.cleaned_data
        if data.get('pwd') == data.get('cpwd'):
            return data
        else:
            raise ValidationError("Both Password's don't match")

