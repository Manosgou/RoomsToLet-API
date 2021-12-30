from django.urls import path
from api.views.staff import get_requests, get_request, delete_request, update_request_status

urlpatterns = [
    path('get/requests', get_requests),
    path('get/request/<int:id>', get_request),
    path('delete/request/<int:id>', delete_request),
    path('update/request-status/<int:id>', update_request_status),
]
