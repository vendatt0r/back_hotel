import pytest
from app.models import User, Room, Category, Review
from django.utils import timezone
from app.models import Booking, Payment

@pytest.mark.django_db
def test_review_is_positive():
    user = User.objects.create(email="petrov@example.com", username="ivan")
    category = Category.objects.create(name="Люкс", description="Номер люкс")
    room = Room.objects.create(category=category, price=5000, capacity=2, description="С балконом", status="available")
    review = Review.objects.create(user=user, room=room, rating=5, comment="Очень понравилось!")

    assert review.is_positive() is True


@pytest.mark.django_db
def test_review_short_comment():
    user = User.objects.create(email="smirnova@example.com", username="olga")
    category = Category.objects.create(name="Эконом", description="Бюджетный вариант")
    room = Room.objects.create(category=category, price=1200, capacity=2, description="Простой номер", status="available")
    long_comment = "Отличное соотношение цены и качества" * 5
    review = Review.objects.create(user=user, room=room, rating=4, comment=long_comment)

    assert review.short_comment().endswith("...")
    assert len(review.short_comment()) < len(review.comment)


@pytest.mark.django_db
def test_category_has_available_rooms():
    category = Category.objects.create(name="Семейный", description="Подходит для отдыха с детьми")
    Room.objects.create(category=category, price=3500, capacity=4, description="Просторный номер", status="available")

    assert category.has_available_rooms() is True


@pytest.mark.django_db
def test_user_str():
    user = User.objects.create_user(email="ivanova@example.com", username="maria", password="123", role="user")
    assert str(user) == "maria (user)"


@pytest.mark.django_db
def test_category_methods():
    category = Category.objects.create(name="Бизнес", description="Для командировок")
    Room.objects.create(category=category, price=2500, capacity=2, description="Стандартный номер", status="available")
    Room.objects.create(category=category, price=2700, capacity=2, description="С рабочим местом", status="booked")

    assert str(category) == "Бизнес"
    assert category.get_room_count() == 2
    assert category.has_available_rooms() is True


@pytest.mark.django_db
def test_room_str():
    category = Category.objects.create(name="Стандарт", description="Базовый номер")
    room = Room.objects.create(category=category, price=1800, capacity=2, description="Номер без балкона", status="available")
    assert str(room) == f"Room {room.id} - available"


@pytest.mark.django_db
def test_booking_str():
    user = User.objects.create_user(email="sidorov@example.com", username="pavel", password="123")
    category = Category.objects.create(name="Одноместный", description="Для одного гостя")
    room = Room.objects.create(category=category, price=1500, capacity=1, description="Уютный номер", status="available")
    booking = Booking.objects.create(user=user, room=room, check_in="2025-09-01", check_out="2025-09-05", status="pending")
    assert str(booking) == f"Booking {booking.id} (pending)"


@pytest.mark.django_db
def test_payment_str():
    user = User.objects.create_user(email="kuznetsov@example.com", username="sergey", password="123")
    category = Category.objects.create(name="Апартаменты", description="Большие номера")
    room = Room.objects.create(category=category, price=7000, capacity=3, description="С кухней", status="available")
    booking = Booking.objects.create(user=user, room=room, check_in="2025-09-10", check_out="2025-09-15", status="confirmed")
    payment = Payment.objects.create(booking=booking, amount=20000, status="paid")

    assert "Payment" in str(payment)
    assert "paid" in str(payment)
    assert payment.amount == 20000


@pytest.mark.django_db
def test_review_methods():
    user = User.objects.create_user(email="volkova@example.com", username="anna", password="123")
    category = Category.objects.create(name="Хостел", description="Общежитие")
    room = Room.objects.create(category=category, price=600, capacity=6, description="Койко место", status="available")
    review = Review.objects.create(user=user, room=room, rating=5, comment="Замечательный персонал")

    assert str(review) == f"Review {review.id} - 5 stars"
    assert review.is_positive() is True
    assert review.short_comment() == "Замечательный персонал"

    long_comment = "Очень длинный отзыв " * 10
    review_long = Review.objects.create(user=user, room=room, rating=2, comment=long_comment)
    assert review_long.short_comment().endswith("...")

    start = timezone.now() - timezone.timedelta(days=1)
    end = timezone.now() + timezone.timedelta(days=1)
    reviews_in_period = Review.get_reviews_in_period(start, end)
    assert review in reviews_in_period
