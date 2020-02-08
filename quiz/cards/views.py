from django.shortcuts import render, redirect
from django.http import HttpResponse
from cards.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    cards = Card.objects.all()
    return render(request, "cards/index.html", locals())

@login_required
def card_new(request):
    if request.method == "POST":
        form = CardForm(request.POST) 
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
            return redirect('index') 
    else:
        form = CardForm()
        return render(request, 'cards/card_form.html', {'form': form})

class CardUpdate(UpdateView):
    model = Card
    fields = ['question', 'answer', 'url']
    success_url = reverse_lazy('index')

class CardDelete(DeleteView):
    model = Card
    success_url = reverse_lazy('index')

    