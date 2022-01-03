from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.models import Booking, House
from api.serializers.client import HouseSerializer, DetailedBookingSerializer, BookingSerializer, RequestSerializer
from api.models import House
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
)
from django.core.mail import send_mail
from django.conf import settings


@api_view(['GET'])
def get_available_houses(request):
    houses = House.objects.filter(is_available=True)
    serialized_houses = HouseSerializer(houses, many=True)
    return Response(serialized_houses.data)


@api_view(['GET'])
def get_house(request, id):
    house = House.objects.get(id=id)
    serialized_house = HouseSerializer(house)
    return Response(serialized_house.data)


@api_view(['POST'])
def book_house(request):
    data = JSONParser().parse(request)
    serializer = BookingSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        booking_code = serializer.data.get('id')
        lastname = serializer.data.get('lastname')
        firstname = serializer.data.get('firstname')
        email = serializer.data.get('email')
        send_mail(
            subject='Your booking code',
            message=f'Dear Sir / Madam {lastname} {firstname},\n \n \n Thank you for choosing us. Your booking code is {booking_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
        return Response({"book_code": booking_code}, status=HTTP_201_CREATED)
    print(serializer.errors)
    return Response(status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def check_booking(request, id):
    try:
        Booking.objects.get(id=id)
    except Booking.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    return Response(status=HTTP_200_OK)


@api_view(['GET'])
def get_booking(request, id):
    try:
        booking = Booking.objects.get(id=id)
        serializer = DetailedBookingSerializer(booking)
    except Booking.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
def make_requests(request):
    data = JSONParser().parse(request)
    serializer = RequestSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=HTTP_201_CREATED)
    return Response(status=HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def stop_accommodation(request, id):
    try:
        booking = Booking.objects.get(id=id)
        booking.delete()
    except Booking.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    return Response(status=HTTP_204_NO_CONTENT)
