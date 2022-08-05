from django.shortcuts import render
from django.urls import path
from django.contrib import admin
from app1 import views
from django.conf.urls import include

app_name = 'app1'
urlpatterns = [
    path('',views.Homepage.as_view(),name='Homepage'),
    path('home1/',views.Homepage1.as_view(),name='Homepage1'),
]