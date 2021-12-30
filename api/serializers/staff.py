from rest_framework import serializers
from api.models import Requests


class RequestsSeriliazer(serializers.ModelSerializer):
    house = serializers.StringRelatedField()

    class Meta:
        model = Requests
        fields = ('id', 'house', 'description', 'status')
