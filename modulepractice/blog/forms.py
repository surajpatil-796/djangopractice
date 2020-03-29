from django import forms
from .models import Article

class ArticlePost(forms.ModelForm):
    class Meta:
        model = Article 
        fields = ['title', 'content']
                              #validating title
    # def clean_title(self, *args, **kwargs):
    #     title= self.cleaned_data('title')
    #     qs= Article.objects.filters(title=title)
    #     if qs.exists():
    #         raise forms.ValidationError("same name")
    #     return title

