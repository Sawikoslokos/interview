from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.shortURL),
    path(r'shorten/<uuid:pk>', views.redirectToLong)
]