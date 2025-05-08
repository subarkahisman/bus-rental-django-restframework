from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bus(models.Model):
    bus_name = models.CharField(max_length=1000)
    number = models.CharField(max_length=20, unique=True)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    features = models.TextField()
    start_time = models.TimeField()
    reach_time = models.TimeField()
    no_of_seats = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.bus_name} {self.number} {self.origin} {self.destination}"

class Seat(models.Model):
    bus = models.ForeignKey('Bus', on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.bus} {self.seat_number}"
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    