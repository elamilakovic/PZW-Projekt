from django.db import models
from django.utils import timezone

class autor(models.Model):
    ime = models.CharField(max_length=20)
    prezime = models.CharField(max_length=30)
    titula = models.CharField(max_length=10)
    predgovor = models.TextField()

    def __str__(self):
        return self.prezime

class zanr(models.Model):
    DjecjaFikcija = 'DF'
    Romantika = 'RO'
    ZnanstvenaFantastika = 'ZF'
    TrilerHoror = 'TH'
    Biografija = 'BI'
    Motivacija = 'MO'
    Strip = 'ST'
    ZANR_CHOICES = [
        (DjecjaFikcija, 'Djecja fikcija'),
        (Romantika, 'Romantika'),
        (ZnanstvenaFantastika, 'Znanstvena fantastika'),
        (TrilerHoror, 'Triler ili horor'),
        (Biografija, 'Biografija ili autobiografija'),
        (Motivacija, 'Motivacijske knjige'),
        (Strip, 'Strip'),
    ]
    zanr = models.CharField(max_length=2,choices=ZANR_CHOICES,default=Biografija)

class kategorija(models.Model):
    dobna_skupina = models.IntegerField()
    edukativna_namjena = models.BooleanField(default=False)

class knjiga(models.Model):
    naslov = models.CharField(max_length=100)
    sadrzaj = models.TextField()
    izdavanje = models.DateTimeField("datum izdavanja")
    nakladnik = models.CharField(max_length=40)
    dostupnost = models.BooleanField(default=True)
    autorKnjige = models.ForeignKey(autor, default=1, on_delete=models.CASCADE)
    zanrovi = models.ManyToManyField(zanr)
    kategorijaKnjige = models.OneToOneField(kategorija, on_delete=models.CASCADE, default=True )

    def __str__(self):
        return self.naslov  

class clanstvo(models.Model):
    dugovanje = models.BooleanField(default=False)
    odobrenje_posudbe = models.BooleanField(default=True)
    trajanje_clanstva = models.IntegerField()

