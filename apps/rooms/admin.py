from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.rooms.models import Room, Currency, Reservation, Review

# Register your models here.
class RoomAdmin(TranslationAdmin):
    list_display = ('title', 'description')

admin.site.register(Room, RoomAdmin)
admin.site.register(Currency)
admin.site.register(Reservation)
admin.site.register(Review)