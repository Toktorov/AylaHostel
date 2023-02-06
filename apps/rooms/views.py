from django.shortcuts import render, redirect
from apps.settings.models import Setting, Reservation
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

def reservation_room(request, id):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        if first_name and last_name and phone_number:
            reservation = Reservation.objects.create(room_id = id,first_name = first_name, last_name = last_name, phone_number = phone_number)
        return redirect('index')
    context = {
        'setting' : setting,
    }
    return render(request, 'room/reservation.html', context)
