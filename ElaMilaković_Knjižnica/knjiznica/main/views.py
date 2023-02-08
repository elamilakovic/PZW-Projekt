from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from main.models import *

def homepage(request):
    return render (request, "homepage.html")

class knjigaList(ListView):
    model = knjiga
    
class autorList(ListView):
    model = autor
    
class kategorijaList(ListView):
    model = kategorija

class clanstvoList(ListView):
    model = clanstvo

class zanrList(ListView):
    model = zanr

def Autori(request):
    Autori = autor.objects.all().values()
    template = loader.get_template('main/autor_list.html')
    context = {'Autori': Autori}
    return HttpResponse(template.render(context, request))

def AutoriIme(request):
    AutoriIme = autor.objects.filter(ime__startswith='A')
    context = {'AutoriIme': AutoriIme}
    return render(request, 'main/AutoriIme.html', context=context)

def Knjigas(request):
    Knjigas = knjiga.objects.all().values()
    template = loader.get_template('main/knjiga_list.html')
    context = {'Knjigas': Knjigas}
    return HttpResponse(template.render(context, request))

def KnjigePretraga(request):
    KnjigePretraga = knjiga.objects.filter(naslov__contains='ona')
    context = {'KnjigePretraga' : KnjigePretraga}
    return render (request, 'main/knjige_pretraga.html', context=context)

def Clanstvos(request):
    Clanstvos = clanstvo.objects.all().values()
    template = loader.get_template('main/clanstvo_list.html')
    context = {'Clanstvos': Clanstvos}
    return HttpResponse(template.render(context, request))

def Kategorijas(request):
    Kategorijas = kategorija.objects.all().values()
    template = loader.get_template('main/kategorija_list.html')
    context = {'Kategorijas': Kategorijas}
    return HttpResponse(template.render(context, request))

def Zanrs(request):
    Zanrs = zanr.objects.all().values()   
    template = loader.get_template('main/zanr_list.html')
    context = {'Zanrs': Zanrs}
    return HttpResponse(template.render(context, request))
