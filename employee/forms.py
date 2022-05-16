from django import forms


class EmployeeRegForm(forms.Form):
    name = forms.CharField(max_length=25)
    address = forms.CharField(max_length=25)
    number = forms.IntegerField()
    image = forms.ImageField()
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
