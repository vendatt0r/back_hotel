from django.contrib import admin
from .models import User, Room, Booking, Payment

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Payment)
