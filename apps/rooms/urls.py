from django.urls import path 
from apps.rooms.views import room_detail


urlpatterns = [
    path('<int:id>/', room_detail, name = "room_detail"),
]