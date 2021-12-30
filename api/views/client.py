from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Booking, House
from api.serializers.client import HouseSerializer, BookingSerializer
from api.models import House
from rest_framework.parsers import JSONParser
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
)


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
        booking_id = serializer.data.get('id')
        return Response({"book_code": booking_id}, status=HTTP_201_CREATED)
    return Response(status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_booking(request, id):
    try:
        booking = Booking.objects.get(id=id)
        serializer = BookingSerializer(booking)
    except Booking.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    return Response(serializer.data, status=HTTP_200_OK)
