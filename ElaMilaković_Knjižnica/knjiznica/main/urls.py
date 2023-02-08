from django.urls import path
from . import views
from main.views import *

app_name = 'main'  

urlpatterns = [
    path("", homepage, name="homepage"),
    path("Autori", Autori),
    path("AutoriIme", AutoriIme),
    path("Knjigas", Knjigas),
    path("KnjigePretraga", KnjigePretraga),
    path("Clanstvos", Clanstvos),
    path("Kategorijas", Kategorijas),
    path("Zanrs", Zanrs),
]