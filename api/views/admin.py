from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from api.models import Booking, House
from django.contrib.auth.models import User
from api.serializers.admin import CreateUpdateHouseSerializer, GetHouseSerializer, HouseSerializer, StaffMembersSerializer, BookingSerializer, UpdateBookingSerializer
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def houses(request):
    if request.method == 'GET':
        houses = House.objects.all()
        serializer = GetHouseSerializer(houses, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CreateUpdateHouseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_201_CREATED)
    return Response(status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_available_houses(request):
    available_houses = House.objects.filter(is_available=True)
    serializer = HouseSerializer(available_houses, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_house(request, id):
    house = House.objects.get(id=id)
    serializer = GetHouseSerializer(house)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_house(request, id):
    try:
        house = House.objects.get(id=id)
        house.delete()
    except House.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    return Response(status=HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_house(request, id):
    try:
        house = House.objects.get(id=id)
        data = JSONParser().parse(request)
        serialzier = CreateUpdateHouseSerializer(
            house, data=data, partial=True)
        if serialzier.is_valid():
            serialzier.save()
    except House.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    return Response(status=HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def staff_members(request):
    if request.method == 'GET':
        staff_members = User.objects.filter(is_staff=True)
        seriliazer = StaffMembersSerializer(staff_members, many=True)
        return Response(seriliazer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StaffMembersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_201_CREATED)
    return Response(status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_staff_member(request, id):
    try:
        staff_member = User.objects.get(id=id)
        serializer = StaffMembersSerializer(staff_member)
    except User.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_staff_member(request, id):
    try:
        staff_member = User.objects.get(id=id)
        staff_member.delete()
    except User.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    return Response(status=HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_staff_member(request, id):
    try:
        staff_member = User.objects.get(id=id)
        data = JSONParser().parse(request)
        serialzier = StaffMembersSerializer(
            staff_member, data=data, partial=True)
        if serialzier.is_valid():
            serialzier.save()
    except House.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    return Response(status=HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bookings(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_booking(request, id):
    try:
        booking = Booking.objects.get(id=id)
        serializer = BookingSerializer(booking)
    except Booking.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_booking(request, id):
    try:
        booking = Booking.objects.get(id=id)
        booking.delete()
    except Booking.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    return Response(status=HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_booking(request, id):
    try:
        booking = Booking.objects.get(id=id)
        data = JSONParser().parse(request)
        house_id = data.get('house')
        if house_id:
            data['house'] = int(house_id)
        print(data)
        serializer = UpdateBookingSerializer(
            booking, data=data)
        if serializer.is_valid():
            serializer.save()
        print(serializer.errors)
    except Booking.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    return Response(status=HTTP_204_NO_CONTENT)
