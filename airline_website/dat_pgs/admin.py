from django.contrib import admin
from .models import Booking, FlightList, PassList, Payment
from .models import Airline
from .models import Employees

# Register your models here.
admin.site.register(PassList)
admin.site.register(Airline)
admin.site.register(Employees)
admin.site.register(FlightList)
admin.site.register(Booking)
admin.site.register(Payment)
