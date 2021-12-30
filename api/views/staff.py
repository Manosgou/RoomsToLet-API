from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
from api.models import Requests
from api.serializers.staff import RequestsSeriliazer


@api_view(['GET'])
def get_requests(request):
    requests = Requests.objects.all()
    serializer = RequestsSeriliazer(requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_request(request, id):
    request = Requests.objects.get(id=id)
    serializer = RequestsSeriliazer(request)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_request(request, id):
    pass


@api_view(['PUT'])
def update_request_status(request, id):
    pass
