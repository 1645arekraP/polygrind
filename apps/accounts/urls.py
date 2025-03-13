from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("settings/", views.settings, name="settings"),
    path("logout/", views.logout_view, name="logout"),
    path("respond_friend_request/<int:request_id>/<str:response>/", views.respond_friend_request, name="respond_friend_request"),
]