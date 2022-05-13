from dataclasses import field
from django import forms
from django.shortcuts import render

from customer.models import Customer, Measurement

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
