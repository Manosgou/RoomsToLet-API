from rest_framework import serializers
from api.models import Booking, House, HouseImage, Request


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
        fields = ('id', 'house', 'lastname', 'firstname',
                  'email', 'phone_number', 'duration')

    def create(self, validated_data):
        booking = super().create(validated_data)
        house = House.objects.get(id=booking.house.id)
        house.is_available = False
        house.save()
        return booking


class DetailedBookingSerializer(serializers.Serializer):
    id = serializers.CharField()
    house = HouseSerializer()
    lastname = serializers.CharField()
    firstname = serializers.CharField()
    duration = serializers.IntegerField()
    total_price = serializers.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        model = Booking
        fields = ('id', 'house', 'lastname',
                  'firstname', 'duration', 'total_price')

    def to_representation(self, instance):
        detail_booking = super().to_representation(instance)
        house = detail_booking.get('house')
        house.pop('images')
        return detail_booking


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('house', 'description')
