from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from vendor.forms import UserLoginForm


def home(request):
    return render(request,'home.html',{})

def signup(request):
    return render(request,'signup.html',{'reg_comp': True})


def login(request):
    form = UserLoginForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user:
            return render(request, 'dashboard.html')
        else:
            messages.info(request, 'No such account!')
            return render(request, 'home.html', {'msg': True})
    else:
        return render(request, 'home.html') 