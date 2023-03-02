from django.shortcuts import render, redirect

from apps.settings.models import Setting, Promotion
from apps.rooms.models import Room, Reservation, Review
from apps.telegram.views import get_reservation_text

# Create your views here.
def rooms(request):
    setting = Setting.objects.latest('id')
    rooms = Room.objects.all()
    promotions = Promotion.objects.all().order_by('-id')[:1]
    context = {
        'setting' : setting,
        'rooms' : rooms,
        'promotions' : promotions,
    }
    return render(request, 'room/rooms.html', context)

def room_detail(request, id):
    setting = Setting.objects.latest('id')
    room = Room.objects.get(id = id)
    one_random_room = Room.objects.all().order_by('?')[:1]
    two_random_room = Room.objects.all().order_by('?')[:1]
    reviews = Review.objects.filter(room = room, checked = True).order_by('-created')
    promotions = Promotion.objects.all().order_by('-id')[:1]
    if request.method == "POST":
        if 'reservation' in request.POST:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone_number = request.POST.get('phone_number')
            arrival_date = request.POST.get('arrival_date')
            departure_date = request.POST.get('departure_date')
            reservation_id = Reservation.objects.create(room = room, first_name = first_name, last_name = last_name, phone_number = phone_number, arrival_date = arrival_date, departure_date = departure_date)
            get_reservation_text(f"""Заявка на бронь #{reservation_id.id}:
Фамилия: {reservation_id.first_name}
Имя: {reservation_id.last_name}
Номер: {reservation_id.phone_number}
Комната: {reservation_id.room}
Дата заезда: {reservation_id.arrival_date}
Дата отъезда {reservation_id.departure_date}

Дата создания: {reservation_id.created.date()}""", int(setting.id_reservation))
            return redirect('confirmation', reservation_id.id)
        if 'review' in request.POST:
            name = request.POST.get('name')
            text = request.POST.get('text')
            review = Review.objects.create(room = room, name = name, text = text)
            get_reservation_text(f"""Оставлен отзыв #{review.id}
Комната: {review.room}
Имя: {review.name}
Текст: {review.text}
Статус: {review.checked}
Дата {review.created}""", int(setting.id_review))
            return redirect('review_confirmation')
    context = {
        'setting' : setting,
        'room' : room,
        'reviews' : reviews,
        'one_random_room' : one_random_room,
        'two_random_room' : two_random_room,
        'promotions' : promotions,
    }
    return render(request, 'room/room_detail.html', context)

def review_confirmation(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting
    }
    return render(request, 'confirm_comment.html', context)

def reservation(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        arrival_date = request.POST.get('arrival_date')
        departure_date = request.POST.get('departure_date')
        if first_name and last_name and phone_number:
            reservation = Reservation.objects.create(room_id = None, first_name = first_name, last_name = last_name, phone_number = phone_number, arrival_date = arrival_date, departure_date = departure_date)
            get_reservation_text(f"""Заявка на бронь #{reservation.id}:
Фамилия: {reservation.first_name}
Имя: {reservation.last_name}
Номер: {reservation.phone_number}
Дата заезда: {reservation.arrival_date}
Дата отъезда {reservation.departure_date}

Дата создания: {reservation.created.date()}""", int(setting.id_reservation))
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
        arrival_date = request.POST.get('arrival_date')
        departure_date = request.POST.get('departure_date')
        if first_name and last_name and phone_number:
            reservation = Reservation.objects.create(room_id = id,first_name = first_name, last_name = last_name, phone_number = phone_number, arrival_date = arrival_date, departure_date =departure_date)
            get_reservation_text(f"""Заявка на бронь #{reservation.id}:
Фамилия: {reservation.first_name}
Имя: {reservation.last_name}
Номер: {reservation.phone_number}
Комната: {reservation.room}
Дата заезда: {reservation.arrival_date}
Дата отъезда {reservation.departure_date}

Дата создания: {reservation.created.date()}""", int(setting.id_reservation))
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