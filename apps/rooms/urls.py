from django.urls import path 
from apps.rooms.views import room_detail, reservation, reservation_room, confirmation, rooms, review_confirmation


urlpatterns = [
    path('', rooms, name = "rooms"),
    path('<int:id>/', room_detail, name = "room_detail"),
    path('review/confirmation/', review_confirmation, name = "review_confirmation"),
    path('reservation/', reservation, name = "reservation"),
    path('reservation/<int:id>/', reservation_room, name = "reservation_room"),
    path('confirmation/<int:id>/', confirmation, name = "confirmation")
]