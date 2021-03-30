from django import forms
from .models import *

class NameForm(forms.Form):
    name = forms.CharField(max_length=20)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UploadProfile
        fields = ['picture']

""" class InfoForm(forms.ModelForm):
    class Meta:
        model = EditInfo
        fields = ['bio'] """