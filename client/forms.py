from django import forms
from .models import Picture
from encoder import encoder
from decoder import decoder


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = '__all__'

    def clean_message(self):
        message = self.cleaned_data['message']
        cleaned_message = encoder.CreateMessage(message)
        return cleaned_message

