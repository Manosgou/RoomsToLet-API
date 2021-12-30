from django.urls import path
from api.views.client import get_available_houses, get_house, get_booking, book_house

urlpatterns = [
    path('houses', get_available_houses),
    path('house/<int:id>', get_house),
    path('book/house', book_house),
    path('get/booking/<str:id>', get_booking)

]
