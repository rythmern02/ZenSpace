from django import forms
from .models import Club, ClubMessage


class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'description', 'image']


class ClubMessageForm(forms.ModelForm):
    class Meta:
        model = ClubMessage
        fields = ['content']
