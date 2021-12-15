from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import HouseSerializer
from api.models import House


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
