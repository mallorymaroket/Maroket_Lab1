from django.shortcuts import render
from django.http import HttpResponse

from .forms import NameForm


def home_view(request):
        if request.method == "POST":
                form = NameForm(request.POST)
                if form.is_valid():
                        name = form.cleaned_data["nickname"]
                        return render(request, "name.html", {"name":name})
        else:
                form = NameForm()
                return render(request, "home.html", {"form": NameForm})

def profile_view(request):
        return render(request, "profile.html")

def key_view(request):
        return render(request, "key.html")

def thisweek_view(request):
        return render(request, "thisweek.html")

def today_view(request):
        return render(request, "today.html")