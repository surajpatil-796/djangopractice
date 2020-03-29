from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email') 
        print(email)#this gives me value
        if email.endswith(".edu"):
            raise forms.ValidationError("dont use .edu")
        return email