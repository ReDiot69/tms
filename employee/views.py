import re
from django.contrib.auth.hashers import make_password
from django.shortcuts import render

# Create your views here.
from employee.forms import EmployeeRegForm
from vendor.models import MyUser, Vendor, Role
# subha
from .models import Employee

def all_data_employee(request):
    emp_data=Employee.objects.all()
    return render(request,'employeelanding.html',{'emp_data':emp_data})

def __str__(self):
    return self.emp_data

def displayInfoEmp(request):
    fetchemp= MyUser.objects.all()
    return render(request,'employee.html',{'fetchemp':fetchemp})
# subha end
def employee(request): 
    return render(request, 'employee.html')

def reg_employ(request):
    form = EmployeeRegForm(request.POST, request.FILES)
    if form.is_valid():
        vendor = request.user.vendor
        v = Vendor.objects.get(vendor=vendor)
        role = Role.objects.get(id=3)
        Employee.objects.create(name=form.cleaned_data['name'],
                                number=form.cleaned_data['number'],
                                address=form.cleaned_data['address'],
                                email=form.cleaned_data['email'],
                                password=make_password(form.cleaned_data['password']), 
                                image=form.cleaned_data['image'],
                                role=role, vendor=v)
    return render(request, 'employee.html', {'reg_emp': True})

def employeelanding(request):
    return render(request, 'employeelanding.html')