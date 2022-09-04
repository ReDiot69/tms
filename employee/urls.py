from  django.urls import path
from .import views

urlpatterns = [
    # path('employee', views.employee, name="call_employee_page"),
    path('reg_emp', views.reg_employ),
    path('employee', views.employeelanding, name="call_employee_page"),
    path('empDelete', views.empDelete, name="delete_call_employee_page")
 ]

