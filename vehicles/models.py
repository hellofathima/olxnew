from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Autos(models.Model):
    type=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    year=models.CharField(max_length=200)
    kmdriven=models.CharField(max_length=200)
    description=models.CharField(max_length=300)
    price=models.CharField(max_length=300,null=True)
    phn=models.CharField(max_length=200,null=True)
    image=models.ImageField(upload_to="images",null=True)
    user=user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
       
        return self.type