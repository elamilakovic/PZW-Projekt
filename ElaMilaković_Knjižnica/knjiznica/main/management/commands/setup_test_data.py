import random
from django.utils import timezone
from django.db import transaction
from django.core.management.base import BaseCommand
from main.models import *
from main.factory import (AutorFactory, KnjigaFactory, ZanrFactory, ClanstvoFactory)

NUM_AUTORS = 100
NUM_KNJIGAS = 100
NUM_ZANRS = 1
NUM_CLANSTVOS = 20

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [autor, knjiga, clanstvo, zanr]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_AUTORS):
            autor = AutorFactory()

        for _ in range(NUM_KNJIGAS):
            knjiga = KnjigaFactory()

        for _ in range(NUM_ZANRS):
            zanr = ZanrFactory()
        
        for _ in range(NUM_CLANSTVOS):
            clanstvo = ClanstvoFactory()
