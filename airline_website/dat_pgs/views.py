#from attr import field
import http
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

class HomePageView(View):
    def get(self, request):      
        return render(request, "dat_pgs/home_page.html")

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
    def get_form(self):
        form = super(BookingCreateView, self).get_form()

        print(self.request.POST.get("flight_no"))

        if self.request.POST.get("flight_no") != None:


            flight_no = self.request.POST.get("flight_no")
            # print(type(form['flight_no']))
            # print(flight_no)
            for i in form['flight_no']:
                print(i.data['value'])
                if str(i.data['value']) == flight_no:
                # print('hi')
                    flight_no = str(i.data['label'])
            command = "UPDATE dat_pgs_flightlist SET seats_left = seats_left - 1 WHERE flight_id = "
            command += str(flight_no)
            command += ";"
            print(command)
            with connection.cursor() as cursor:
                cursor.execute(command)
                connection.commit()

        return form

class PaymentListView(ListView):
    model = Payment

class PaymentCreateView(CreateView):
    model = Payment
    fields = ['pass_id', 'credit_card_name', 'card_no', 'sec_code' , 'exp_date']

#function to group by airlines
def group_by_airline(company):
    print(f'Company{company}')
    http_itm = []
    with connection.cursor() as cursor:
        cursor.execute('''SELECT * FROM dat_pgs_airline a, dat_pgs_flightlist b 
        WHERE b.airline_name_id =  a.id;''')
        row = cursor.fetchall()
        for itm in row:
            print(itm)
            if itm[1] == company:
                print('Entered if')
                http_itm.append(itm)
    print(http_itm)
    if (len(http_itm) > 0):
        return HttpResponse(http_itm)
    else:
        return HttpResponse('No flights exist for this airline as of yet')

#function to filter flights by destination
def group_by_destination(destination):
    print(f'Company{destination}')
    http_itm = []
    with connection.cursor() as cursor:
        cursor.execute('''SELECT * FROM dat_pgs_airline a, dat_pgs_flightlist b 
        WHERE b.airline_name_id =  a.id;''')
        row = cursor.fetchall()
        for itm in row:
            print(itm)
            if destination in itm[-1]:
                print('Entered if')
                http_itm.append(itm)
    print(http_itm)
    if (len(http_itm) > 0):
        return HttpResponse(http_itm)
    else:
        return HttpResponse('This city is not a current destination')

#function to filter flights by departure airport
def group_by_departure(departure):
    print(f'Company{departure}')
    http_itm = []
    with connection.cursor() as cursor:
        cursor.execute('''SELECT * FROM dat_pgs_airline a, dat_pgs_flightlist b 
        WHERE b.airline_name_id =  a.id;''')
        row = cursor.fetchall()
        for itm in row:
            print(itm)
            if departure in itm[7]:
                print('Entered if')
                http_itm.append(itm)
    print(http_itm)
    if (len(http_itm) > 0):
        return HttpResponse(http_itm)
    else:
        return HttpResponse('This city is not currently a departure city')
    
#function to view added payments
def detail_view_payment(self,pass_id):
    with connection.cursor() as cursor_0:
        cursor_0.execute(''' 
            SELECT * FROM dat_pgs_airline;
        ''')
        row_0 = cursor_0.fetchall()
        for itm in row_0:
            if pass_id == itm[1]:
                return group_by_airline(pass_id)
    if 'arr' in pass_id:
        pass_id = pass_id[3:]
        with connection.cursor() as cursor_1:
            cursor_1.execute('''
                SELECT arr_arpt FROM 
                (SELECT * FROM dat_pgs_airline a, dat_pgs_flightlist b 
            WHERE b.airline_name_id =  a.id)
            '''
            )
            row_1 = cursor_1.fetchall()
            print(row_1)
            for itm in row_1:
                if pass_id in itm[-1]:
                    return group_by_destination(pass_id)
    if 'dep' in pass_id:
        pass_id = pass_id[3:]
        with connection.cursor() as cursor_2:
            cursor_2.execute('''
                SELECT dep_arpt FROM 
                (SELECT * FROM dat_pgs_airline a, dat_pgs_flightlist b 
            WHERE b.airline_name_id =  a.id)
            '''
            )
            row_2 = cursor_2.fetchall()
            print(row_2)
            for itm in row_2:
                if pass_id in itm[-1]:
                    return group_by_departure(pass_id)
                
    http_itm_1 = []
    with connection.cursor() as cursor:
        cursor.execute('''SELECT name,pass_id, credit_card_name, card_no, sec_code 
        FROM (SELECT * FROM dat_pgs_payment a, dat_pgs_passlist b WHERE b.id = a.id);''')
        row = cursor.fetchall()
        for itm in row:
            if itm[1] == pass_id:
                http_itm_1.append(itm)
    print(row)
    if (len(http_itm_1) > 0):
        return HttpResponse(http_itm_1)
    return HttpResponse('Item cannot be found please try again')

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