from django.shortcuts import render

from .forms import *


def home_view(request):
        if request.method == "POST":
                form = NameForm(request.POST)
                if form.is_valid():
                        form.save()
                        return render(request, "home.html", {"name":form.cleaned_data["name"]})
        else:
                form = NameForm()
                return render(request, "home.html", {"form": NameForm})

def profile_view(request):
        if request.method == "POST":
                form = ProfileInfoForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save()
                        update_info = form.instance     
                        return render(request, "profile.html", {"update_info":update_info, "nickname":form.cleaned_data["nickname"],"bio":form.cleaned_data["bio"]})                         
        else:
                form = ProfileInfoForm()
                return render(request, "profile.html", {"form":ProfileInfoForm})

def key_view(request):
        if request.method == "POST":
                form = KeyForm(request.POST)
                if form.is_valid():
                        form.save()
                        return render(request, "key.html", {"key":form.cleaned_data["key"], "description":form.cleaned_data["description"]})
        else:
                form = KeyForm()
                return render(request, "key.html", {"form": KeyForm})

def thisweek_view(request):
        if request.method == "POST":
                form = ThisWeekForm(request.POST)
                while form.is_valid():
                        form.save()
                        return render(request, "thisweek.html", {"key":form.cleaned_data["key"], "details":form.cleaned_data["details"]})
        else:
                form = ThisWeekForm()
                return render(request, "thisweek.html", {"form": ThisWeekForm})

def today_view(request):
        if request.method == "POST":
                form = ThisWeekForm(request.POST)
                if form.is_valid():
                        form.save()
                        return render(request, "today.html", {"key":form.cleaned_data["key"], "details":form.cleaned_data["details"]})
        else:
                form = ThisWeekForm()
                return render(request, "today.html", {"form": ThisWeekForm})