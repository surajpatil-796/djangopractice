from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title   = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return f"/blog/{self.id}"

    
    def get_edit_url(self):
        return f"/blog/{self.id}/update"

    
    def get_delete_url(self):
        return f"/blog/{self.id}/delete"
    
    