from django.contrib import admin
from .models import *
# Register your models here.
model_list = [knjiga, autor, zanr, clanstvo, kategorija]
admin.site.register(model_list)
