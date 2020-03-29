from django import forms
from .models import Task

class TaskPost(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'user', 'description','image']