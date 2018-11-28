# Generated by Django 2.0.5 on 2018-11-28 02:14

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('digitalassetsmanagement', '0009_auto_20181022_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id_auto_series', models.BigAutoField(editable=False, help_text='Auto Increment ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now, help_text='Auto set field', verbose_name='Created in')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='This is an auto set field', unique=True, verbose_name='Universal Unique Identifier')),
                ('title', models.CharField(blank=True, default=None, help_text='Ex.: The title of this record', max_length=256, null=True, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, default=None, help_text='Ex.: complete-collection-sebastiao-salgado', max_length=256, null=True, unique=True, verbose_name='Slug')),
                ('file', models.FileField(upload_to='', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='capture',
            field=models.ManyToManyField(blank=True, help_text='Image(s) taked from this item.', to='digitalassetsmanagement.Capture', verbose_name='Image(s)'),
        ),
    ]
