from django.shortcuts import render
from apps.settings.models import Setting, Contact
from apps.rooms.models import Room

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    rooms = Room.objects.all()
    context = {
        'setting' : setting,
        'rooms' : rooms,
    }
    return render(request, 'index.html', context)