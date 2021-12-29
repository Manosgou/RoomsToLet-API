from django.urls import path
from api.views.general import login, logout
from api.views.general import get_available_houses, get_house


urlpatterns = [
    path('login', login),
    path('logout', logout),
    path('houses', get_available_houses),
    path('house/<int:id>', get_house),
]
