from django.urls import path
from . import views
from main.views import *

app_name = 'main'  

urlpatterns = [
    path("", homepage, name="homepage"),
    path("Autors", Autors),
    path("Knjigas", Knjigas),
    path("Clanstvo", clanstvoList.as_view()),
    path("Kategorija", kategorijaList.as_view()),
    path("Zanr", zanrList.as_view()),

]