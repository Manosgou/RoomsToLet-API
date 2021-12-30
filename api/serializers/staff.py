from rest_framework import serializers
from api.models import Requests


class RequestsSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ('id', 'house', 'description', 'status')
