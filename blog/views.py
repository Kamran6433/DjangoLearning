from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import MinecraftUser, Item
from .forms import CreateAccount

# Create your views here.

def base_page(reponse, id):
    ls = MinecraftUser.objects.get(id=id)
    dynamic_dict = {"name": ls.name}
    return render(reponse, "base.html", dynamic_dict)


def home_page(request):
    return render(request, "home.html", {})


def error_page(request):
    return render(request, "error.html")


def profile_page(reponse, id):
    ls = MinecraftUser.objects.get(id=id)
    return render(reponse, "profile.html", {"ls": ls})


def create_account_page(response):
    # Post is a high security request which hides the information. Get has less security and anyone can see the information.
    if response.method == "POST":
        form = CreateAccount(response.POST)

        if form.is_valid():
            # This decrypts the data
            n = form.cleaned_data["name"]
            t = MinecraftUser(name=n)
            t.save()
        
        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateAccount()
    
    return render(response, "create_account.html", {"form": form})


# Dynamic page
def user_input_int_page(response, id):
    # ls1 = MinecraftUser.objects.get(name=name)
    ls = MinecraftUser.objects.get(id=id)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (ls.name, str(item.text)))
