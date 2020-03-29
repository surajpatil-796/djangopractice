from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class TaskPract(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
    
    # def get_abs_url(self):
    #     return f"/serialpractice/{self.id}"
