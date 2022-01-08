from django.urls import path
from api.views.admin import get_available_houses, houses, get_house, delete_house, staff_members, update_house, get_staff_member, delete_staff_member, update_staff_member, bookings, get_booking, delete_booking, update_booking


urlpatterns = [
    path('houses', houses),
    path('available-houses', get_available_houses),
    path('houses/<int:id>', get_house),
    path('delete/houses/<int:id>', delete_house),
    path('update/houses/<int:id>', update_house),
    path('staff-members', staff_members),
    path('staff-members/<int:id>', get_staff_member),
    path('delete/staff-members/<int:id>', delete_staff_member),
    path('update/staff-members/<int:id>', update_staff_member),
    path('bookings', bookings),
    path('bookings/<str:id>', get_booking),
    path('update/bookings/<str:id>', update_booking),
    path('delete/bookings/<int:id>', delete_booking),

]
