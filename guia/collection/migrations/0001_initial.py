# Generated by Django 2.2.7 on 2019-12-23 00:59

import ckeditor.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vocabulary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
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
                ('article', ckeditor.fields.RichTextField(blank=True, help_text='Full description', null=True, verbose_name='Article')),
                ('start_date', models.DateField(blank=True, help_text='Choose a start date', null=True, verbose_name='Initial Date')),
                ('end_date', models.DateField(blank=True, help_text='Choose an final date', null=True, verbose_name='Final date')),
                ('dimention_items', models.PositiveIntegerField(blank=True, help_text='Total collection items', null=True, verbose_name='Total of items')),
                ('progressbar_work', models.PositiveIntegerField(blank=True, help_text='Percentage of work done', null=True, verbose_name='Work progress bar')),
                ('progressbar_online', models.PositiveIntegerField(blank=True, help_text='Percentage of work available online', null=True, verbose_name='Online progress bar')),
                ('inventory_status', models.NullBooleanField(help_text='This collection has any inventory?', verbose_name='Inventory')),
                ('inventory_start_date', models.DateField(blank=True, help_text='When the inventory beggins?', null=True, verbose_name='Inventory start date')),
                ('inventory_end_date', models.DateField(blank=True, help_text='When the inventory ends?', null=True, verbose_name='Inventory end date')),
                ('insurance_status', models.NullBooleanField(help_text='This collection has any insurance?', verbose_name='Insurance')),
                ('insurance_start_date', models.DateField(blank=True, help_text='When the insurance beggins?', null=True, verbose_name='Insurance start date')),
                ('insurance_end_date', models.DateField(blank=True, help_text='When the insurance ends?', null=True, verbose_name='Insurance end date')),
                ('contract_status', models.NullBooleanField(help_text='This collection has any contract?', verbose_name='Contract')),
                ('contract_start_date', models.DateField(blank=True, help_text='When the contract beggins?', null=True, verbose_name='Contract start date')),
                ('contract_end_date', models.DateField(blank=True, help_text='When the contract ends?', null=True, verbose_name='Contract end date')),
                ('aggregation_type', models.ManyToManyField(blank=True, help_text='Select the terms used in this vocabulary', limit_choices_to={'vocabularies__id_human': 'aggregation_type'}, related_name='aggregation_types', to='vocabulary.Term', verbose_name='Aggregation Type')),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
            },
        ),
    ]
