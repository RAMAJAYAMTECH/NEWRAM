from django.db import models

# Create your models here.
class Messagebox(models.Model):
    Name= models.CharField(max_length=30,null=True)
    Email = models.EmailField(null=True)
    Message = models.CharField(max_length=30,null=True)

class getintouch(models.Model):
    c_name= models.CharField(max_length=30,null=True)
    c_phone = models.IntegerField(null=True,max_length=10)
    c_email = models.EmailField(null=True)
    text = models.CharField(max_length=30,null=True)