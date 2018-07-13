# Generated by Django 2.0.5 on 2018-07-13 20:29

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id_auto_series', models.BigAutoField(editable=False, help_text='Auto Increment ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='This is an auto set field', unique=True, verbose_name='Universal Unique Identifier')),
                ('id_human', models.CharField(blank=True, help_text='Institucional Identifier', max_length=64, null=True, unique=True, verbose_name='Institucional ID')),
                ('title', models.CharField(default='No title publication', help_text='Ex.: The complete photo collection of Sebastião Salgado.', max_length=256, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, help_text='Ex.: book-sebastiao-salgado', max_length=256, null=True, unique=True, verbose_name='Slug')),
                ('abstract', models.TextField(blank=True, help_text='Ex.: This publication is composed by...', null=True, verbose_name='Abstract')),
                ('full_text', models.TextField(blank=True, help_text='Ex.: The book serie is...', null=True, verbose_name='Full Text')),
                ('date_released', models.DateField(blank=True, help_text='Choose the released date', null=True, verbose_name='Released Date')),
                ('dimension', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Feed with information about dimensions', null=True, verbose_name='Dimensions')),
                ('pages', models.PositiveIntegerField(blank=True, help_text='Total number of pages', null=True, verbose_name='Number of pages')),
                ('other_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Other unstructured data of this publication', null=True, verbose_name='Other Data')),
                ('author', models.ManyToManyField(blank=True, help_text="Choose some collection's authors", related_name='personAuthor', to='person.Person', verbose_name='Authors')),
                ('publisher', models.ManyToManyField(blank=True, help_text="Choose some collection's authors", related_name='personPublisher', to='person.Person', verbose_name='Authors')),
            ],
            options={
                'verbose_name': 'Publication',
                'verbose_name_plural': 'Publications',
            },
        ),
        migrations.CreateModel(
            name='PublicationType',
            fields=[
                ('id_auto_series', models.BigAutoField(editable=False, help_text='Auto Increment ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='This is an auto set field', unique=True, verbose_name='Universal Unique Identifier')),
                ('title', models.CharField(help_text='Ex.: book', max_length=256, verbose_name='Title')),
                ('description', models.CharField(blank=True, help_text='Ex.: A book is...', max_length=512, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Publication Type',
                'verbose_name_plural': 'Publication Types',
            },
        ),
        migrations.AddField(
            model_name='publication',
            name='type',
            field=models.ForeignKey(blank=True, help_text='Choose the more appropriate type to means this publication', null=True, on_delete=django.db.models.deletion.SET_NULL, to='publication.PublicationType', verbose_name='Type'),
        ),
    ]