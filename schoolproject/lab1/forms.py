from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm

from .models import *

class NameForm(forms.Form):
    name = forms.CharField(max_length=20)

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = UploadProfile
        fields = ['picture']

""" class ProfileInfoForm(forms.Form):
    nickname = forms.CharField(max_length=20)
    bio = forms.CharField(widget=forms.Textarea) """