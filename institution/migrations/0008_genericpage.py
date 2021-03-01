# Generated by Django 3.1.4 on 2021-02-15 21:22

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0007_sacreddates'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('text', tinymce.models.HTMLField()),
            ],
            options={
                'verbose_name': 'Página Genérica',
                'verbose_name_plural': 'Páginas Genéricas',
                'ordering': ['-id'],
            },
        ),
    ]