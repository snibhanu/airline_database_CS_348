import uuid
from django.db import models

# Create your models here.
class PassList(models.Model):
    pass_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    ph_nbr = models.CharField(max_length=200)
    email = models.CharField(max_length =200)

    def __str__(self):
        return self.name