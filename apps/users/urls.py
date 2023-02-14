from django.urls import path

from apps.users.views import user_login, admin_panel

urlpatterns = [
    path('user/login/', user_login, name = "admin_login_user"),
    path('user/custom/admin/', admin_panel, name = "admin_panel")
]