# Generated by Django 3.1.4 on 2021-01-24 18:12

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20210117_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='policies',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
    ]
