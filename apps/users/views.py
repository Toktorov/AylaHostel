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
    context = {
        'setting' : setting,
        'rooms' : rooms,
        'reservations' : reservations
    }
    return render(request, 'custom_admin/index.html', context)