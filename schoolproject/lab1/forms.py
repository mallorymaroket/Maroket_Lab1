from django import forms

class NameForm(forms.Form):
    nickname = forms.CharField(label="Enter your nickname:", max_length=20)