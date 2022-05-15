from django.contrib import admin

# Register your models here.
from user.models import MyUser, Vendor, Role

admin.site.register(MyUser)
admin.site.register(Vendor)
admin.site.register(Role)