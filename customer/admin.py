from django.contrib import admin

from customer.models import Customer, Measurement, Order, Category

# Register your models here.
admin.site.register(Customer)
admin.site.register(Measurement)
admin.site.register(Order)
admin.site.register(Category)