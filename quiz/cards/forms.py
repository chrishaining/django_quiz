from django import forms

from .models import *

class CardForm(forms.ModelForm):
    card = forms.ModelChoiceField(Card.objects.all())
    class Meta:
        model = Card
        fields = ('question', 'answer')