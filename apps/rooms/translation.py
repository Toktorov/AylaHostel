from modeltranslation.translator import translator, TranslationOptions
from apps.rooms.models import Room

class RoomTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Room, RoomTranslationOptions)