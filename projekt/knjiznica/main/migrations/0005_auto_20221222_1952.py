# Generated by Django 2.2.12 on 2022-12-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20221220_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clanstvo',
            name='trajanje_clanstva',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='kategorija',
            name='dobna_skupina',
            field=models.IntegerField(),
        ),
    ]
