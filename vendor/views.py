from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from vendor.forms import UserLoginForm, UserRegForm
from django.contrib.auth import logout

from vendor.models import Vendor, MyUser, Role


def home(request):
    return render(request, 'home.html', {})


def signup(request):
     return render(request, 'signup.html', {'reg_comp': True})
def home1(request):
     return render(request, 'home1.html',{})

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
    if request.method== 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return render(request, 'dashboard.html')
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
