from django.contrib import admin
from .models import PassList
from .models import Airline
from .models import Employees

# Register your models here.
admin.site.register(PassList)
admin.site.register(Airline)
admin.site.register(Employees)