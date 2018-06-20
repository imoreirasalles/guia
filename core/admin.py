from django.contrib import admin
from django import forms
from .models import *



# From postgres
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget

# From Django Admin Hstore widget
from django_admin_hstore_widget.forms import HStoreFormField
