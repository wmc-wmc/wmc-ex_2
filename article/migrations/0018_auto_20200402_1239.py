# Generated by Django 2.2 on 2020-04-02 12:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0017_commet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commet',
            new_name='Comment',
        ),
    ]