# Generated by Django 4.2.3 on 2023-07-08 17:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote', '0003_candidates_votecandidates'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='voteCandidates',
            new_name='votes_candidate',
        ),
    ]