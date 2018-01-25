import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Users
from .models import Diets
from .models import Days
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

def diet(request,diet_id):
    diet = Diets.objects.get(id=diet_id)
    dietsid = Diets.objects.all().values_list('id',flat=True)
    try:
        diet.days = Days.objects.filter(diet=int(diet_id))
    except:
       print("Error")
    try:
       diet.foods = json.loads(diet.foods)
       diet.exercises = json.loads(diet.exercises)
    except:
       print("Error")

    return render(request,"diet.html",{'diet':diet,'dietsid':dietsid})
