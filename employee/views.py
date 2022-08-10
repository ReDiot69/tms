from urllib import request
from django.contrib.auth.hashers import make_password
from django.shortcuts import render

# Create your views here.
from employee.forms import EmployeeRegForm
from vendor.models import MyUser, Vendor, Role


# def employee(request):
#     return render(request, 'employee.html')


def reg_employ(request):
    form = EmployeeRegForm(request.POST, request.FILES)
    if form.is_valid():
        password = make_password(form.cleaned_data['password'])
        vendor = request.user.vendor
        v = Vendor.objects.get(vendor=vendor)
        role = Role.objects.get(id=3)
        MyUser.objects.create(name=form.cleaned_data['name'], number=form.cleaned_data['number'],
                              address=form.cleaned_data['address'], email=form.cleaned_data['email'],
                              password=password, image=form.cleaned_data['image'],
                              role=role, vendor=v)

    m = request.user.vendor.vendor
    return render(request, 'employee.html', {'vendor': m, 'reg_emp': True})


def employeelanding(request):
    if request.user.is_anonymous:
        return render(request, "home.html")
    user = request.user
    m = request.user.vendor.vendor
    emp_detail = MyUser.objects.filter(vendor=user.vendor)
    context = {'emp_detail': emp_detail, 'vendor': m}
    return render(request, 'employeelanding.html', context)

    