from rest_framework import serializers
from api.models import Request


class RequestsSeriliazer(serializers.ModelSerializer):
    house = serializers.StringRelatedField()

    class Meta:
        model = Request
        fields = ('id', 'house', 'description', 'status')
        extra_kwargs = {
            'id': {'read_only': True},
            'house': {'read_only': True},
            'description': {'read_only': True},
        }
