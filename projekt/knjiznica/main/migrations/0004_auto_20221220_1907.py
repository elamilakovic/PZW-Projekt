# Generated by Django 2.2.12 on 2022-12-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20221216_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategorija',
            name='dobna_skupina',
            field=models.CharField(max_length=2),
        ),
    ]
