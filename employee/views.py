from django.shortcuts import render

# Create your views here.


def employee(request):
    return render(request, 'employee.html')

def reg_employ(request):
    return render(request, 'employeelanding.html', {'reg_emp':True})

def employeelanding(request):
    return render(request, 'employeelanding.html')