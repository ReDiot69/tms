from django.db import models


# Create your models here.
class Employee(models.Model):
    vendor = models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    address = models.CharField(max_length=25)
    number = models.IntegerField()

    def __str__(self):
        return self.name


# git check
