# Generated by Django 2.0.5 on 2018-06-29 22:22

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_auto_20180628_1909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accesscondition',
            options={'verbose_name': 'access condition', 'verbose_name_plural': 'access conditions'},
        ),
        migrations.AlterModelOptions(
            name='aggregationtype',
            options={'verbose_name': 'Aggregation Type', 'verbose_name_plural': 'Aggregations Type'},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'verbose_name': 'collection', 'verbose_name_plural': 'collections'},
        ),
        migrations.AlterModelOptions(
            name='descriptionlevel',
            options={'verbose_name': 'Description level', 'verbose_name_plural': 'Description levels'},
        ),
        migrations.AlterModelOptions(
            name='genretag',
            options={'verbose_name': 'genre tag', 'verbose_name_plural': 'genre tags'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'item', 'verbose_name_plural': 'items'},
        ),
        migrations.AlterModelOptions(
            name='sets',
            options={'verbose_name': 'container', 'verbose_name_plural': 'containers'},
        ),
        migrations.AlterModelOptions(
            name='thumbnail',
            options={'verbose_name': 'thumbnail', 'verbose_name_plural': 'thumbnails'},
        ),
        migrations.RemoveField(
            model_name='collection',
            name='dimension',
        ),
        migrations.RemoveField(
            model_name='sets',
            name='abstract',
        ),
        migrations.AddField(
            model_name='collection',
            name='dimensions',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='feed with information about dimensions', null=True, verbose_name='dimensions'),
        ),
        migrations.AddField(
            model_name='sets',
            name='description',
            field=models.TextField(blank=True, help_text='ex.: this container is...', null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='accesscondition',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='auto set field', verbose_name='created in'),
        ),
        migrations.AlterField(
            model_name='accesscondition',
            name='description',
            field=models.TextField(blank=True, help_text='ex.: Some documents here have copyright...', null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='accesscondition',
            name='title_long',
            field=models.CharField(blank=True, help_text='ex.: Partial - copyright', max_length=128, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='accesscondition',
            name='title_short',
            field=models.CharField(blank=True, help_text='ex.: Full Free, Partial, Retricted', max_length=64, verbose_name='access'),
        ),
        migrations.AlterField(
            model_name='aggregationtype',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='auto set field', verbose_name='Created in'),
        ),
        migrations.AlterField(
            model_name='aggregationtype',
            name='description',
            field=models.CharField(blank=True, help_text='ex.: the collection is a group of...', max_length=512, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='aggregationtype',
            name='title',
            field=models.CharField(blank=True, help_text='ex.: collection, archive, etc', max_length=256, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='abstract',
            field=models.TextField(blank=True, help_text='ex.: this collection is composed by...', null=True, verbose_name='abstract'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='access_condition',
            field=models.ForeignKey(blank=True, help_text='choose the more appropriate access condition to this collection', null=True, on_delete=django.db.models.deletion.SET_NULL, to='collection.AccessCondition', verbose_name='access condition'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='access_link',
            field=models.URLField(blank=True, help_text='do you have some online link access to this collection?', null=True, verbose_name='access link'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='access_local_status',
            field=models.NullBooleanField(help_text='local access status', verbose_name='is there any local access to the collection?'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='access_online_status',
            field=models.NullBooleanField(help_text='is there any online access to the collection?', verbose_name='online access status'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='aggregation_type',
            field=models.ForeignKey(blank=True, help_text='choose an option', null=True, on_delete=django.db.models.deletion.SET_NULL, to='collection.AggregationType', verbose_name='aggregation type'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='author',
            field=models.ManyToManyField(blank=True, help_text="choose some collection's authors", to='person.Person', verbose_name='authors'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='auto set field', verbose_name='created in'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='date_end',
            field=models.DateTimeField(blank=True, help_text='choose an final date', null=True, verbose_name='final date'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='date_end_caption',
            field=models.CharField(blank=True, help_text='choose a final date caption', max_length=64, null=True, verbose_name='final date caption'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='date_start',
            field=models.DateTimeField(blank=True, help_text='choose a start date', null=True, verbose_name='initial date'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='date_start_caption',
            field=models.CharField(blank=True, help_text='choose a start date caption', max_length=64, null=True, verbose_name='initial date caption'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='description_level',
            field=models.ForeignKey(blank=True, help_text='choose an option', null=True, on_delete=django.db.models.deletion.SET_NULL, to='collection.DescriptionLevel', verbose_name='description level'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='fulltext',
            field=models.TextField(blank=True, help_text='ex.: All itens in this collection...', null=True, verbose_name='full text'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='genre_tags',
            field=models.ForeignKey(blank=True, help_text='choose one or more options', null=True, on_delete=django.db.models.deletion.SET_NULL, to='collection.GenreTag', verbose_name='genre tags'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='id',
            field=models.CharField(blank=True, help_text='institucional collection human identifier', max_length=64, null=True, unique=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='id_old',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='legacy identifiers', null=True, verbose_name='old ids'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='inventary_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='several data about the inventary', null=True, verbose_name='inventary data'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='inventary_last_date',
            field=models.DateField(blank=True, help_text='what is the inventary last date?', null=True, verbose_name='inventary last date'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='inventary_status',
            field=models.NullBooleanField(help_text='is there any inventary to this collection?', verbose_name='inventary status'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='items',
            field=models.ManyToManyField(blank=True, help_text='choose some items that compose this collection. ATTENTION: You can create a container and aggregate items there', to='collection.Item', verbose_name='items'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='items_online',
            field=models.PositiveIntegerField(blank=True, help_text='total online collection items', null=True, verbose_name='online items'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='items_processed',
            field=models.PositiveIntegerField(blank=True, help_text='total processed items', null=True, verbose_name='processed items'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='items_total',
            field=models.PositiveIntegerField(blank=True, help_text='total collection items', null=True, verbose_name='total items'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='location_generic',
            field=models.ManyToManyField(blank=True, help_text='what is the generic location to the collection?', to='location.Location', verbose_name='generic location'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='location_specific',
            field=models.CharField(blank=True, help_text='what is the specific location to this collection?', max_length=256, verbose_name='specific location'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='management_unit',
            field=models.ManyToManyField(blank=True, help_text='what is the management unit concerning to this collection?', to='management.ManagementUnit', verbose_name='management unit'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='other_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='other unstructured data of this collection', null=True, verbose_name='other data'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='sets',
            field=models.ManyToManyField(blank=True, help_text='choose containers that compose the collection', to='collection.Sets', verbose_name='containers'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='slug',
            field=models.SlugField(blank=True, help_text='ex.: complete-collection-sebastiao-salgado', max_length=256, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='thumbnail',
            field=models.ManyToManyField(blank=True, help_text='choose some introduction and representative images', to='collection.Thumbnail', verbose_name='thumbnails'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='title',
            field=models.CharField(blank=True, help_text='the complete photo collection of Sebastião Salgado', max_length=256, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='auto set field', primary_key=True, serialize=False, unique=True, verbose_name='universally unique identifier'),
        ),
        migrations.AlterField(
            model_name='descriptionlevel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='auto set field', verbose_name='created in'),
        ),
        migrations.AlterField(
            model_name='descriptionlevel',
            name='description',
            field=models.CharField(blank=True, help_text='the description of level type...', max_length=512, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='descriptionlevel',
            name='title',
            field=models.CharField(blank=True, help_text='ex.: basic - 0', max_length=256, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='genretag',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='auto set field', verbose_name='created in'),
        ),
        migrations.AlterField(
            model_name='genretag',
            name='title',
            field=models.CharField(blank=True, help_text='ex.: photo, picture, draw, etc', max_length=256, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='item',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='auto set field', verbose_name='created in'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, help_text='ex.: gelatin negative of the first photo...', null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.CharField(blank=True, help_text='institucional human identifier', max_length=64, null=True, unique=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(blank=True, help_text='ex.: Salgado Negative - 001', max_length=256, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='item',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='auto set field', primary_key=True, serialize=False, unique=True, verbose_name='universally unique identifier'),
        ),
        migrations.AlterField(
            model_name='sets',
            name='aggregation_type',
            field=models.ForeignKey(blank=True, help_text='container aggregation type', null=True, on_delete=django.db.models.deletion.SET_NULL, to='collection.AggregationType', verbose_name='aggregation type'),
        ),
        migrations.AlterField(
            model_name='sets',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='auto set field', verbose_name='created in'),
        ),
        migrations.AlterField(
            model_name='sets',
            name='description_level',
            field=models.ForeignKey(blank=True, help_text='choose a description level to this container', null=True, on_delete=django.db.models.deletion.SET_NULL, to='collection.DescriptionLevel', verbose_name='description level'),
        ),
        migrations.AlterField(
            model_name='sets',
            name='id',
            field=models.CharField(blank=True, help_text='institucional container human identifier', max_length=64, null=True, unique=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='sets',
            name='items',
            field=models.ManyToManyField(blank=True, help_text='itens that composes the container', to='collection.Item', verbose_name='items'),
        ),
        migrations.AlterField(
            model_name='sets',
            name='sets_child',
            field=models.ForeignKey(blank=True, help_text='choose child containers to aggregate to this one', null=True, on_delete=django.db.models.deletion.SET_NULL, to='collection.Sets', verbose_name='child containers'),
        ),
        migrations.AlterField(
            model_name='sets',
            name='title',
            field=models.CharField(blank=True, help_text='ex.: container of...', max_length=256, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='sets',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='auto set field', primary_key=True, serialize=False, unique=True, verbose_name='universally unique identifier'),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='auto set field', verbose_name='created in'),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='image',
            field=models.ImageField(blank=True, help_text='ex.: image file', null=True, upload_to='', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='title',
            field=models.CharField(blank=True, help_text='ex.: image title, like "the photographer resting" ', max_length=256, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='auto set field', primary_key=True, serialize=False, unique=True, verbose_name='universally unique identifier'),
        ),
    ]