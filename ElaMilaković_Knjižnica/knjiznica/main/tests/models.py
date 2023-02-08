from django.test import TestCase
from main.models import autor, knjiga, clanstvo, kategorija, zanr


class Testmodels(TestCase):

    def setUp(self):
        self.author1 = autor.objects.create(
            ime = 'some-author',
            prezime = 'some-author',
            titula = 'TestTitula',
            predgovor = 'TestPredgovor',
        )

    def test_autor(self):
        self.assertEquals(self.author1.ime, "some-author")

    def setUp2(self):
        self.knjiga1 = knjiga.objects.create(
            naslov = 'some-knjiga',
            sadrzaj = 'some-sadrzaj',
            izdavanje = 'some-izdavanje',
        )
    
    def test_knjiga(self):
        self.assertEquals(self.knjiga1.naslov, "some-knjiga")
