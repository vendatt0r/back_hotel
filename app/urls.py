from django.urls import path
from .views import (UserView, RoomView, BookingView, PaymentView,
                    BookingDetailView, PaymentDetailView, ReviewDetailView,
                    ReviewView, CategoryView, CategoryDetailView, RoomDetailView)

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('rooms/', RoomView.as_view(), name='rooms_list'),
    path('rooms/<int:id>/', RoomDetailView.as_view(), name='room_detail'),
    path('categories/', CategoryView.as_view(), name='categories_list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category_detail'),
    path('bookings/', BookingView.as_view(), name='bookings_list'),
    path('bookings/<int:id>/', BookingDetailView.as_view(), name='booking_detail'),
    path('payments/', PaymentView.as_view(), name='payments_list'),
    path('payments/<int:id>/', PaymentDetailView.as_view(), name='payment_detail'),

    path('reviews/', ReviewView.as_view(), name='reviews_list'),
    path('reviews/<int:id>/', ReviewDetailView.as_view(), name='review_detail'),
]
