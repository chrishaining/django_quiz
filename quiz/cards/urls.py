from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('card/new/', views.card_new, name='card_new'),
    path('test_yourself/', views.test_yourself, name='test_yourself'),
    path('card/<int:pk>/update/', views.CardUpdate.as_view(), name='card_update'),
    path('card/<int:pk>/delete/', views.CardDelete.as_view(), name='card_delete')
]