from unicodedata import name
from django.shortcuts import render
from django.urls import path
from django.contrib import admin
from app2 import views

app_name = 'app2'
urlpatterns = [
    path('home2/',views.Homepage2.as_view(),name='Homepage2')
]