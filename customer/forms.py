from django import forms


class CustomerForm(forms.Form):
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

class SearchForm(forms.Form):
    searchBox = forms.CharField()
