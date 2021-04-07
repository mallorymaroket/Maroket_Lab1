from django.shortcuts import render

from .forms import *


def home_view(request):
        if request.method == "POST":
                form = HomeForm(request.POST)
                if form.is_valid():
                        form.save()
                        return render(request, "home.html", {"name":form.cleaned_data["name"]})
        else:
                form = HomeForm()
                return render(request, "home.html", {"form": HomeForm})

def profile_view(request):
        if request.method == "POST":
                form = ProfileForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save()
                        update_info = form.instance     
                        return render(request, "profile.html", {"update_info":update_info, "nickname":form.cleaned_data["nickname"],"bio":form.cleaned_data["bio"], "form": ProfileForm})                         
        else:
                form = ProfileInfoForm()
                return render(request, "profile.html", {"form":ProfileForm})

def key_view(request):
        if request.method == "POST":
                form = KeyForm(request.POST)
                if form.is_valid():
                        form.save()
                        allkeys = AddKey.objects.all()
                        context = {
                        "key":form.cleaned_data["key"],
                        "description":form.cleaned_data["description"],
                        "allkeys":allkeys,
                        "form": KeyForm,
                        }
                        return render(request, "key.html", context)
        else:
                form = KeyForm()
                return render(request, "key.html", {"form": KeyForm})

def thisweek_view(request):
        if request.method == "POST":
                form = ThisWeekForm(request.POST)
                if form.is_valid():
                        form.save()
                        allitems = AddItemThisWeek.objects.all()
                        context = {
                        "key":form.cleaned_data["key"],
                        "details":form.cleaned_data["details"],
                        "allitems":allitems,
                        "form": ThisWeekForm,
                        }
                        return render(request, "thisweek.html", context)
        else:
                form = ThisWeekForm()
                return render(request, "thisweek.html", {"form": ThisWeekForm})

def today_view(request):
        if request.method == "POST":
                form = TodayForm(request.POST)
                if form.is_valid():
                        form.save()
                        allitems = AddItemToday.objects.all()
                        context = {
                        "key":form.cleaned_data["key"],
                        "details":form.cleaned_data["details"],
                        "allitems":allitems,
                        "form": TodayForm,
                        }
                        return render(request, "today.html", context)
        else:
                form = TodayForm()
                return render(request, "today.html", {"form": ThisWeekForm})