from django.db import models
from django.contrib.auth.models import User
from main.models import Hotel
from datetime import date

# Create your models here.
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reserved_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    schedule = models.DateField()
    paid = models.BooleanField(default=False)
    date_paid = models.DateTimeField(auto_now_add=True, null=True)
    checkout = models.BooleanField(default=False)
