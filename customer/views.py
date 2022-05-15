from django.shortcuts import render
from customer.forms import CustomerForm
from customer.models import Customer, Measurement, Order
from employee.models import Employee


def measurement(request):
    form = CustomerForm()
    emp = Employee.objects.all()
    context = {'employee': emp, 'form': form}
    return render(request, 'measurement.html', context)


def account(request):
    return render(request, 'account.html')


def customer(request):
    cus = Customer.objects.all()
    context = {'customer': cus}
    return render(request, "customer.html", context)


def customer_store(request):
    form = CustomerForm(request.POST, request.FILES)
    if form.is_valid():
        c = Customer.objects.create(name=form.cleaned_data['name'], email=form.cleaned_data['email'],
                                    address=form.cleaned_data['address'],
                                    number=form.cleaned_data['number'])
        m = Measurement.objects.create(customer=c, shoulder=form.cleaned_data['shoulder'],
                                       full_length=form.cleaned_data['full_length'],
                                       chest=form.cleaned_data['chest'], hip=form.cleaned_data['hip'],
                                       sl=form.cleaned_data['sl'], m=form.cleaned_data['m'], ah=form.cleaned_data['ah'],
                                       open=form.cleaned_data['open'], thigh=form.cleaned_data['thigh'],
                                       knee=form.cleaned_data['knee'], image=form.cleaned_data['image'])
        emp = Employee.objects.get(id=form.cleaned_data['employee'])
        Order.objects.create(customer_measurement=m, deadline=form.cleaned_data['deadline'],
                             employee=emp)
        context = {'reg': True}
    else:
        context = {}

    return render(request, 'measurement.html', context)


def accounts_detail(request):
    pass


def dashboard(request):
    return render(request,"dashboard.html")

