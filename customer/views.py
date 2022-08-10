from django.http import Http404
from django.shortcuts import render
from customer.forms import CustomerForm, SearchForm, BillingForm
from customer.models import Customer, Measurement, Order, Description, Invoice, OrderedDescription
from vendor.models import Vendor, MyUser, Role


def measurement(request):
    n = request.user.vendor.vendor
    if request.user.is_anonymous:
        return render(request, "home.html")
    vendor = Vendor.objects.get(vendor=request.user.vendor)
    m = MyUser.objects.filter(vendor=vendor)
    a = CustomerForm()
    r = Role.objects.get(role='Staff')
    if request.user.role == r:
        return render(request, 'measurement.html',
                      {'staff': True, 'emp': m, 'vendor': n, 'form': a, 'measurement': True})
    return render(request, 'measurement.html', {'emp': m, 'vendor': n, 'form': a, 'measurement': True})


def account(request):
    if request.user.is_anonymous:
        return render(request, "home.html")
    r = Role.objects.get(role='Staff')
    m = request.user.vendor.vendor
    if request.user.role == r:
        return render(request, 'account.html', {'staff': True, 'vendor': m, 'accounts': True})
    return render(request, 'account.html', {'vendor': m, 'accounts': True})


def billing(request):
    form = BillingForm(request.POST)
    if form.is_valid():
        des = request.POST.getlist('description')
        des_price = request.POST.getlist('price')
        le = len(des)
        o = Order.objects.get(id=request.POST.get('order'))
        i = Invoice.objects.create(order=o, discount=form.cleaned_data['discount'],
                                   net_total=form.cleaned_data['nettotal'], gross_total=form.cleaned_data['grosstotal'])
        for d in range(le):
            descrip = Description.objects.create(description=des[d])
            od = OrderedDescription.objects.create(description=descrip, subtotal=des_price[d])
            i.orderdes.add(od)
            i.save()
        print(i)
    return render(request, 'billing.html', {'invoice': i})


def order(request):
    m = request.user.vendor
    r = Role.objects.get(role='Staff')
    if request.user.role == r:
        o = Order.objects.filter(employee=r)
        return render(request, 'order.html', {'order': o, 'staff': True, 'vendor': m})
    od = Order.objects.filter(employee__vendor=m)
    context = {'order': od, 'vendor': m.vendor, 'order_nav': True}
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

    return render(request, "order.html", {'vendor': m})


def customer_store(request):
    me = request.user.vendor.vendor
    form = CustomerForm(request.POST, request.FILES)
    if form.is_valid():
        descriptions = request.POST.getlist('des')
        vendor = request.user.vendor
        v = Vendor.objects.get(vendor=vendor)
        try:
            c = Customer.objects.get(email=form.cleaned_data['email'], number=form.cleaned_data['number'])
        except:
            c = Customer.objects.create(name=form.cleaned_data['name'], email=form.cleaned_data['email'],
                                        address=form.cleaned_data['address'],
                                        number=form.cleaned_data['number'], vendor=v)
        m = Measurement.objects.create(customer=c, shoulder=form.cleaned_data['shoulder'],
                                       full_length=form.cleaned_data['full_length'], image=form.cleaned_data['image'],
                                       chest=form.cleaned_data['chest'], hip=form.cleaned_data['hip'],
                                       sl=form.cleaned_data['sl'], m=form.cleaned_data['m'], ah=form.cleaned_data['ah'],
                                       open=form.cleaned_data['open'], thigh=form.cleaned_data['thigh'],
                                       knee=form.cleaned_data['knee'])
        for description in descriptions:
            des = Description.objects.create(description=description)
            m.description.add(des)
            m.save()
        emp = MyUser.objects.get(id=form.cleaned_data['employee'])
        o = Order.objects.create(customer_measurement=m, deadline=form.cleaned_data['deadline'],
                                 employee=emp)
        context = {'order': o, 'reg': True, 'vendor': me}
    else:
        context = {'vendor': me}
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
        od = Order.objects.filter(employee__vendor=request.user.vendor)
        emp = MyUser.objects.filter(vendor=request.user.vendor)
        orders = len(od)
        employee = len(emp)
        if user.role == r:
            return render(request, 'dashboard.html',
                          {'staff': True, 'vendor': m, 'orders': orders, 'employees': employee, 'dashboard': True})
        return render(request, "dashboard.html",
                      {'vendor': m, 'orders': orders, 'employees': employee, 'dashboard': True})


def login(request):
    return render(request, "home.html")
