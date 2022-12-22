# Generated by Django 2.2.12 on 2022-12-16 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_knjiga_autorknjige'),
    ]

    operations = [
        migrations.AddField(
            model_name='knjiga',
            name='kategorijaKnjige',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to='main.Kategorija'),
        ),
        migrations.AddField(
            model_name='knjiga',
            name='zanrovi',
            field=models.ManyToManyField(to='main.Zanr'),
        ),
    ]