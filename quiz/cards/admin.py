from django.contrib import admin
from cards.models import *
from django.contrib.admin import sites

# Register your models here.
admin.site.register(Card)
sites.AdminSite.site_url = '/cards/'