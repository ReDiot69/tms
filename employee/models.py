from tkinter import CASCADE
from django.db import models
from cgitb import text
import email
import imp
from django.db import models
import datetime

import vendor
# Create your models here.
class Employee(models.Model):
    vendor = models.ForeignKey('vendor.Vendor',on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email =models.EmailField()
    address = models.CharField(max_length=25)
    number = models.IntegerField()

class EmployeeOrder(models.Model):
    order = models.ForeignKey('customer.Order',on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)