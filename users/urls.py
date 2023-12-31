from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (register_request,
                    login_request,
                    logout_request,

                    password_success,
                    PasswordChangeView,
                    )

urlpatterns = [
    path("register/", register_request, name="register"),
    path("logout", logout_request, name="logout"),

    path("login/", login_request, name="login"),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='main/change-password.html')),

    path('password/', PasswordChangeView.as_view(template_name='main/change-password.html'), name='password-change'),
    path("password/seccess", password_success, name="password-success"),
]
