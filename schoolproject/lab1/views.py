from django.shortcuts import render
from django.conf import settings

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
                form = ProfileForm(request.POST, request.FILES)
                if form.is_valid():
                        upload = form.instance
                        return render(request, "profile.html", {"upload":upload})
                        # form = InfoForm(request.POST)
        else:
                form = ProfileForm()
                return render(request, 'profile.html', {'form':form})

def key_view(request):
        return render(request, "key.html")

def thisweek_view(request):
        return render(request, "thisweek.html")

def today_view(request):
        return render(request, "today.html")

""" def upload_profile(request):
        if request.method == POST:
                form = ProfileForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save()
                        upload = form.instance
                        return render(request, "profile.html", {"upload":upload})
                else:
                        form = PictureForm()
                return render(request, 'profile.html', {'form':form})

def upload_picture(request):
        if request.method == "POST":
                form = PictureForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save()
                        upload = form.instance
                        return render(request, "profile.html", {"upload":upload})
        else:
                form = PictureForm()
                return render(request, "profile.html", {"form":PictureForm}) """