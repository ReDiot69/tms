from datetime import datetime
from django import forms


class CustomerForm(forms.Form):
    name = forms.CharField(max_length=25)
    category = forms.IntegerField()
    email = forms.EmailField()
    address = forms.CharField(max_length=25)
    number = forms.IntegerField()
    shoulder = forms.FloatField()
    full_length = forms.FloatField()
    chest = forms.FloatField()
    hip = forms.FloatField()
    sl = forms.FloatField()
    m = forms.FloatField()
    ah = forms.FloatField()
    open = forms.FloatField()
    thigh = forms.FloatField()
    knee = forms.FloatField()
    employee = forms.IntegerField()
    deadline = forms.DateField()
    image = forms.ImageField()