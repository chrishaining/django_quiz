from django import forms
from .models import *

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('question', 'answer', 'url')


class MultipleChoiceCardForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceCard
        # answer = answer= forms.ChoiceField(label='What is your answer?', widget=forms.RadioSelect(choices=)
        fields = ('question', 'answer', 'url')