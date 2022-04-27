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

    class Meta:
        ordering = ["pass_id"]

    def __str__(self):
        return self.name


class Airline(models.Model):
    airline_name = models.CharField(max_length=100, blank=False, unique=True, default=uuid.uuid4)
    type_of_airline = models.CharField(max_length=200)

    class Meta:
        ordering = ["airline_name"]

    def __str__(self):
        return self.airline_name

class FlightList(models.Model):
    flight_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    flight_no = models.CharField(max_length=200)
    airline_name = models.ForeignKey(Airline, on_delete=models.CASCADE)
    seats_left = models.IntegerField(default=0)
    dep_arpt = models.CharField(max_length=200)
    arr_arpt = models.DateTimeField()
    dep_date = models.DateTimeField()
    arr_date = models.DateTimeField()

    class Meta:
        ordering = ["flight_id"]

    def __str__(self):
        return self.flight_id

class Employees(models.Model):
    emp_id = models.CharField(max_length=100, blank=False, unique=True, default=uuid.uuid4)
    airline_name = models.ForeignKey(Airline, on_delete=models.CASCADE)
    flight_no = models.ForeignKey(FlightList, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-emp_id"]

    def __str__(self):
        return "%s %s" % (self.emp_id, self.airline_name)

class Booking(models.Model):
    confirmation_no = models.CharField(max_length=100, blank=False, unique=True, default=uuid.uuid4)
    pass_id = models.ForeignKey(PassList, on_delete=models.CASCADE)
    pass_id  = models.ForeignKey(FlightList, on_delete=models.CASCADE)
    dep_arpt = models.CharField(max_length=200)
    arr_arpt = models.DateTimeField()
    dep_date = models.DateTimeField()
    arr_date = models.DateTimeField()

    class Meta:
         ordering = ["confirmation_no"]
    
    def __str__(self):
        return self.confirmation_no

class Payment(models.Model):
    pass_id = models.ForeignKey(PassList, on_delete=models.CASCADE)
    credit_card_name = models.CharField(max_length=200)
    card_no = models.CharField(max_length=200)
    sec_code = models.CharField(max_length=3)
    exp_date = models.DateTimeField()
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["pass_id", "credit_card_name"],
                name="payment_id"
            )
        ]

class Preferences(models.Model):
    pass_id = models.ForeignKey(PassList, on_delete=models.CASCADE)
    seat_no = models.IntegerField(default=0)
    seat_type = models.CharField(max_length=200)
    meal_type = models.CharField(max_length=200)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["pass_id", "seat_no"],
                name="pref_id"
            )
        ]
    
    




