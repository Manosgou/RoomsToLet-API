from rest_framework import authentication
from rest_framework import exceptions
from api.models import Booking


class ClientAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):

        booking_code = request.META.get('HTTP_X_BOOKING_CODE')
        if not booking_code:
            return None

        try:
            booking = Booking.objects.get(id=booking_code)
        except Booking.DoesNotExist:
            raise exceptions.AuthenticationFailed('No booking found')
        return (booking, None)
