from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('card/new/', views.card_new, name='card_new')
]