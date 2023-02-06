from django.urls import path 
from apps.rooms.views import room_detail, reservation_room


urlpatterns = [
    path('<int:id>/', room_detail, name = "room_detail"),
    path('reservation/<int:id>/', reservation_room, name = "reservation_room")
]