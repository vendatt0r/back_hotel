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

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    def get_room_count(self):
        return self.rooms.count()
    def has_available_rooms(self):
        return self.rooms.filter(status="available").exists()

class Room(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="rooms")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[("available", "Available"), ("booked", "Booked")])

    def __str__(self):
        return f"Room {self.id} - {self.status}"
    def is_available(self):
        return self.status == "available"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("canceled", "Canceled")])

    def __str__(self):
        return f"Booking {self.id} ({self.status})"
    
    def cancel_booking(self):
        self.status = "canceled"
        self.save()

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="payments")
    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("paid", "Paid"),
                                                      ("failed", "Failed"), ("cancelled", "Cancelled"),
                                                      ("refunded", "Refunded")])
    
    def __str__(self):
        return f"Payment {self.id} - {self.status} ({self.amount} RUB)"
    
    def mark_as_paid(self):
        self.status = "paid"
        self.paid_at = timezone.now()
        self.save()

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.id} - {self.rating} stars"
    
    def is_positive(self):
        return self.rating > 3
    
    def short_comment(self):
        return self.comment[:50] + "..." if len(self.comment) > 50 else self.comment
    
    def get_reviews_in_period(cls, start_date, end_date):
        return cls.objects.filter(created_at__range=[start_date, end_date])

