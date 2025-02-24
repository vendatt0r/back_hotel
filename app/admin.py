from django.contrib import admin
from .models import User, Room, Booking, Payment, Category, Review

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Category)
admin.site.register(Review)
