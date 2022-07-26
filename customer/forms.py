from datetime import datetime
from django import forms
from django.contrib.postgres.forms import SimpleArrayField

from customer.models import Category, Measurement


class CustomerForm(forms.Form):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all()
    )
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    address = forms.CharField(max_length=25)
    number = forms.IntegerField()
    shoulder = forms.FloatField(required=False)
    full_length = forms.FloatField(required=False)
    chest = forms.FloatField(required=False)
    hip = forms.FloatField(required=False)
    sl = forms.FloatField(required=False)
    m = forms.FloatField(required=False)
    ah = forms.FloatField(required=False)
    open = forms.FloatField(required=False)
    thigh = forms.FloatField(required=False)
    knee = forms.FloatField(required=False)
    employee = forms.IntegerField()
    deadline = forms.DateField()
    image = forms.ImageField()