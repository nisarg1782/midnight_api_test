from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api_data/', views.api_data, name="api_data/"),
    path('', views.index, name="index")
]
