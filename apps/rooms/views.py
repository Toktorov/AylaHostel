from django.shortcuts import render, redirect
from apps.settings.models import Setting, Reservation, Review
from apps.rooms.models import Room

# Create your views here.
def rooms(request):
    setting = Setting.objects.latest('id')
    rooms = Room.objects.all()
    context = {
        'setting' : setting,
        'rooms' : rooms
    }
    return render(request, 'room/rooms.html', context)

def room_detail(request, id):
    setting = Setting.objects.latest('id')
    room = Room.objects.get(id = id)
    one_random_room = Room.objects.all().order_by('?')[:1]
    two_random_room = Room.objects.all().order_by('?')[:1]
    reviews = Review.objects.filter(room = room, checked = True).order_by('-created')
    context = {
        'setting' : setting,
        'room' : room,
        'reviews' : reviews,
        'one_random_room' : one_random_room,
        'two_random_room' : two_random_room
    }
    return render(request, 'room/room_detail.html', context)

def reservation(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        if first_name and last_name and phone_number:
            reservation = Reservation.objects.create(room_id = None,first_name = first_name, last_name = last_name, phone_number = phone_number)
            return redirect('confirmation', reservation.id)
    context = {
        'setting' : setting,
    }
    return render(request, 'room/reservation.html', context)

def reservation_room(request, id):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        if first_name and last_name and phone_number:
            reservation = Reservation.objects.create(room_id = id,first_name = first_name, last_name = last_name, phone_number = phone_number)
            return redirect('confirmation', reservation.id)
    context = {
        'setting' : setting,
    }
    return render(request, 'room/reservation.html', context)

def confirmation(request, id):
    setting = Setting.objects.latest('id')
    reservation = Reservation.objects.get(id = id)
    context = {
        'setting' : setting,
        'reservation' : reservation
    }
    return render(request, 'room/confirmation.html', context)