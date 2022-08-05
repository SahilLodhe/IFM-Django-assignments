from unicodedata import name
from django.shortcuts import render
from django.urls import path
from django.contrib import admin
from app3 import views

app_name = 'app3'
urlpatterns = [
    path('home3/',views.Homepage3,name='Homepage3'),
]