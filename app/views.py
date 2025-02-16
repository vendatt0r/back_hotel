from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from .serializers import UserSerializer, RoomSerializer, BookingSerializer, PaymentSerializer, ReviewSerializer, CategorySerializer

class UserView(APIView):
    @extend_schema(
        summary="Получение списка пользователей",
        description="Возвращает список всех пользователей.",
        responses={200: UserSerializer(many=True)}
    )
    def get(self, request):
        return Response([], status=status.HTTP_200_OK)


class RoomView(APIView):
    @extend_schema(
        summary="Получение списка номеров",
        description="Возвращает список всех номеров отеля.",
        responses={200: RoomSerializer(many=True)}
    )
    def get(self, request):
        return Response([], status=status.HTTP_200_OK)

class RoomDetailView(APIView):
    @extend_schema(
        summary="Получение информации о номере",
        description="Возвращает данные конкретного номера.",
        responses={200: RoomSerializer}
    )
    def get(self, request, room_id):
        return Response({"id": room_id}, status=status.HTTP_200_OK)

class CategoryView(APIView):
    @extend_schema(
        summary="Получение списка категорий номеров",
        description="Возвращает список всех категорий номеров отеля.",
        responses={200: CategorySerializer(many=True)}
    )
    def get(self, request):
        return Response([], status=status.HTTP_200_OK)

class CategoryDetailView(APIView):
    @extend_schema(
        summary="Получение информации о категории номеров",
        description="Возвращает данные конкретной категории номеров.",
        responses={200: CategorySerializer}
    )
    def get(self, request, category_id):
        return Response({"id": category_id}, status=status.HTTP_200_OK)

class BookingView(APIView):
    @extend_schema(
        summary="Получение списка бронирований",
        description="Возвращает список всех бронирований.",
        responses={200: BookingSerializer(many=True)}
    )
    def get(self, request):
        return Response([], status=status.HTTP_200_OK)

    @extend_schema(
        summary="Создание бронирования",
        description="Создает новое бронирование.",
        request=BookingSerializer,
        responses={201: BookingSerializer}
    )
    def post(self, request):
        return Response(request.data, status=status.HTTP_201_CREATED)


class BookingDetailView(APIView):
    @extend_schema(
        summary="Получение информации о бронировании",
        description="Возвращает данные конкретного бронирования.",
        responses={200: BookingSerializer}
    )
    def get(self, request, booking_id):
        return Response({"id": booking_id}, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Обновление бронирования",
        description="Обновляет информацию о бронировании.",
        request=BookingSerializer,
        responses={200: BookingSerializer}
    )
    def put(self, request, booking_id):
        return Response(request.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Удаление бронирования",
        description="Удаляет бронирование.",
        responses={204: None}
    )
    def delete(self, request, booking_id):
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentView(APIView):
    @extend_schema(
        summary="Получение списка платежей",
        description="Возвращает список всех платежей.",
        responses={200: PaymentSerializer(many=True)}
    )
    def get(self, request):
        return Response([], status=status.HTTP_200_OK)

    @extend_schema(
        summary="Создание платежа",
        description="Создает новый платеж.",
        request=PaymentSerializer,
        responses={201: PaymentSerializer}
    )
    def post(self, request):
        return Response(request.data, status=status.HTTP_201_CREATED)


class PaymentDetailView(APIView):
    @extend_schema(
        summary="Получение информации о платеже",
        description="Возвращает данные конкретного платежа.",
        responses={200: PaymentSerializer}
    )
    def get(self, request, payment_id):
        return Response({"id": payment_id}, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Обновление платежа",
        description="Обновляет информацию о платеже.",
        request=PaymentSerializer,
        responses={200: PaymentSerializer}
    )
    def put(self, request, payment_id):
        return Response(request.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Удаление платежа",
        description="Удаляет платеж.",
        responses={204: None}
    )
    def delete(self, request, payment_id):
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewView(APIView):
    @extend_schema(
        summary="Получение списка отзывов",
        description="Возвращает список всех отзывов.",
        responses={200: ReviewSerializer(many=True)}
    )
    def get(self, request):
        return Response([], status=status.HTTP_200_OK)

    @extend_schema(
        summary="Создание отзыва",
        description="Создает новый отзыв.",
        request=ReviewSerializer,
        responses={201: ReviewSerializer}
    )
    def post(self, request):
        return Response(request.data, status=status.HTTP_201_CREATED)


class ReviewDetailView(APIView):
    @extend_schema(
        summary="Получение информации об отзыве",
        description="Возвращает данные конкретного отзыва.",
        responses={200: ReviewSerializer}
    )
    def get(self, request, review_id):
        return Response({"id": review_id}, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Обновление отзыва",
        description="Обновляет информацию об отзыве.",
        request=ReviewSerializer,
        responses={200: ReviewSerializer}
    )
    def put(self, request, review_id):
        return Response(request.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Удаление отзыва",
        description="Удаляет отзыв.",
        responses={204: None}
    )
    def delete(self, request, review_id):
        return Response(status=status.HTTP_204_NO_CONTENT)
