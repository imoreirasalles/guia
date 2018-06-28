## Adding language translations

### 1. settings.py LANGUAGES

Add a new language in settings LANGUAGES var:

```
# Provide a lists of languages which your site supports.
LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
    ('pt-br', _('Portuguese - Brasilian')),
)
```

### 2. Default project language

In settings.py, find the LANGUAGE_CODE var and change the language:

```
# Set the default language for your site.
LANGUAGE_CODE = 'en'
```

### 3. Make Translation Files and Compile Messages

```
django-admin makemessages --locale=pt_BR
django-admin compilemessages --locale=pt_BR
```

## Adding new key:value translation into your code

### Import ugettext_lazy

```
from django.utils.translation import ugettext_lazy as _
```

### Add terms

```
_('Example of string translatable')
```

## Reference
* https://docs.djangoproject.com/en/2.0/topics/i18n/translation/
* https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-compilemessages
* https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/#overriding-the-default-fields
* https://github.com/deschler/django-modeltranslation
