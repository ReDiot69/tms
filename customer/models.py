from django.db import models
import datetime


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    address = models.CharField(max_length=25)
    number = models.IntegerField()
    vendor = models.ForeignKey('user.Vendor', on_delete=models.CASCADE )

    def __str__(self):
        return self.name


class Measurement(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shoulder = models.FloatField()
    full_length = models.FloatField()
    chest = models.FloatField()
    hip = models.FloatField()
    sl = models.FloatField()
    m = models.FloatField()
    ah = models.FloatField()
    open = models.FloatField()
    thigh = models.FloatField()
    knee = models.FloatField()


class Order(models.Model):
    employee = models.ForeignKey('user.MyUser', on_delete=models.CASCADE)
    customer_measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    orderdate = models.DateField(auto_now=False, default=datetime.date.today)
    deadline = models.DateField(auto_now=False)
