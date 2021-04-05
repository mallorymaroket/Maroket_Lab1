from django.shortcuts import render

from .forms import *


def home_view(request):
        if request.method == "POST":
                form = NameForm(request.POST)
                if form.is_valid():
                        return render(request, "home.html", {"name":form.cleaned_data["name"]})
        else:
                form = NameForm()
                return render(request, "home.html", {"form": NameForm})

def profile_view(request):
        if request.method == "POST":
                form = ProfileInfoForm(request.POST, request.FILES)
                if form.is_valid():
                        # form.save()
                        update_info = form.instance     
                        return render(request, "profile.html", {"update_info":update_info, "nickname":form.cleaned_data["nickname"],"bio":form.cleaned_data["bio"]})                         
        else:
                form = ProfileInfoForm()
                return render(request, "profile.html", {"form":ProfileInfoForm})

def key_view(request):
        if request.method == "POST":
                form = KeyForm(request.POST)
                if form.is_valid():
                        return render(request, "key.html", {"key":form.cleaned_data["key"], "description":form.cleaned_data["description"]})
        else:
                form = KeyForm()
                return render(request, "key.html", {"form": KeyForm})

def thisweek_view(request):
        return render(request, "thisweek.html")

def today_view(request):
        return render(request, "today.html")