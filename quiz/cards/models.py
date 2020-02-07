from django.db import models

# Create your models here.
class Card(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    url = models.URLField(max_length=250)

    def __str__(self):
        return self.question

# use Python's property decorator to format the url so it can be used inside html tags
    @property
    def url_formatted(self):
     return '<a href="%s"></a>' % self.url

    # could have a separate type of card for multiple choice