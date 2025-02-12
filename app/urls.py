from django.urls import path
from .views import UserView, RoomView, BookingView, PaymentView, BookingDetailView, PaymentDetailView

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('rooms/', RoomView.as_view(), name='rooms'),
    path('bookings/', BookingView.as_view(), name='bookings_list'),
    path('bookings/<int:id>/', BookingDetailView.as_view(), name='booking_detail'),
    path('payments/', PaymentView.as_view(), name='payments_list'),
    path('payments/<int:id>/', PaymentDetailView.as_view(), name='payment_detail'),
]
