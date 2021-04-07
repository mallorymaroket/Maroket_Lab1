from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm

from .models import *

class HomeForm(forms.ModelForm):
    class Meta:
        model = InputName
        fields = ['name']

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = UploadPicture
        fields = ['picture']

class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UpdateInfo
        fields = ['nickname', 'bio']

class KeyForm(forms.ModelForm):
    class Meta:
        model = AddKey
        fields = ['key', 'description']

class ThisWeekForm(forms.ModelForm):
    class Meta:
        model = AddItemThisWeek
        fields = ['key', 'details']

class TodayForm(forms.ModelForm):
    class Meta:
        model = AddItemToday
        fields = ['key', 'details']