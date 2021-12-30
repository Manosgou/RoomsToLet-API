from django.urls import path
from api.views.general import login, logout


urlpatterns = [
    path('login', login),
    path('logout', logout)
]
