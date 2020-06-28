from django.db import models

class Role(models.Model):
    name= name = models.CharField(max_length=50)
    descript= models.CharField(max_length=100) 
      
 
    def __str__(self):
        return self.name

    
    def get_abs_url(self):
        return f"/roles/{self.id}"

    def get_edit_url(self):
        return f"/roles/{self.id}/update"
    
    def get_rdelete_url(self):
        return f"/roles/{self.id}/delete"



