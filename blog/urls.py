from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("error/", views.error_page, name="error"),
    path("#/", views.error_page, name="error"),
]