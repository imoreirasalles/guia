# Generated by Django 2.2.7 on 2019-12-13 20:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='article',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Full description', null=True, verbose_name='Article'),
        ),
    ]
