from operator import mod
from pyexpat import model
from django.db import models
from numpy import number
# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=25)
    number = models.IntegerField()
    