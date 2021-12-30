from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from api.serializers.general import UserSigninSerializer
from django.contrib.auth import authenticate


@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    signin_serializer = UserSigninSerializer(data=data)
    if not signin_serializer.is_valid():
        return Response(signin_serializer.errors, status=HTTP_400_BAD_REQUEST)

    user = authenticate(
        username=signin_serializer.data['username'],
        password=signin_serializer.data['password']
    )
    if not user:
        return Response({'detail': 'Invalid Credentials or activate account'}, status=HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        'token': token.key
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout(request):
    print(request.user.auth_token)
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)
