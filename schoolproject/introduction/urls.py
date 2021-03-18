from django.urls import path

from .views import home_view, profile_view, key_view, thisweek_view, today_view


urlpatterns = [
    path("home", home_view, name="home"),
    path("profile", profile_view, name="profile"),
    path("key", key_view, name="key"),
    path("thisweek", thisweek_view, name="thisweek"),
    path("today", today_view, name="today"),
]
