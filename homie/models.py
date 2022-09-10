from distutils.command.upload import upload
import email
from unicodedata import name
from django.db import models
from django.forms import CharField

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name
    
class IceCream(models.Model):
    heading = models.CharField(max_length=122)
    desc = models.CharField(max_length=122)
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)
    price = models.IntegerField(default=499)
    
    def __str__(self):
        return self.heading