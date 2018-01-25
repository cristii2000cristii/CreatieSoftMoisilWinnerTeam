from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Users
from .models import Diets
from .forms import UsersForm

# Create your views here.

def add_user(request):
    form = UsersForm(request.POST)
    if form.is_valid():
        users = Users(name = form.cleaned_data['name'],
                      email = form.cleaned_data['email'],
                      phone = form.cleaned_data['phone'],
                      adress = form.cleaned_data['adress'])
        users.save()
    return HttpResponseRedirect('/')

def index(request):
    diets = Diets.objects.all()
    return render(request,"index.html",{'diets':diets})

def user(request,user_id):
    user = Users.objects.get(id=user_id)
    return render(request,"user.html",{'user':user})
