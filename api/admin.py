from django.contrib import admin
from api.models import *
# Register your models here.


class HouseImageAdmin(admin.StackedInline):
    model = HouseImage


admin.register(HouseImageAdmin)


def make_house_available(modeladmin, request, queryset):
    queryset.update(is_available=True)


def make_house_unavailable(modeladmin, request, queryset):
    queryset.update(is_available=False)


class HouseAdmin(admin.ModelAdmin):
    inlines = (HouseImageAdmin,)
    list_display = ('title', 'price', 'is_available',)
    readonly_fields = ('slug',)
    actions = [make_house_available, make_house_unavailable]


admin.site.register(House, HouseAdmin)


admin.site.register(Request)
admin.site.register(Booking)
