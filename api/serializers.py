from rest_framework import serializers
from api.models import House


class UserSigninSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'
