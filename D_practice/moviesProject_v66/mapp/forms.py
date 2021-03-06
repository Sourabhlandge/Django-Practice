from django.forms.widgets import DateInput
from django import forms
from mapp.models import Movies

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['rdate', 'movie', 'hero', 'heroine', 'rating']
        widgets =  {'rdate':DateInput(attrs={'type':'date'})}