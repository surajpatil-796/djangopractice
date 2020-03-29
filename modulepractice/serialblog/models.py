from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    dateCreated = models.DateTimeField('date created', auto_now_add=True)
    dateUpdated = models.DateTimeField('date updated', auto_now=True)

    
    def __str__(self):
        return self.name
    
    
    
    def get_abs_url(self):
        return f"/serialblog/{self.id}"
