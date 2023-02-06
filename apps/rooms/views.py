from django.shortcuts import render
from apps.settings.models import Setting
from apps.rooms.models import Room

# Create your views here.
def room_detail(request, id):
    setting = Setting.objects.latest('id')
    room = Room.objects.get(id = id)
    context = {
        'setting' : setting,
        'room' : room
    }
    return render(request, 'room/room_detail.html', context)