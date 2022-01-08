from django.urls import path
from api.views.staff import get_requests, get_request, delete_request, update_request_status

urlpatterns = [
    path('requests', get_requests),
    path('requests/<int:id>', get_request),
    path('delete/requests/<int:id>', delete_request),
    path('update/request-status/<int:id>', update_request_status),
]
