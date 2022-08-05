from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.urls import reverse
# Create your views here.

class Homepage(TemplateView):
    template_name = 'base.html'
class Homepage1(TemplateView):
    template_name = 'app1/templates/base1.html'