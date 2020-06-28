from django import forms
from .models import Employee

class EmployeePost(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'gmail', 'department_name','role_name']