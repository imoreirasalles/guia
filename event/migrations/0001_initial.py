# Generated by Django 2.0.5 on 2018-07-14 21:35

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id_auto_series', models.BigAutoField(editable=False, help_text='Auto Increment ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='This is an auto set field', unique=True, verbose_name='Universal Unique Identifier')),
                ('id_human', models.CharField(blank=True, help_text='Institucional Identifier', max_length=64, null=True, unique=True, verbose_name='Institucional ID')),
                ('title', models.CharField(help_text='Ex.: Launch of new publication...', max_length=256, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, help_text='Ex.: lauch-new-publication', max_length=256, null=True, unique=True, verbose_name='Slug')),
                ('date_start', models.DateField(blank=True, help_text='Choose a start date', null=True, verbose_name='Initial Date')),
                ('date_end', models.DateField(blank=True, help_text='Choose an final date', null=True, verbose_name='Final date')),
                ('abstract', models.TextField(blank=True, help_text='Ex.: This event was performed by...', null=True, verbose_name='Abstract')),
                ('full_text', models.TextField(blank=True, help_text='Ex.: The course was...', null=True, verbose_name='Full Text')),
                ('team', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Feed with information about team that worked on this', null=True, verbose_name='Team')),
                ('other_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Other unstructured data of this collection', null=True, verbose_name='Other Data')),
                ('location', models.ForeignKey(blank=True, help_text='Choose the location where this event occurs', null=True, on_delete=django.db.models.deletion.SET_NULL, to='location.Location', verbose_name='Location')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id_auto_series', models.BigAutoField(editable=False, help_text='Auto Increment ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='This is an auto set field', unique=True, verbose_name='Universal Unique Identifier')),
                ('title', models.CharField(help_text='Ex.: course, workshop, show, launching', max_length=256, verbose_name='Title')),
                ('description', models.CharField(blank=True, help_text='Ex.: A course is a formative event... ', max_length=512, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Event Type',
                'verbose_name_plural': 'Events Type',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(blank=True, help_text='Choose the an appropriate type to this one', null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.EventType', verbose_name='Type'),
        ),
    ]
