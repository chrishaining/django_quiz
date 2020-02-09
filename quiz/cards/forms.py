from django import forms
from .models import *

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('question', 'answer', 'url')


# class MultipleChoiceCardForm(forms.ModelForm):
#     class Meta:
#         model = MultipleChoiceCard
#         # answer = answer= forms.ChoiceField(label='What is your answer?', widget=forms.RadioSelect(choices=)
#         fields = ('question', 'answer', 'url')



class MultipleChoiceCardForm(forms.Form):
    question = forms.CharField(max_length=100)
    A = 'A'
    B = 'B'
    C = 'C'
    ANSWER_CHOICES = [
        (A, 'A'),
        (B, 'B'),
        (C, 'C')
    ]
    answer = forms.CharField(max_length=3, widget=forms.Select(choices=ANSWER_CHOICES))
    # url = forms.URLField(max_length=250)

# class BookForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())