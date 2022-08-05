from app1 import views
from django.conf.urls import include
from django.urls import path

app_name = 'app1'
urlpatterns = [
    path('',views.Homepage.as_view(),name='home'),
    # path('NewCompany/',views.CreateCompany.as_view(),name='NewCompany'),
    # path('NewEmployee/',views.CreateEmployee.as_view(),name='NewEmployee'),
    # path('CompanyList/',views.CompanyListView.as_view(),name='CompanyList'),
    # path('EmployeeList/',views.EmployeeListView.as_view(),name='EmployeeList'),
    # path('CompanyDetail/<int:pk>/',views.CompanyDetailView.as_view(),name='CompanyDetail'),
    # path('EmployeeDetail/<int:pk>/',views.EmployeeDetailView.as_view(),name='EmployeeDetail'),
    # path('CompanyUpdate/<int:pk>/',views.CompanyUpdateView.as_view(),name='CompanyUpdate'),
    # path('EmployeeUpdate/<int:pk>/',views.EmployeeUpdateView.as_view(),name='EmployeeUpdate'),
    # path('CompanyDelete/<int:pk>/',views.CompanyDeleteView.as_view(),name='CompanyDelete'),
    # path('EmployeeDelete/<int:pk>/',views.EmployeeDeleteView.as_view(),name='EmployeeDelete'),
    path('NewCompany/',views.CreateCompany.as_view(),name='NewCompany'),
    path('NewEmployee/',views.CreateEmployee.as_view(),name='NewEmployee'),
    path('CompanyList/',views.CompanyList.as_view(),name='CompanyList'),
    path('EmployeeList/',views.EmployeeList.as_view(),name='EmployeeList'),
    path('CompanyDetail/<int:pk>/',views.CompanyDetail.as_view(),name='CompanyDetail'),
    path('EmployeeDetail/<int:pk>/',views.EmployeeDetail.as_view(),name='EmployeeDetail'),
    path('CompanyUpdate/<int:pk>/',views.CompanyUpdate.as_view(),name='CompanyUpdate'),
    path('EmployeeUpdate/<int:pk>/',views.EmployeeUpdate.as_view(),name='EmployeeUpdate'),
    path('CompanyDelete/<int:pk>/',views.CompanyDelete.as_view(),name='CompanyDelete'),
    path('EmployeeDelete/<int:pk>/',views.EmployeeDelete.as_view(),name='EmployeeDelete'),

]