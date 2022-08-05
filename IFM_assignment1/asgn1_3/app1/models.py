from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()
class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.EmailField(default="")
    def __str__(self):
        return self.name

class Student(models.Model):
    student_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone_no = models.PositiveBigIntegerField()
    def __str__(self):
        return self.name


