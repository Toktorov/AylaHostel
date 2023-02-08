from django.urls import path
from apps.settings.views import index, about, contact, error_settings_page, news_detail

urlpatterns = [
    path('', index, name = "index"),
    path('news/<int:id>/', news_detail, name = "news_detail"),
    path('about/', about, name = "about"),
    path('contact/', contact, name= "contact"),
    path('settings/error/', error_settings_page, name = "error_page")
]