# Generated by Django 4.2 on 2023-05-02 12:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_episode'),
        ('profile', '0006_alter_userrating_rating'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserRating',
            new_name='UserReview',
        ),
    ]
