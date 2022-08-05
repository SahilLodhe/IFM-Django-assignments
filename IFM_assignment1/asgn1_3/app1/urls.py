from django.urls import path
from app1 import views
from django.conf.urls import include

app_name = 'app1'
urlpatterns = [
    path('newStudent/',views.create_student,name='newStudent'),
    path('newEmployee/',views.create_employee,name='newEmployee'),
]