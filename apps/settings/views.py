from django.shortcuts import render, redirect

from apps.settings.models import Setting, Contact,Partners,  Gallery, FAQ, News, Promotion, Benefit, Team,WeAre, About
from apps.rooms.models import Room,Review
from apps.telegram.views import get_reservation_text

# Create your views here.
def index(request):
    try:
        setting = Setting.objects.latest('id')
    except:
        return redirect('error_page')
    weare = WeAre.objects.all().order_by('-id')[:10]
    rooms = Room.objects.all().order_by('?')[:10]
    reviews = Review.objects.all().order_by('?')[:5]
    faqs = FAQ.objects.all().order_by('id')
    news = News.objects.all().order_by('-id')[:3]
    galleries = Gallery.objects.all().order_by('-id')[:10]
    benefits = Benefit.objects.all().order_by('-id')
    if request.method == "POST":
        if 'contact' in request.POST:
            name = request.POST.get('name')
            phone_number = request.POST.get('phone_number')
            email = request.POST.get('email')
            message = request.POST.get('message')
            contact = Contact.objects.create(name = name, phone_number = phone_number, email = email, message = message)
            get_reservation_text(f"""Заявка на контакт #{contact.id}
Имя: {contact.name}
Номер: {contact.phone_number}
Почта: {contact.email}
Сообщение: {contact.message}
Создан: {contact.created.ctime()}""", -851422112)
            return redirect('confirm_contact')
    context = {
        'setting' : setting,
        'rooms' : rooms,
        'reviews' : reviews,
        'faqs' : faqs,
        'news' : news,
        'galleries' : galleries,
        'benefits' : benefits,
        'weare' : weare,
    }
    return render(request, 'index.html', context)

def about(request):
    setting = Setting.objects.latest('id')
    team = Team.objects.all()
    partners = Partners.objects.all()
    about = About.objects.latest('id')
    context = {
        'setting' : setting,
        'team' : team,
        'partners' : partners,
        'about' : about,
        
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
        get_reservation_text(f"""Заявка на контакт #{contact.id}
Имя: {contact.name}
Номер: {contact.phone_number}
Почта: {contact.email}
Сообщение: {contact.message}
Создан: {contact.created.ctime()}""", -851422112)
        return redirect('confirm_contact')
    context = {
        'setting' : setting
    }
    return render(request, 'contact.html', context)

def confirm_contact(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting
    }
    return render(request, 'confirm_contact.html', context)

def news_index(request):
    setting = Setting.objects.latest('id')
    news = News.objects.all().order_by('-id')[:12]
    context = {
        'setting' : setting,
        'news' : news
    }
    return render(request, 'news/index.html', context)

def news_detail(request, id):
    setting = Setting.objects.latest('id')
    news = News.objects.get(id = id)
    random_news = News.objects.all().order_by('?')[:5]
    context = {
        'setting' : setting,
        'news' : news,
        'random_news' : random_news
    }
    return render(request, 'news/detail.html', context)

def error_settings_page(request):
    return render(request, 'error.html')