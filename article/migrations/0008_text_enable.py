# Generated by Django 2.2 on 2020-03-26 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='enable',
            field=models.BooleanField(default=True),
        ),
    ]