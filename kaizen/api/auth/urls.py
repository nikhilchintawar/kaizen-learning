from django.urls import path
from rest_framework.authtoken import views as rest_framework_views
from .views import SignIn, SignUpAPI, SignOutAPI, UserAPI

urlpatterns = [
    path("signin/", SignIn, name="signin"),
    path("signup/", SignUpAPI.as_view(), name="signup"),
    path("signout/", SignOutAPI.as_view(), name="signout"),
    path("profile/", UserAPI.as_view(), name="current_user"),
    path(
        "get_auth_token",
        rest_framework_views.obtain_auth_token,
        name="get_auth_token",
    ),
]
