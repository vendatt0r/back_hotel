from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Room(models.Model):
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="rooms")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[("available", "Available"), ("booked", "Booked")])

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("canceled", "Canceled")])

    def __str__(self):
        return f"Booking {self.id} ({self.status})"




