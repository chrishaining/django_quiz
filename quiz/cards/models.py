from django.db import models
# from multiselectfield import MultiSelectField

# Create your models here.
class Card(models.Model):
    question = models.TextField()
    answer = models.TextField()
    url = models.URLField(max_length=250, blank=True)

    def __str__(self):
        return self.question

# use Python's property decorator to format the url so it can be used inside html tags
    @property
    def url_formatted(self):
        return '<a href="%s"></a>' % self.url

    # could have a separate type of card for multiple choice

class MultipleChoiceCard(models.Model):
    question = models.TextField()

    A = 'A'
    B = 'B'
    C = 'C'

    CHOICES = [
        (A, 'A'),
        (B, 'B'),
        (C, 'C')
    ]

    answer = models.CharField(max_length=6, choices=CHOICES)
    # answer = MultiSelectField(choices=CHOICES, max_choices=3, max_length=3)

    
    url = models.URLField(max_length=250, blank=True)
    
    def __str__(self):
        return self.question

    @property
    def url_formatted(self):
        return '<a href="%s"></a>' % self.url