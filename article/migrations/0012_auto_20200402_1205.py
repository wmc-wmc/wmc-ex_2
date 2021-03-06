# Generated by Django 2.2 on 2020-04-02 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20200402_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Tag'),
        ),
        migrations.AlterField(
            model_name='text',
            name='subject',
            field=models.CharField(max_length=255),
        ),
    ]
