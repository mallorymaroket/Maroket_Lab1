from django.shortcuts import render
from bootstrap_modal_forms.generic import BSModalCreateView

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
                form = ProfilePicForm(request.POST, request.FILES)
                if form.is_valid():
                        # form.save()
                        upload_pic = form.instance
                        return render(request, "profile.html", {"upload_pic":upload_pic})          
        else:
                form = ProfilePicForm()
                return render(request, 'profile.html', {'form':form})

def key_view(request):
        return render(request, "key.html")

def thisweek_view(request):
        return render(request, "thisweek.html")

def today_view(request):
        return render(request, "today.html")