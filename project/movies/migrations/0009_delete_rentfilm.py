# Generated by Django 4.2 on 2023-05-19 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_rentfilm'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RentFilm',
        ),
    ]
