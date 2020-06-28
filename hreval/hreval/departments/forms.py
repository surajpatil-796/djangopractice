from django import forms
from .models import Department

class DepartmentPost(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'descriptt']