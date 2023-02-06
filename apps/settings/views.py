from django.shortcuts import render, redirect
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

def about(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting
    }
    return render(request, 'about.html', context)

def contact(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact.objects.create(name = name, phone_number = phone_number, email = email, message = message)
        return redirect('index')
    context = {
        'setting' : setting
    }
    return render(request, 'contact.html', context)