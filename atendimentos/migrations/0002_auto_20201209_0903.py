# Generated by Django 2.2.17 on 2020-12-09 12:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('atendimentos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dados',
            new_name='Dado',
        ),
    ]
