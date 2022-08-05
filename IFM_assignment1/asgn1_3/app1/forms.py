from dataclasses import fields
from pyexpat import model
from app1.models import Student,Employee
from django import forms
from . models import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()
class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id','name','address','phone_no']
class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id','name','address','email']