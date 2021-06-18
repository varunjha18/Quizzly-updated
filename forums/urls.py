from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
   path('', views.forums, name='forums'),
   path('<str:room_name>/', views.room2, name='room2'),
   
]