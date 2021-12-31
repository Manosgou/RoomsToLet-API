from django.urls import path
from api.views.client import get_available_houses, get_house, get_booking, book_house, check_booking, make_requests, stop_accommodation

urlpatterns = [
    path('get/available-houses', get_available_houses),
    path('get/house/<int:id>', get_house),
    path('book/house', book_house),
    path('check/booking/<str:id>', check_booking),
    path('get/booking/<str:id>', get_booking),
    path('make/requests', make_requests),
    path('stop/accommodation/<str:id>', stop_accommodation)
]
