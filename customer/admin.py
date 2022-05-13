from django.contrib import admin

from customer.models import Customer, Measurement, Order

# Register your models here.
admin.site.register(Customer)
admin.site.register(Measurement)
admin.site.register(Order)