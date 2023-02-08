import factory
import datetime
import factory.fuzzy
from factory.django import DjangoModelFactory
from main.models import *
from django.utils import timezone

class AutorFactory(DjangoModelFactory):
    class Meta:
        model = autor

    ime = factory.Faker("first_name")
    prezime = factory.Faker("first_name")
    titula = factory.Faker("sentence", nb_words=2)
    predgovor = factory.Faker("sentence", nb_words=100)

class ZanrFactory(DjangoModelFactory):
    class Meta:
        model = zanr

    zanr = factory.Faker("sentence", nb_words=2)

class KategorijaFactory(DjangoModelFactory):
    class Meta:
        model = kategorija

    dobna_skupina = factory.Faker("pyint", min_value = 5, max_value= 100)
    edukativna_namjena = factory.Faker("pybool")

class KnjigaFactory(DjangoModelFactory):
    class Meta: 
        model = knjiga

    naslov = factory.Faker("sentence", nb_words=5)
    sadrzaj = factory.Faker("sentence", nb_words=500)
    izdavanje = factory.Faker("date_time")
    nakladnik = factory.Faker("sentence", nb_words = 3)
    dostupnost = factory.Faker("pybool")
    autorKnjige = factory.Iterator(autor.objects.all())
    kategorijaKnjige = factory.SubFactory(KategorijaFactory)

class ClanstvoFactory(DjangoModelFactory):
    class Meta:
        model = clanstvo

    dugovanje = factory.Faker("pybool")
    odobrenje_posudbe = factory.Faker("pybool")
    trajanje_clanstva = factory.Faker("pyint", min_value=1, max_value=60)