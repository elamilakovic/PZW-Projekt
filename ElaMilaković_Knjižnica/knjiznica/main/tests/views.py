from django.test import TestCase, Client
from django.urls import reverse
from main.models import autor, knjiga, clanstvo, kategorija, zanr


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('homepage')

        self.autor1 = autor.objects.create(
            ime = 'some-author',
            prezime = 'some-author',
            titula = 'TestTitula',
            predgovor = 'TestPredgovor',
        )

    def test_project_homepage_GET(self):
        client = Client()

        response = client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')

    def test_project_autori_GET(self):
        client = Client()

        response = client.get(self.autor1)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/autor_list.html')
