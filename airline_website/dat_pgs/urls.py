from turtle import home
from django.urls import path
from . import views

from .views import BookingCreateView, BookingListView, EmployeesListView, EmployeesCreateView, AirlineListView, AirlineCreateView, FlightCreateView, FlightListView, HomePageView, PassCreateView, PassListView, PaymentCreateView, PaymentListView, PreferencesCreateView, PreferencesListView, detail_view_payment
#path("", homePageView, name="home")
urlpatterns = [
        path("passengers/", PassListView.as_view(), name= 'passengers'),
        path("add_passengers/", PassCreateView.as_view(), name='add_passengers'),
        path("employees/", EmployeesListView.as_view(), name='employees'),
        path("add_employee/", EmployeesCreateView.as_view(), name='add_employee'),
        path("airlines/", AirlineListView.as_view(), name= 'airlines'),
        path("add_airline/", AirlineCreateView.as_view(), name='add_airline'),
        path("payment/", PaymentListView.as_view(), name='payment'),
        path("add_payment/", PaymentCreateView.as_view(), name= 'add_payment'),
        path("add_homepage/", HomePageView.as_view(), name= "home_page_view"),
        path('<pass_id>', detail_view_payment, name='add_indiv_payment'),
        path("booking/", BookingListView.as_view(), name='booking'),
        path("add_booking/", BookingCreateView.as_view(), name = 'add_booking'),
        path("preferences/", PreferencesListView.as_view(), name= 'preferences'),
        path("add_preferences/", PreferencesCreateView.as_view(), name='add_preferences'),
        path("flights/", FlightListView.as_view(), name='flights'),
        path("add_flights/", FlightCreateView.as_view(), name='add_flights')
]