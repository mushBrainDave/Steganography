from django import forms
from .models import Message


class NameForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["message_text"]
