from django.contrib import admin
from .models import Users
from .models import Diets
from .models import Days

# Register your models here.
admin.site.register(Users)
admin.site.register(Diets)
admin.site.register(Days)
