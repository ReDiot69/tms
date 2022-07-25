from django.http import Http404
from django.shortcuts import render
from customer.forms import CustomerForm
from customer.models import Customer, Measurement, Order, Category
from vendor.models import Vendor, MyUser


def measurement(request):
    vendor = Vendor.objects.get(vendor=request.user.vendor)
    m = MyUser.objects.filter(vendor=vendor)
    category = Category.objects.all()
    return render(request, 'measurement.html', {'emp': m, 'category': category})


def account(request):
    return render(request, 'account.html')


def billing(request):
    return render(request, 'billing.html')


def order(request):
    order = Order.objects.all()
    context = {'order': order}
    return render(request, "order.html", context)


def customer_store(request):
    form = CustomerForm(request.POST, request.FILES)
    if form.is_valid():
        cat = Category.objects.get(id=form.cleaned_data['category'])
        vendor = request.user.vendor
        v = Vendor.objects.get(vendor=vendor)
        c = Customer.objects.create(name=form.cleaned_data['name'], email=form.cleaned_data['email'],
                                    address=form.cleaned_data['address'],
                                    number=form.cleaned_data['number'], vendor=v)
        m = Measurement.objects.create(customer=c, shoulder=form.cleaned_data['shoulder'],
                                       full_length=form.cleaned_data['full_length'], image=form.cleaned_data['image'],
                                       chest=form.cleaned_data['chest'], hip=form.cleaned_data['hip'],
                                       sl=form.cleaned_data['sl'], m=form.cleaned_data['m'], ah=form.cleaned_data['ah'],
                                       open=form.cleaned_data['open'], thigh=form.cleaned_data['thigh'],
                                       knee=form.cleaned_data['knee'])
        m.category.add(cat)
        m.save()
        emp = MyUser.objects.get(id=form.cleaned_data['employee'])
        Order.objects.create(customer_measurement=m, deadline=form.cleaned_data['deadline'],
                             employee=emp)
        context = {'reg': True}
    else:
        context = {}
    return render(request, 'measurement.html', context)


def accounts_detail(request):
    pass


def dashboard(request):
    if request.user == 'AnonymousUser':
        return render(request, "home.html")
    else:
        return render(request, "dashboard.html")


def login(request):
    return render(request, "home.html")
