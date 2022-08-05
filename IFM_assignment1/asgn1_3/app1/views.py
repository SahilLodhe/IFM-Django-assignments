from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.urls import reverse
from app1.models import Student,Employee
from app1.forms import CreateEmployeeForm,CreateStudentForm,UserCreateForm
# Create your views here.

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

class Homepage(TemplateView):
    template_name = 'base.html'
def create_student(request):
    context ={}
    form = CreateStudentForm(request.POST or None)
    if form.is_valid():
        form.save()
          
    context['form']= form
    return render(request,'create_student.html',context)

def create_employee(request):
    context ={}
    form = CreateEmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
          
    context['form']= form
    return render(request,'create_employee.html',context)