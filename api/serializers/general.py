from rest_framework import serializers
from api.models import House, HouseImage


class UserSigninSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class HouseImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImage
        fields = ('image',)


class HouseSerializer(serializers.ModelSerializer):
    images = HouseImagesSerializer(source='houseimage_set', many=True)

    class Meta:
        model = House
        fields = '__all__'
