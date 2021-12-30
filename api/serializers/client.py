from rest_framework import serializers
from api.models import Booking, House, HouseImage


class HouseImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImage
        fields = ('image',)


class HouseSerializer(serializers.ModelSerializer):
    images = HouseImagesSerializer(source='houseimage_set', many=True)

    class Meta:
        model = House
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'house', 'lastname', 'firstname', 'duration')
