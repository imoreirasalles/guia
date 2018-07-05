## New Model Routine

0. Get the model.py file into an being app
1. Create the main class
1.1 Apply docstring, string default function, verbose_name and verbose_name_plural

```
class MyModelName(models.Model):
    """My docstring explaning what this class do"""
    field1 = typeField(condition1, condition2),
    field2 = typeField(condition1, condition2),
    field3 = typeField(ForeignKey, conditions),
    field4 = typeField(ManyToManyField, condition2),

        def __str__(self):
            return self.field1

        class Meta:
            verbose_name = _('My Verbose Name')
            verbose_name_plural = _('My Plural Verbose Name')
```

1.2 Dont forget the translation engine at the top of imports, if necessary

```
from django.utils.translation import gettext_lazy as _
```

2. Create and apply migrations

With you env active, for example:

```
python manage.py makemigrations
python manage.py migrate
```

3. Register the new model into django panel (admin.py)

Very short simple way:

```
admin.site.register(MyModelName)
```

With a class and optional features:

```
@admin.register(MyModelName)
class MyModelNameAdmin(admin.ModelAdmin):
  # this set fields just for ready only
  readonly_fields = ['field1']
  # this set field for listing into dashboard django panel
  list_display = ('field1', 'field2')
```

4. Make translations

4.1 First, make up and get new terms

```
django-admin makemessages --locale=pt_BR
```

4.2 Second, open your locale file (`django.po`) and translate

```
#: MyApp/models.py:65
msgid "My Label"
msgstr "Minha Etiqueta"
```


4.3 Finaly, compile your translations to generate `django.mo`

```
django-admin compilemessages --locale=pt_BR
```
