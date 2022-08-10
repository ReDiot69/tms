from django.http import Http404
from django.shortcuts import render
from customer.forms import CustomerForm, SearchForm
from customer.models import Customer, Measurement, Order, Category
from vendor.models import Vendor, MyUser, Role


def measurement(request):
    n = request.user.vendor.vendor
    if request.user.is_anonymous:
        return render(request, "home.html")
    vendor = Vendor.objects.get(vendor=request.user.vendor)
    m = MyUser.objects.filter(vendor=vendor)
    category = Category.objects.all()
    a = CustomerForm()
    r = Role.objects.get(role='Staff')
    if request.user.role == r:
        return render(request, 'measurement.html', {'staff': True, 'emp': m, 'vendor': n, 'category': category, 'form': a})
    return render(request, 'measurement.html', {'emp': m, 'category': category, 'vendor': n, 'form': a})


def account(request):
    if request.user.is_anonymous:
        return render(request, "home.html")
    r = Role.objects.get(role='Staff')

    m = request.user.vendor.vendor
    if request.user.role == r:
        return render(request, 'account.html', {'staff': True, 'vendor': m})
    return render(request, 'account.html', {'vendor': m})


def billing(request):
    return render(request, 'billing.html')


def order(request):
    m = request.user.vendor.vendor
    order = Order.objects.all()
    context = {'order': order, 'vendor': m}
    r = Role.objects.get(role='Staff')
    if request.user.role == r:
        return render(request, 'order.html', {'staff': True, 'vendor': m})
    return render(request, "order.html", context)


def orderSearch(request):
    form = SearchForm(request.POST)
    m = request.user.vendor.vendor
    if form.is_valid():
        data = form.cleaned_data['searchBox']

        try:
            nameCustomer = Order.objects.get(customer_measurement__customer__name=data)
            context = {'order': nameCustomer, 'singlecus': True, 'vendor': m}
        except:
            context = {'msg': 'Not found', 'vendor': m}
        return render(request, "order.html", context)

    return render(request, "order.html", {'vendor': m} )


def customer_store(request):
    m = request.user.vendor.vendor
    form = CustomerForm(request.POST, request.FILES)
    if form.is_valid():
        ct = form.cleaned_data['category']
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
        for cat in ct:
            m.category.add(cat)
            m.save()
        emp = MyUser.objects.get(id=form.cleaned_data['employee'])
        o = Order.objects.create(customer_measurement=m, deadline=form.cleaned_data['deadline'],
                                 employee=emp)
        context = {'order': o, 'reg': True, 'vendor': m}
    else:
        context = {'vendor': m}
    return render(request, 'billing.html', context)


def accounts_detail(request):
    pass


def dashboard(request):
    user = request.user
    if request.user.is_anonymous:
        return render(request, "home.html")
    else:
        m = request.user.vendor.vendor
        r = Role.objects.get(role='Staff')
        if user.role == r:
            return render(request, 'dashboard.html', {'staff': True, 'vendor':m})
        return render(request, "dashboard.html", {'vendor':m})


def login(request):
    return render(request, "home.html")
