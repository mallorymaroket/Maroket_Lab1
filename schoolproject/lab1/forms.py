from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm

from .models import *

class NameForm(forms.Form):
    name = forms.CharField(max_length=20)

class ProfileInfoForm(forms.ModelForm):
    nickname = forms.CharField(max_length=20, label='Update Nickname:')
    bio = forms.CharField(widget=forms.Textarea, label='Update Bio:')
    class Meta:
        model = UpdateProfile
        fields = ['picture']

class KeyForm(forms.Form):
    KEY_TYPES=[
        ('Task:','Task'),
        ('Event:','Event'),
        ('Note:','Note'),
    ]

    key = forms.CharField(widget=forms.Select(choices=KEY_TYPES),label='Key:')
    description = forms.CharField(max_length=50, label='Description:')