import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from app.models import User, Room, Category, Booking
from datetime import date

@pytest.mark.django_db
def test_get_rooms_list():
    client = APIClient()
    category = Category.objects.create(name="Эконом", description="Доступный вариант")
    Room.objects.create(category=category, price=1000, capacity=2, description="Простой номер", status="available")

    url = reverse("rooms_list")
    response = client.get(url)

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["status"] == "available"


@pytest.mark.django_db
def test_create_booking():
    client = APIClient()
    user = User.objects.create(email="user@example.com", username="booking_user")
    category = Category.objects.create(name="Люкс", description="Просторный номер")
    room = Room.objects.create(category=category, price=4500, capacity=2, description="С видом на море", status="available")

    url = reverse("bookings_list")
    data = {
        "user": user.id,
        "room": room.id,
        "check_in": str(date.today()),
        "check_out": str(date.today()),
        "status": "pending"
    }
    response = client.post(url, data, format="json")

    assert response.status_code == 201
    assert Booking.objects.count() == 1
    assert response.data["status"] == "pending"


@pytest.mark.django_db
def test_update_booking():
    client = APIClient()
    user = User.objects.create(email="user@example.com", username="update_user")
    category = Category.objects.create(name="Стандарт", description="Удобный номер")
    room = Room.objects.create(category=category, price=2500, capacity=2, description="С телевизором", status="available")
    booking = Booking.objects.create(user=user, room=room, check_in=date.today(), check_out=date.today(), status="pending")

    url = reverse("booking_detail", args=[booking.id])
    response = client.put(url, {"status": "confirmed"}, format="json")

    assert response.status_code == 200
    booking.refresh_from_db()
    assert booking.status == "confirmed"


@pytest.mark.django_db
def test_delete_booking():
    client = APIClient()
    user = User.objects.create(email="user@example.com", username="delete_user")
    category = Category.objects.create(name="Делюкс", description="Элитный номер")
    room = Room.objects.create(category=category, price=6000, capacity=2, description="С панорамным видом", status="available")
    booking = Booking.objects.create(user=user, room=room, check_in=date.today(), check_out=date.today(), status="pending")

    url = reverse("booking_detail", args=[booking.id])
    response = client.delete(url)

    assert response.status_code == 204
    assert Booking.objects.count() == 0


@pytest.mark.django_db
def test_booking_create_invalid():
    client = APIClient()
    url = reverse("bookings_list")
    response = client.post(url, {})
    assert response.status_code == 400


@pytest.mark.django_db
def test_booking_not_found():
    client = APIClient()
    url = reverse("booking_detail", args=[999])
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_booking_update_and_delete():
    client = APIClient()
    user = User.objects.create_user(email="test@example.com", username="tester", password="123")
    category = Category.objects.create(name="Тестовый", description="Описание категории")
    room = Room.objects.create(category=category, price=2000, capacity=2, description="Номер для теста", status="available")
    booking = Booking.objects.create(user=user, room=room, check_in="2025-09-01", check_out="2025-09-03", status="pending")

    url = reverse("booking_detail", args=[booking.id])

    response = client.put(url, {"status": "confirmed"}, format="json")
    assert response.status_code == 200
    assert response.data["status"] == "confirmed"

    response = client.delete(url)
    assert response.status_code == 204
