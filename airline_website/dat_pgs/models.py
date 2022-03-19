import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class PassList(models.Model):
    pass_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    ph_nbr = models.CharField(max_length=200)
    email = models.CharField(max_length =200)

    def __str__(self):
        return self.name

class Airline(models.Model):
    airline_name = models.CharField(max_length=100, blank=False, unique=True, default=uuid.uuid4)
    type_of_airline = models.CharField(max_length=200)


    class Meta:
        ordering = ["airline_name"]

    def __str__(self):
        return self.airline_name

class Employees(models.Model):
    emp_id = models.CharField(max_length=100, blank=False, unique=True, default=uuid.uuid4)
    airline_name = models.ForeignKey(Airline, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-emp_id"]

    def __str__(self):
        return "%s %s" % (self.emp_id, self.airline_name)


