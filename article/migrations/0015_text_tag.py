# Generated by Django 2.2 on 2020-04-02 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_remove_text_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Tag'),
        ),
    ]
