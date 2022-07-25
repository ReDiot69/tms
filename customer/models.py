from django.db import models
import datetime


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    address = models.CharField(max_length=25)
    number = models.IntegerField()
    vendor = models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=25)


class Measurement(models.Model):
    category = models.ManyToManyField(Category)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shoulder = models.FloatField(null=True)
    full_length = models.FloatField(null=True)
    chest = models.FloatField(null=True)
    hip = models.FloatField(null=True)
    sl = models.FloatField(null=True)
    m = models.FloatField(null=True)
    ah = models.FloatField(null=True)
    open = models.FloatField(null=True)
    thigh = models.FloatField(null=True)
    knee = models.FloatField(null=True)
    image = models.ImageField()


class Order(models.Model):
    employee = models.ForeignKey('vendor.MyUser', on_delete=models.CASCADE)
    customer_measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    orderdate = models.DateField(auto_now=False, default=datetime.date.today)
    deadline = models.DateField(auto_now=False)


# class Invoice(models.Models):
#     order =
#     total =
#     advance =
#     remai = asdasd