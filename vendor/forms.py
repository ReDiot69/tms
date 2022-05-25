from django import forms


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class UserRegForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=25)
    address = forms.CharField(max_length=25)
    number = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput())
    owner_image = forms.ImageField()

    c_name = forms.CharField(max_length=50)
    c_number = forms.IntegerField()
    c_address = forms.CharField(max_length=25)
    c_image = forms.ImageField()