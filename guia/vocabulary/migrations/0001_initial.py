# Generated by Django 2.2.7 on 2019-12-23 03:12

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(editable=False, help_text='Sequential identifier', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Universal unique identifier', unique=True, verbose_name='UUID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Date this resource was created', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Date this resource was last updated', verbose_name='Updated at')),
                ('label', models.CharField(default=None, help_text='Short title for this resource', max_length=128, null=True, verbose_name='Label')),
                ('summary', models.TextField(blank=True, default=None, help_text='Brief description', max_length=512, null=True, verbose_name='Summary')),
                ('published', models.BooleanField(db_index=True, default=False, help_text='This resource is available to the public', verbose_name='Published')),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Semi-structured data in JSON', null=True, verbose_name='Extra')),
                ('slug', models.SlugField(blank=True, default=None, editable=False, help_text='String presented as part of the URL', max_length=128, null=True, unique=True, verbose_name='Slug')),
                ('id_human', models.CharField(blank=True, default=None, help_text='Human readable identifier', max_length=32, null=True, verbose_name='Identifier')),
                ('semantic_url', models.URLField(blank=True, default=None, help_text='https://www.wikidata.org/wiki/Q3180571', null=True, verbose_name='Semantic URL')),
            ],
            options={
                'verbose_name': 'Term',
                'verbose_name_plural': 'Terms',
            },
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.BigAutoField(editable=False, help_text='Sequential identifier', primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Universal unique identifier', unique=True, verbose_name='UUID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Date this resource was created', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Date this resource was last updated', verbose_name='Updated at')),
                ('label', models.CharField(default=None, help_text='Short title for this resource', max_length=128, null=True, verbose_name='Label')),
                ('summary', models.TextField(blank=True, default=None, help_text='Brief description', max_length=512, null=True, verbose_name='Summary')),
                ('published', models.BooleanField(db_index=True, default=False, help_text='This resource is available to the public', verbose_name='Published')),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Semi-structured data in JSON', null=True, verbose_name='Extra')),
                ('slug', models.SlugField(blank=True, default=None, editable=False, help_text='String presented as part of the URL', max_length=128, null=True, unique=True, verbose_name='Slug')),
                ('id_human', models.CharField(blank=True, default=None, help_text='Human readable identifier', max_length=32, null=True, verbose_name='Identifier')),
                ('semantic_url', models.URLField(blank=True, default=None, help_text='https://www.wikidata.org/wiki/Q3180571', null=True, verbose_name='Semantic URL')),
                ('terms', models.ManyToManyField(blank=True, help_text='Select the terms used in this vocabulary', related_name='vocabularies', to='vocabulary.Term', verbose_name='Terms')),
            ],
            options={
                'verbose_name': 'Vocabulary',
                'verbose_name_plural': 'Vocabularies',
            },
        ),
    ]
