from django import forms

# Create your models here.
class UsersForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    phone = forms.IntegerField()
    adress = forms.CharField(max_length=100)
