from turtle import home
from django.urls import path
from . import views

from .views import BookingCreateView, BookingListView, EmployeesListView, EmployeesCreateView, AirlineListView, AirlineCreateView, FlightCreateView, FlightListView, PaymentCreateView, PaymentListView, PreferencesCreateView, PreferencesListView
#path("", homePageView, name="home")
urlpatterns = [
        path("passenger/<int:id>", views.index, name="index"),
        path("employees/", EmployeesListView.as_view()),
        path("add_employee/", EmployeesCreateView.as_view()),
        path("airlines/", AirlineListView.as_view()),
        path("add_airline/", AirlineCreateView.as_view()),
        path("payment/", PaymentListView.as_view()),
        path("add_payment/", PaymentCreateView.as_view()),
        path("booking/", BookingListView.as_view()),
        path("add_booking/", BookingCreateView.as_view()),
        path("preferences/", PreferencesListView.as_view()),
        path("add_preferences/", PreferencesCreateView.as_view()),
        path("flights/", FlightListView.as_view()),
        path("add_flights/", FlightCreateView.as_view())
]