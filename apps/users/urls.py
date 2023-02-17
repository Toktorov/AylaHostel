from django.urls import path

from apps.users.views import user_login, admin_panel, accept_reservations, refusal_reservations, refusal_reviews, create_room, delete_room, update_room, update_room_detail

urlpatterns = [
    path('user/login/', user_login, name = "admin_login_user"),
    path('user/custom/admin/', admin_panel, name = "admin_panel"),
    path('user/custom/admin/accept/', accept_reservations, name = "accept_reservations"),
    path('user/custom/admin/refusal/', refusal_reservations, name = "refusal_reservations"),
    path('user/custom/admin/refusal/review/', refusal_reviews, name = "refusal_reviews"),
    path('user/custom/admin/room/create/', create_room, name = "create_room"),
    path('user/custom/admin/room/delete/', delete_room, name = "delete_room"),
    path('user/custom/admin/room/update/', update_room, name = "update_room"),
    path('user/custom/admin/room/update/<int:id>/', update_room_detail, name = "update_room_detail"),
]