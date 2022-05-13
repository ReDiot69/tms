from django.shortcuts import render
from customer.forms import CustomerForm
from customer.models import Customer, Measurement

# Create your views here.
def measurement(request):
    return render(request, 'measurement.html')

def accounts(request):
    return render(request, 'accounts.html')


def customer(request):
    cus = Customer.objects.all()
    context = {'customer': cus}
    return render(request,"customer.html", context)
    
def customer_store(request):
    form = CustomerForm(request.POST)
    
    if form.is_valid():
        Customer.objects.create(name=form.cleaned_data['name'],email=form.cleaned_data['email'],address=form.cleaned_data['address'],
        number=form.cleaned_data['number'])
    return render(request,'measurement.html')



def accounts_detail(request):
    pass

