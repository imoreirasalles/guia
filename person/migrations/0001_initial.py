# Generated by Django 2.0.6 on 2018-06-22 20:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nickname', models.CharField(blank=True, max_length=128, null=True)),
                ('slug', models.SlugField(blank=True, max_length=256, null=True, unique=True)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('full_text', models.TextField(blank=True, null=True)),
                ('date_start', models.DateTimeField(blank=True, null=True)),
                ('date_end', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
