from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/<int:user_id>', views.user),
    path('add_user/', views.add_user),
]
