from django.db import models
from django.urls import reverse
from roles.models import Role
from departments.models import Department

class Employee(models.Model):



    name = models.CharField(max_length=50)
    gmail= models.EmailField(max_length=50)
    
    role_name=models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    department_name=models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    
    def get_abs_url(self):
        return f"/employees/{self.id}"

    def get_update_url(self):
        return f"/employees/{self.id}/update"
    
    def get_delete_url(self):
        return f"/employees/{self.id}/delete"


