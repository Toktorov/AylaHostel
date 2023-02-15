from django.urls import path

from apps.users.views import user_login, admin_panel, accept_reservations, refusal_reservations, refusal_reviews

urlpatterns = [
    path('user/login/', user_login, name = "admin_login_user"),
    path('user/custom/admin/', admin_panel, name = "admin_panel"),
    path('user/custom/admin/accept/', accept_reservations, name = "accept_reservations"),
    path('user/custom/admin/refusal/', refusal_reservations, name = "refusal_reservations"),
    path('user/custom/admin/refusal/review/', refusal_reviews, name = "refusal_reviews"),
]