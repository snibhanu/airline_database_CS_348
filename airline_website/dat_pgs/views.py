#from attr import field
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Booking, FlightList, PassList, Payment, Preferences
from .models import Employees
from .models import Airline




# Create your views here.
class PassListView(ListView):
    model = PassList

class PassCreateView(CreateView):
    model = PassList
    fields = ['pass_id', 'name','address', 'ph_nbr', 'email']


class EmployeesListView(ListView):
    model = Employees

class EmployeesCreateView(CreateView):
    model = Employees
    fields = ['emp_id', 'airline_name']

class BookingListView(ListView):
    model = Booking

class BookingCreateView(CreateView):
    model =  Booking
    fields = ['confirmation_no', 'pass_id', 'flight_no', 'dep_arpt', 'arr_arpt', 'dep_date', 'arr_date']

class PaymentListView(ListView):
    model = Payment

class PaymentCreateView(CreateView):
    model = Payment
    fields = ['pass_id', 'credit_card_name', 'card_no', 'sec_code' , 'exp_date']

class PreferencesListView(ListView):
    model = Preferences

class PreferencesCreateView(CreateView):
    model = Preferences
    fields = ['pass_id', 'seat_no', 'seat_type', 'meal_type']

class FlightListView(ListView):
    model = FlightList

class FlightCreateView(CreateView):
    model = FlightList
    fields = ['flight_id', 'flight_no', 'airline_name', 'seats_left', 'dep_arpt', 'arr_arpt', 'dep_date', 'arr_date']

class AirlineListView(ListView):
    model = Airline

class AirlineCreateView(CreateView):
    model = Airline
    fields = ['airline_name', 'type_of_airline']