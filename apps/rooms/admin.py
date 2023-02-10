from django.contrib import admin
from apps.rooms.models import Room, Currency, Reservation, Review

# Register your models here.
admin.site.register(Room)
admin.site.register(Currency)
admin.site.register(Reservation)
admin.site.register(Review)