# Generated by Django 4.2 on 2023-05-18 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_rename_src_thumb_thumb_src_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='included',
            field=models.BooleanField(default=True),
        ),
    ]