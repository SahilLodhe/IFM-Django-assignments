from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.urls import reverse
# Create your views here.

# class Homepage3(TemplateView):
#     template_name = "app3/templates/base3.html"

def Homepage3(request):
    return render(request,'app3/templates/base3.html')