from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()
    role = serializers.CharField()

class RoomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    category = serializers.CharField()
    price = serializers.FloatField()

class BookingSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    room_id = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    status = serializers.CharField()

class PaymentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    booking_id = serializers.IntegerField()
    amount = serializers.FloatField()
    status = serializers.CharField()
