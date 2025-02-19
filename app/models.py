from decimal import Decimal
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=20, blank=False)
    email = models.EmailField(unique=True, blank=False)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    role = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('user', 'User')], default='user')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone", "role"]

    def __str__(self):
        return f"{self.username} ({self.role})"

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

class Payment(models.Model):
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="bookings")
    create_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("paid", "Paid"),
                                                      ("failed", "Failed"), ("cancelled", "Cancelled"),
                                                      ("refunded", "Refunded")])

    def __str__(self):
        return f"Payment {self.id} - {self.status} ({self.amount} RUB)"