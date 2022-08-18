from django.http import Http404
from django.shortcuts import render
from customer.forms import CustomerForm, SearchForm, BillingForm
from customer.models import Customer, Measurement, Order, Description, Invoice, OrderedDescription, InvoiceDetail
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
    m = request.user.vendor

    if request.user.role == r:
        invoice = InvoiceDetail.objects.filter(invoice__order__employee__role=r)
        return render(request, 'account.html', {'invoice': invoice, 'staff': True, 'vendor': m.vendor, 'accounts': True})
    invoice = InvoiceDetail.objects.filter(invoice__order__employee__vendor=m, invoice__status='Not Paid')
    return render(request, 'account.html', {'invoice': invoice, 'vendor': m.vendor, 'accounts': True})

def historyacc(request):
    if request.user.is_anonymous:
        return render(request, "home.html")
    r = Role.objects.get(role='Staff')
    m = request.user.vendor

    if request.user.role == r:
        invoice = InvoiceDetail.objects.filter(invoice__order__employee__role=r)
        return render(request, 'historyacc.html', {'invoice': invoice, 'staff': True, 'vendor': m.vendor, 'history': True})
    invoice = InvoiceDetail.objects.filter(invoice__order__employee__vendor=m, invoice__status='Not Paid')
    return render(request, 'historyacc.html', {'invoice': invoice, 'vendor': m.vendor, 'history': True})


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
        InvoiceDetail.objects.create(advance=form.cleaned_data['advance'], remain=i.net_total-form.cleaned_data['advance'],
                                     invoice=i)
    return render(request, 'billing.html', {'invoice': i})


def order(request):
    m = request.user.vendor
    r = Role.objects.get(role='Staff')
    if request.user.role == r:
        try:
            o = Order.objects.filter(employee=request.user, status='Not Complete', emp_status='ACCEPTED')
            return render(request, 'order.html', {'order': o, 'staff': True, 'vendor': m})
        except:
            return render(request, 'order.html', {'staff': True, 'vendor': m})
    try:
        od = Order.objects.filter(employee__vendor=m, status='Not Complete', emp_status='ACCEPTED')
    except:
        od = None
    context = {'order': od, 'vendor': m.vendor, 'order_nav': True}
    return render(request, "order.html", context)

def acceptorder(request):
    m = request.user.vendor
    r = Role.objects.get(role='Staff')
    if request.user.role == r:
        try:
            o = Order.objects.filter(employee=request.user, status='Not Complete')
            return render(request, 'acceptacceptorder.html', {'order': o, 'staff': True, 'vendor': m})
        except:
            return render(request, 'acceptorder.html', {'staff': True, 'vendor': m})
    try:
        od = Order.objects.filter(employee__vendor=m, status='Not Complete')
    except:
        od = None
    context = {'order': od, 'vendor': m.vendor, 'acceptorder': True}
    return render(request, "acceptorder.html", context)

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



def dashboard(request):
    user = request.user
    if request.user.is_anonymous:
        return render(request, "home.html")
    else:
        m = request.user.vendor.vendor
        r = Role.objects.get(role='Staff')
        od = Order.objects.filter(employee__vendor=request.user.vendor)
        emp = MyUser.objects.filter(vendor=request.user.vendor)
        if user.role == r:
            od = Order.objects.filter(employee__vendor=request.user.vendor, employee=user)
            orders = len(od)
            return render(request, 'dashboard.html',
                          {'staff': True, 'vendor': m, 'orders': orders, 'dashboard': True})
        orders = len(od)
        employee = len(emp)
        return render(request, "dashboard.html",
                      {'vendor': m, 'orders': orders, 'employees': employee, 'dashboard': True})


def login(request):
    return render(request, "home.html")
