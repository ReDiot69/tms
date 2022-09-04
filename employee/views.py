from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from employee.forms import EmployeeRegForm
from vendor.models import MyUser, Vendor, Role
from customer.models import  Order


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
    username = request.user.name
    return render(request, 'employeelanding.html', {'vendor': m, 'reg_emp': True,'name':username})


def employeelanding(request):
    if request.user.is_anonymous:
        return render(request, "home.html")
    user = request.user
    m = request.user.vendor.vendor
    username = request.user.name
    emp_detail = MyUser.objects.filter(vendor=user.vendor)
    r = Role.objects.get(role='Staff')
    if request.user.role == r:
        context = {'emp_detail': emp_detail, 'vendor': m,'staff': True,'employ': True,'name':username}
    else:
        context = {'emp_detail': emp_detail, 'vendor': m,'employ': True,'name':username}
    return render(request, 'employeelanding.html', context)

def empDelete(request):
    if request.user.is_anonymous:
        return render(request, "home.html")
    user = request.user
    m = request.user.vendor.vendor
    username = request.user.name
    emp = MyUser.objects.filter(id=request.POST.get('id')).delete()
    emp_detail = MyUser.objects.filter(vendor=user.vendor)
    context = {'emp_detail': emp_detail, 'vendor': m,'employ': True,'name':username}
    return render(request, 'employeelanding.html', context)
