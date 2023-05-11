from django.contrib import admin
from .models import MinecraftUser, Item

# Register your models here.
admin.site.register(MinecraftUser)
admin.site.register(Item)