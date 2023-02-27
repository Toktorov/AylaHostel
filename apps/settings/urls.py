from django.urls import path
from apps.settings.views import index, about, contact, error_settings_page, news_detail, news_index, confirm_contact

urlpatterns = [
    path('', index, name = "index"),
    path('news/', news_index, name = "news_index"),
    path('news/<int:id>/', news_detail, name = "news_detail"),
    path('about/', about, name = "about"),
    path('contact/', contact, name= "contact"),
    path('contact/confirm/', confirm_contact, name = "confirm_contact"),
    path('settings/error/', error_settings_page, name = "error_page")
]