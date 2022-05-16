from django.contrib import admin

# Register your models here.
from vendor.models import Vendor, MyUser, Role

admin.site.register(Vendor)
admin.site.register(MyUser)
admin.site.register(Role)



