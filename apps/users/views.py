from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from apps.settings.models import Setting
from apps.users.models import User
from apps.rooms.models import Room, Reservation, Review, Currency

# Create your views here.
def user_login(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('admin_panel')
        except:
            return redirect('admin_login_user')
    context = {
        'setting' : setting
    }
    return render(request, 'custom_admin/login.html', context)

def admin_panel(request):
    setting = Setting.objects.latest('id')
    rooms = Room.objects.all()
    reservations = Reservation.objects.all().order_by('-created').order_by('checked')
    accept_reservations = Reservation.objects.filter(checked = True)
    refusal_reservations = Reservation.objects.filter(checked = False)
    if request.method == "POST":
        if 'accept' in request.POST:
            reservation_id = request.POST.get('reservation_id')
            reservation_checked = Reservation.objects.get(id = int(reservation_id))
            reservation_checked.checked = True
            reservation_checked.save()
        if 'delete' in request.POST:
            reservation_id = request.POST.get('reservation_id')
            reservation_delete = Reservation.objects.get(id = int(reservation_id))
            reservation_delete.delete()
    context = {
        'setting' : setting,
        'rooms' : rooms,
        'reservations' : reservations,
        'accept_reservations' : accept_reservations,
        'refusal_reservations' : refusal_reservations,
    }
    return render(request, 'custom_admin/index.html', context)

def accept_reservations(request):
    setting = Setting.objects.latest('id')
    accept_reservations = Reservation.objects.filter(checked = True)
    if request.method == "POST":
        if 'delete' in request.POST:
            reservation_id = request.POST.get('reservation_id')
            reservation_delete = Reservation.objects.get(id = int(reservation_id))
            reservation_delete.delete()
    context = {
        'setting' : setting,
        'accept_reservations' : accept_reservations, 
    }
    return render(request, 'custom_admin/accept_reservation.html', context)

def refusal_reservations(request):
    setting = Setting.objects.latest('id')
    refusal_reservations = Reservation.objects.filter(checked = False)
    if request.method == "POST":
        if 'accept' in request.POST:
            reservation_id = request.POST.get('reservation_id')
            reservation_checked = Reservation.objects.get(id = int(reservation_id))
            reservation_checked.checked = True
            reservation_checked.save()
    context = {
        'setting' : setting,
        'refusal_reservations' : refusal_reservations,
    }
    return render(request, 'custom_admin/refusal_reservation.html', context)
    
def refusal_reviews(request):
    setting = Setting.objects.latest('id')
    reviews = Review.objects.filter(checked=False)
    if request.method == "POST":
        if 'accept' in request.POST:
            review_id = request.POST.get('review_id')
            review_checked = Review.objects.get(id = int(review_id))
            review_checked.checked = True 
            review_checked.save()
    context = {
        'setting' : setting,
        'reviews' : reviews,
    }
    return render(request, 'custom_admin/refusal_review.html', context)

def create_room(request):
    setting = Setting.objects.latest('id')
    currency = Currency.objects.all()
    if request.method == "POST":
        if 'create' in request.POST:
            title = request.POST.get('title')
            description = request.POST.get('description')
            image = request.FILES.get('image')
            price = request.POST.get('price')
            currency = request.POST.get('currency')
            print(title, description, image, price, currency)
            room = Room.objects.create(title = title, description = description, image = image, price_day = int(price), currency_id = int(currency))
            return redirect('room_detail', room.id)
    context = {
        'setting' : setting,
        'currency' : currency,
    }
    return render(request, 'custom_admin/create_room.html', context)

def delete_room(request):
    setting = Setting.objects.latest('id')
    rooms = Room.objects.all().order_by('-id')
    if request.method == "POST":
        if 'delete' in request.POST:
            room_id = request.POST.get('room_id')
            room = Room.objects.get(id = int(room_id))
            room.delete()
    context = {
        'setting' : setting,
        'rooms' : rooms
    }
    return render(request, 'custom_admin/delete_room.html', context)

def update_room(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting
    }
    return render(request, 'custom_admin/update_room.html', context)