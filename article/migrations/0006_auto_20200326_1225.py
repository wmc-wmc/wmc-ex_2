# Generated by Django 2.2 on 2020-03-26 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_text_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='image',
            field=models.ImageField(upload_to='static/image/'),
        ),
    ]