from django.urls import path, include
from rest_framework.authtoken import views as rest_framework_views
from .views import login

urlpatterns = [
    path("login/", login, name="login"),
    path(
        "get_auth_token",
        rest_framework_views.obtain_auth_token,
        name="get_auth_token",
    ),
]
