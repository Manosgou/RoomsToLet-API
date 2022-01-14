from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT
)
from api.models import Request, Request
from api.serializers.staff import RequestsSeriliazer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_requests(request):
    requests = Request.objects.filter(status='PE')
    serializer = RequestsSeriliazer(requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_request(request, id):
    try:
        req = Request.objects.get(id=id)
        serializer = RequestsSeriliazer(req)
    except:
        return Response(status=HTTP_404_NOT_FOUND)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_request(request, id):
    try:
        req = Request.objects.get(id=id)
        req.delete()
    except Request.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    return Response(status=HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_request_status(request, id):
    try:
        req = Request.objects.get(id=id)
        data = JSONParser().parse(request)
        serializer = RequestsSeriliazer(req, data=data)
        if serializer.is_valid():
            serializer.save()
    except Request.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    return Response(status=HTTP_204_NO_CONTENT)
