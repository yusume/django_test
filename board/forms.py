from django import forms
from .models import board

class boardForm(forms.ModelForm):
    
    class Meta:
        model = board
        fields = ('title', 'contents',)