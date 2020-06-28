from django.db import models
from roles.models import Role


class Department(models.Model):
    name = models.CharField(max_length=50)
    descriptt=models.CharField(max_length=100)
    role=models.ForeignKey(Role, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    
    def get_dedit_url(self):
        return f"/departments/{self.id}/update"
    
    def get_ddelete_url(self):
        return f"/departments/{self.id}/delete"