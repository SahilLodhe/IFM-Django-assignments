from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from app1.models import Employee,Company
# Create your views here.

class Homepage(TemplateView):
    template_name = "base.html"

class CreateCompany(CreateView):
    model = Company
    fields = ['domain','address','email','name']

class CompanyList(ListView):
    model = Company
    context_object_name = 'company_list'
    def get_queryset(self):
        return Company.objects.order_by('-company_id')

class CompanyDetail(DetailView):
    model = Company
    context_object_name = 'company'

class CompanyUpdate(UpdateView):
    model = Company
    fields = ['domain','address','email','name']
    success_url = "/"

class CompanyDelete(DeleteView):
    model = Company
    success_url = reverse_lazy('app1:CompanyList')
    template_name = 'app1/company_confirm_delete.html'

class CreateEmployee(CreateView):
    model = Employee
    fields = ['name','address','email','position','employee_company_id']

class EmployeeList(ListView):
    model = Employee
    context_object_name = 'employee_list'
    def get_queryset(self):
        return Employee.objects.order_by('-emp_id')

class EmployeeDetail(DetailView):
    model = Employee
    context_object_name = 'employee'

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name','address','email','position','employee_company_id']
    success_url = "/"

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('app1:EmployeeList')
    template_name = 'app1/employee_confirm_delete.html'





















# class CreateEmployee(CreateView):
#     model = Employee
#     fields = "__all__"

# class EmployeeListView(ListView):
#     model = Employee
#     context_object_name = 'Employee_list'
#     no_of_employees = Employee.objects.count()
#     extra_context = {'no_of_employees' : no_of_employees}
#     def get_queryset(self):
#         return Employee.objects.all()

# class EmployeeDetailView(DetailView):
#     model = Employee
#     context_object_name = 'employee'

# class EmployeeUpdateView(UpdateView):
#     model = Employee
#     fields = ['address','email','position']
#     success_url = "/"

# class EmployeeDeleteView(DeleteView):
#     model = Employee
#     success_url = reverse_lazy('app1:home')

# class CreateCompany(CreateView):
#     model = Company
#     fields = "__all__"

# class CompanyListView(ListView):
#     model = Company
#     context_object_name = 'Company_list'
#     no_of_companies = Employee.objects.count()
#     extra_context = {'no_of_companies',no_of_companies}
#     def get_queryset(self):
#         return Company.objects.all()

# class CompanyDetailView(DetailView):
#     model = Company
#     context_object_name = 'company'

# class CompanyUpdateView(UpdateView):
#     model = Company
#     fields = ['domain','address','email']
#     success_url = "/"

# class CompanyDeleteView(DeleteView):
#     model = Company
#     success_url = reverse_lazy('app1:home')