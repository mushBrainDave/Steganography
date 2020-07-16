from django import forms
from .models import Picture


class NameForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ["pic", "message"]
