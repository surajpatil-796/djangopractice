from django import forms
from .models import Role

class RolePost(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'descript']