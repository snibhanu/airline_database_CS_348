#from attr import field
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.base import View
from django.db import connection
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

#function to view your payment info
def detail_view_payment(self,pass_id):
    print(f'Name {pass_id}')
    http_itm = []
    with connection.cursor() as cursor:
        cursor.execute('''SELECT name,pass_id, credit_card_name, card_no, sec_code 
        FROM (SELECT * FROM dat_pgs_payment a, dat_pgs_passlist b WHERE b.id = a.id);''')
        row = cursor.fetchall()
        for itm in row:
            if itm[1] == pass_id:
                http_itm.append(itm)
    print(row)
    return HttpResponse(http_itm)


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