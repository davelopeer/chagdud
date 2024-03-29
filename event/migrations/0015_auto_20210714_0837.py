# Generated by Django 3.1.4 on 2021-07-14 08:37

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0014_auto_20210524_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='description',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='name_en',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='participation_text',
            new_name='participation_text_en',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='policies',
            new_name='participation_text_es',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='place',
            new_name='place_en',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='requirements',
            new_name='requirements_en',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='short_description',
            new_name='short_description_en',
        ),
        migrations.AddField(
            model_name='event',
            name='description_es',
            field=models.TextField(default='', max_length=20000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='description_pt',
            field=models.TextField(default='', max_length=20000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='name_es',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='name_pt',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='participation_text_pt',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='place_es',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='place_pt',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='policies_en',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='policies_es',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='policies_pt',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='requirements_es',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='requirements_pt',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='short_description_es',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='short_description_pt',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
