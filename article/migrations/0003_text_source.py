# Generated by Django 3.0.1 on 2020-03-03 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200303_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='source',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]