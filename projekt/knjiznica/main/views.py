from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from main.models import *

def homepage(request):
    return render (request, "homepage.html")

def Autors(request):
    context = {"Autors": Autors} 
    return render (request, "main/autor_list.html" , context=context)

def Knjigas(request):
    return render (request, "main/knjiga_list.html")

class knjigaList(ListView):
    model = knjiga
    template_name = "main/knjiga_list.html"
    
class autorList(ListView):
    model = autor
    template_name = "main/autor_list.html"

    def get_queryset(self):
        self.Autor = get_object_or_404(autor, ime=self.kwargs['autor'])
        return autor.objects.filter(autor=self.autor)

class kategorijaList(ListView):
    model = kategorija
    template_name = "main/kategorija_list.html"

class clanstvoList(ListView):
    model = clanstvo
    template_name = "main/clanstvo_list.html"

class zanrList(ListView):
    model = zanr
    template_name = "main/zanr_list.html"


