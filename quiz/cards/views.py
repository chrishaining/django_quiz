from django.shortcuts import render
from django.http import HttpResponse
from cards.models import *

# Create your views here.
def index(request):
    cards = Card.objects.all()
    return render(request, "cards/index.html", locals())


