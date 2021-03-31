from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    path("home", home_view, name="home"),
    path("profile", profile_view, name="profile"),
    path("key", key_view, name="key"),
    path("thisweek", thisweek_view, name="thisweek"),
    path("today", today_view, name="today"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
