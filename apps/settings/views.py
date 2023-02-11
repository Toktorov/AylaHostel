from django.shortcuts import render, redirect

from apps.settings.models import Setting, Contact, Review, Gallery, FAQ, News, Promotion, Benefit, Team,WeAre
from apps.rooms.models import Room

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
            return redirect('index')
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

def user_login(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting
    }
    return render(request, 'custom_admin/login.html', context)

def error_settings_page(request):
    return render(request, 'error.html')