from django.urls import path
from api.views.general import login


urlpatterns = [
    path('login', login)
]
