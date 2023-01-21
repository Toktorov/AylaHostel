from django.urls import path
from apps.settings.views import index 


urlpatterns = [
    path('', index, name = "index")
]