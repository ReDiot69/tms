from  django.urls import path
from .import views

urlpatterns = [
    path('employee', views.employee, name="call_employee_page"),
 ]

# new branch
