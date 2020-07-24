from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class regi(models.Model):
     username = models.CharField(max_length=100)
     firstname = models.CharField(max_length=100)
     lastname =  models.CharField(max_length=100)
     email    =  models.CharField(max_length=30)
     password =  models.CharField(max_length=20)
     password2 = models.CharField(max_length=20)
     fileupload = models.ImageField(upload_to='profile_pics')
