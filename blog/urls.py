from django.urls import path
from . import views
from .models import MinecraftUser, Item

urlpatterns = [
    path("<int:id>", views.base_page, name="base"),
    path("", views.home_page, name="home"),
    path("home/", views.home_page, name="home"),
    path("error/", views.error_page, name="error"),
    path("error/home/", views.home_page, name="home"),
    path("#/", views.error_page, name="error"),
    path("<int:id>/profile/", views.profile_page, name="profile"),
    path("create/", views.create_account_page, name="create account"),
    path("<int:id>", views.user_input_int_page, name="user_input_page")
]