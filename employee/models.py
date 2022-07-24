from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=25)
    number = models.IntegerField()
    address = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(null=False, max_length=256)
    image = models.ImageField(max_length=255, null=True)
    role = models.CharField(max_length=25)
    vendor = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
