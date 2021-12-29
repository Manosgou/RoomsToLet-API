from django.urls import path
from api.views.admin import get_house, add_new_house, delete_house, get_staff_members, update_house, create_staff_member, get_staff_member, delete_staff_member, update_staff_member


urlpatterns = [
    path('get/house/<int:id>', get_house),
    path('add/new/house', add_new_house),
    path('delete/house/<int:id>', delete_house),
    path('update/house/<int:id>', update_house),
    path('get/staff-members', get_staff_members),
    path('get/staff-member/<int:id>', get_staff_member),
    path('create/staff-member', create_staff_member),
    path('delete/staff-member/<int:id>', delete_staff_member),
    path('update/staff-member/<int:id>', update_staff_member)
]
