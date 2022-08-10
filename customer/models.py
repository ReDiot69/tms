from uuid import uuid4
from django.db import models
import datetime


class Customer(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    address = models.CharField(max_length=25)
    number = models.IntegerField()
    vendor = models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Description(models.Model):
    description = models.CharField(max_length=25)

    def __str__(self):
        return self.description


class Measurement(models.Model):
    description = models.ManyToManyField(Description)
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


STATUS_COM = (
    (1, 'Not Complete'),
    (2, 'Completed')
)


class Order(models.Model):
    employee = models.ForeignKey('vendor.MyUser', on_delete=models.CASCADE)
    customer_measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    orderdate = models.DateField(auto_now=False, default=datetime.date.today)
    deadline = models.DateField(auto_now=False)
    status = models.IntegerField(choices=STATUS_COM, default=1)

# def create_id():
#     now = datetime.datetime.now()
#     return str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)+str(int(uuid4()))[:1]
#
#
# class OrderedCategory(models.Model):
#
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     subtotal = models.DecimalField(max_digits=9, decimal_places=4)
#     status = models.IntegerField(choices=STATUS_COM, default=1)
#     description = models.TextField()
#
#
# class Invoice(models.Model):
#     STATUS = (
#         (1, 'Paid'),
#         (2, 'Not Paid')
#     )
#     id = models.CharField(max_length=20, primary_key=True, default=create_id, editable=False)
#     order = models.OneToOneField(Order, on_delete=models.CASCADE)
#     date = models.DateField(default=datetime.date.today)
#     vat = models.IntegerField(default=13)
#     discount = models.FloatField()
#     total = models.DecimalField(decimal_places=4, max_digits=9)
#     advance = models.DecimalField(decimal_places=4, max_digits=9)
#     remaining = models.DecimalField(decimal_places=4, max_digits=9)
#     status = models.IntegerField(choices=STATUS, default=2)
#     ordercat = models.ManyToManyField(OrderedCategory)
