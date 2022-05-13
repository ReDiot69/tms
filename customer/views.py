from django.shortcuts import render
from customer.forms import CustomerForm
from customer.models import Customer, Measurement

# Create your views here.
def measurement(request):
    return render(request, 'measurement.html')

def accounts(request):
    return render(request, 'accounts.html')

def employee(request):
    return render(request, 'employee.html')

def customer(request):
    return render(request,"customer.html")
    
def customer_store(request):
    form = CustomerForm(request.POST)
    
    if form.is_valid():
        Customer.objects.create(name=form.cleaned_data['name'],email=form.cleaned_data['email'],address=form.cleaned_data['address'],
        number=form.cleaned_data['number'])
    return render(request,'measurement.html')



def accounts_detail(request):
    pass

