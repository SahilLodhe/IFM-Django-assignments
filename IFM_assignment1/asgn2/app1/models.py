from django.db import models
from django.urls import reverse
from django import forms

# Create your models here.
class Company(models.Model):
    company_id = models.IntegerField(primary_key=True)
    domain = models.URLField()
    address = models.CharField(max_length=100)
    email = models.EmailField()
    name = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("app1:home")


class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=25)
    employee_company_id = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='employee')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("app1:home")
