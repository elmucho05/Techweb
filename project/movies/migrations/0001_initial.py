# Generated by Django 4.2 on 2023-04-13 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
    ]