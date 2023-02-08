from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import homepage, knjigaList, autorList, kategorijaList, clanstvoList, zanrList


class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('homepage')
        # print(resolve(url))

        self.assertEquals(resolve(url).func, homepage)

    def test_knjiga_url_is_resolved(self):
        url = reverse('Knjigas')

        self.assertEquals(resolve(url).func.view_class, knjigaList)

    def test_autor_url_is_resolved(self):
        url = reverse('Autori')

        self.assertEquals(resolve(url).func.view_class, autorList)

    def test_clanstvo_url_is_resolved(self):
        url = reverse('Clanstvos')

        self.assertEquals(resolve(url).func.view_class, clanstvoList)

    def test_kategorija_url_is_resolved(self):
        url = reverse('Kategorijas')

        self.assertEquals(resolve(url).func.view_class, kategorijaList)

    def test_zanr_url_is_resolved(self):
        url = reverse('Zanrs')

        self.assertEquals(resolve(url).func.view_class, zanrList)