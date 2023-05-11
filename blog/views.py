from django.shortcuts import render
from django.http import HttpResponse
from .models import MinecraftUser, Item

# Create your views here.

def base_page(reponse, id):
    ls = MinecraftUser.objects.get(id=id)
    # dynamic_dict = {"name": ls.name}
    return render(reponse, "base.html", {})

def home_page(request):
    return render(request, "home.html", {})

def error_page(request):
    return render(request, "error.html")

# Dynamic page
def user_input_int_page(response, id):
    # ls1 = MinecraftUser.objects.get(name=name)
    ls = MinecraftUser.objects.get(id=id)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (ls.name, str(item.text)))
