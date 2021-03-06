# Generated by Django 2.0.5 on 2018-07-14 21:35

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('digitalassetsmanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id_auto_series', models.BigAutoField(editable=False, help_text='Auto Increment ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='This is an auto set field', unique=True, verbose_name='Universal Unique Identifier')),
                ('id_human', models.CharField(blank=True, help_text='Institucional Identifier', max_length=64, null=True, unique=True, verbose_name='Institucional ID')),
                ('person_type', models.CharField(blank=True, help_text='Choose the more appropriate option', max_length=32, null=True, verbose_name='Person Type')),
                ('title', models.CharField(help_text='Ex.: Mr. Louis-Jacques-Mandé Daguerre', max_length=256, verbose_name='Title')),
                ('title_index', models.CharField(blank=True, help_text='Ex.: DAGUERRE, Louis-Jacques-Mandé.', max_length=256, null=True, verbose_name='Title Index')),
                ('is_staff', models.NullBooleanField(help_text='This person is a staff member?', verbose_name='Staff Member')),
                ('is_partner', models.NullBooleanField(help_text='This person is an institucional partner?', verbose_name='Institutional Partner')),
                ('is_feature', models.NullBooleanField(help_text='This is a featured person?', verbose_name='Staff Member')),
                ('gender', models.CharField(blank=True, help_text='Biological sex gender', max_length=1, null=True, verbose_name='Gender')),
                ('slug', models.SlugField(blank=True, help_text='Ex.: the-photographer-sebastiao-salgado', max_length=256, null=True, unique=True, verbose_name='Slug')),
                ('abstract', models.TextField(blank=True, help_text='Ex.: This person is...', null=True, verbose_name='Abstract')),
                ('full_text', models.TextField(blank=True, help_text='Ex.: The photographer...', null=True, verbose_name='Full Text')),
                ('date_start', models.DateField(blank=True, help_text='Choose a start date', null=True, verbose_name='Initial Date')),
                ('date_end', models.DateField(blank=True, help_text='Choose an final date', null=True, verbose_name='Final date')),
                ('url', models.URLField(blank=True, help_text='Representative URL about this person', null=True, verbose_name='URL')),
                ('linked_open_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Ex.: VIAF, ULAN, Wiki Data, etc', null=True, verbose_name='Linked Open Data Dictionary')),
                ('thumbnail', models.ManyToManyField(blank=True, help_text='Choose some introduction and representative images', to='digitalassetsmanagement.Thumbnail', verbose_name='Thumbnails')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
        ),
    ]
