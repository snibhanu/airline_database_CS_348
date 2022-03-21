from turtle import home
from django.urls import path
from . import views

from .views import EmployeesListView, EmployeesCreateView, AirlineListView, AirlineCreateView
#path("", homePageView, name="home")
urlpatterns = [
        path("passenger/<int:id>", views.index, name="index"),
        path("employees/", EmployeesListView.as_view()),
        path("add_employee/", EmployeesCreateView.as_view()),
        path("airlines/", AirlineListView.as_view()),
        path("add_airline/", AirlineCreateView.as_view()),
]