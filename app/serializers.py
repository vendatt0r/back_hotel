from rest_framework import serializers
from rest_framework import serializers
from .models import User, Room, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class PaymentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    booking_id = serializers.IntegerField()
    amount = serializers.FloatField()
    status = serializers.CharField()

class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    room_id = serializers.IntegerField()
    rating = serializers.IntegerField()
    comment = serializers.CharField()

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
