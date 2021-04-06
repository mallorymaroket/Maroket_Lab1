from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm

from .models import *

class NameForm(forms.ModelForm):
    class Meta:
        model = InputName
        fields = ['name']

class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UpdateProfile
        fields = ['picture', 'nickname', 'bio']

class KeyForm(forms.ModelForm):
    class Meta:
        model = AddKey
        fields = ['key', 'description']

class ThisWeekForm(forms.ModelForm):
    class Meta:
        model = AddItem
        fields = ['key', 'details']