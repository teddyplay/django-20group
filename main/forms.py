from django import forms

from .models import Film

class PostForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = ('title', 'producer', 'rate', 'duration')

