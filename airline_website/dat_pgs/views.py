from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import PassList
from .models import Employees
from .models import Airline


def homePageView(request):
    return HttpResponse("Hello, World!")
def index(response, id):
    ls = PassList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name,ls.address))
# Create your views here.


class EmployeesListView(ListView):

    model = Employees

class EmployeesCreateView(CreateView):
    model = Employees
    fields = ['emp_id', 'airline_name']


class AirlineListView(ListView):

    model = Airline

class AirlineCreateView(CreateView):
    model = Airline
    fields = ['airline_name', 'type_of_airline']