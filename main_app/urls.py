from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('diet/<int:diet_id>', views.diet),
    path('add_user/', views.add_user),
]
