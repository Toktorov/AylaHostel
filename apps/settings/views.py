from django.shortcuts import render, redirect

from apps.settings.models import Setting, Contact, Review, Gallery, FAQ, News, Promotion, Benefit, Team
from apps.rooms.models import Room

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    rooms = Room.objects.all()
    reviews = Review.objects.all().order_by('?')[:5]
    faqs = FAQ.objects.all().order_by('id')
    news = News.objects.all().order_by('-id')[:3]
    galleries = Gallery.objects.all().order_by('-id')[:10]
    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact.objects.create(name = name, phone_number = phone_number, email = email, message = message)
        return redirect('index')
    context = {
        'setting' : setting,
        'rooms' : rooms,
        'reviews' : reviews,
        'faqs' : faqs,
        'news' : news,
        'galleries' : galleries,
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