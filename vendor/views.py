from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.shortcuts import render
from django.contrib import messages

from customer.models import Order
from vendor.forms import UserLoginForm, UserRegForm
from django.contrib.auth import logout

from vendor.models import Vendor, MyUser, Role


def home(request):
    user = request.user
    if not request.user.is_anonymous:
        r = Role.objects.get(role='Staff')
        m = request.user.vendor.vendor
        if request.user.role == r:
            od = Order.objects.filter(~Q(invoice__order__status='Rejected'), employee__vendor=request.user.vendor, employee=user)
            orders = len(od)
            return render(request, 'dashboard.html',
                          {'staff': True, 'vendor': m, 'orders': orders, 'dashboard': True})
        else:
            od = Order.objects.filter(employee__vendor=request.user.vendor)
            emp = MyUser.objects.filter(vendor=request.user.vendor)
            orders = len(od)
            employee = len(emp)
            return render(request, "dashboard.html",
                          {'vendor': m, 'orders': orders, 'employees': employee, 'dashboard': True})
    return render(request, 'home.html', {})


def signup(request):
    return render(request, 'signup.html', {'reg_comp': True})


def reg_user(request):
    form = UserRegForm(request.POST, request.FILES)
    if form.is_valid():
        vendor = Vendor.objects.create(vendor=form.cleaned_data['c_name'],
                                       address=form.cleaned_data['c_address'], phone=form.cleaned_data['c_number'],
                                       logo=form.cleaned_data['c_image'])
        password = make_password(form.cleaned_data['password'])
        role = Role.objects.get(id=2)
        MyUser.objects.create(email=form.cleaned_data['email'], name=form.cleaned_data['name'],
                              password=password, address=form.cleaned_data['address'], vendor=vendor,
                              role=role, number=form.cleaned_data['number'])

    return render(request, 'home.html')


def login_user(request):
    if not request.user.is_anonymous:
        r = Role.objects.get(role='Staff')
        m = request.user.vendor.vendor
        user = request.user
        od = Order.objects.filter(employee__vendor=request.user.vendor)
        emp = MyUser.objects.filter(vendor=request.user.vendor)
        if user.role == r:
            od = Order.objects.filter(~Q(invoice__order__status='Rejected'), employee__vendor=request.user.vendor, employee=user)
            orders = len(od)
            return render(request, 'dashboard.html',
                          {'staff': True, 'vendor': m, 'orders': orders, 'dashboard': True})
        orders = len(od)
        employee = len(emp)
        return render(request, "dashboard.html",
                      {'vendor': m, 'orders': orders, 'employees': employee, 'dashboard': True})
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                m = request.user.vendor.vendor
                r = Role.objects.get(role='Staff')
                if user.role == r:
                    return render(request, 'dashboard.html', {'staff': True, 'vendor': m})
                return render(request, 'dashboard.html', {'vendor': m})
            else:
                messages.info(request, 'No such account!')
                return render(request, 'home.html', {'msg': True})
        else:
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')


def logout_user(request):
    logout(request)
    return render(request, "home.html")
