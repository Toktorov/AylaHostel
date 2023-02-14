from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from apps.settings.models import Setting
from apps.users.models import User
from apps.rooms.models import Room, Reservation

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
    reservations = Reservation.objects.all().order_by('-created')
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