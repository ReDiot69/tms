from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from vendor.forms import UserLoginForm
from django.contrib.auth import logout

def home(request):
    return render(request,'home.html',{})


def signup(request):
    
    return render(request,'signup.html',{'reg_comp': True})


def loginUser(request):
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


def logoutUser(request):
    logout(request)
    return render(request, "home.html");