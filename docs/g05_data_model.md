## Adopted References
* Django Default Fields https://docs.djangoproject.com/en/2.0/ref/models/fields/
* Django Geo Field https://docs.djangoproject.com/en/2.0/ref/contrib/gis/model-api/


## Declined References
* Django Hash Field
https://github.com/amcat/django-hash-field (It is not necessary, there is a native hash uuid field on django)

* Django Hstore Third part
http://django-hstore.readthedocs.io/en/latest/ (Project with no suport any more. Take a look on issue 161. It was solved with native hstore django field and hstore widget)

* Django Hstore Native
https://docs.djangoproject.com/en/2.0/ref/contrib/postgres/fields/#django.contrib.postgres.fields.HStoreField

* Hstore Widget
https://github.com/PokaInc/django-admin-hstore-widget

* Django Json Field
* Django Json Widget - https://github.com/jmrivas86/django-json-widget, https://pypi.org/project/django-json-widget (It could be useful on future, but at moment we are using hstore)
* Django Pretty Json http://kevinmickey.github.io/django-prettyjson (Good for programmers and geeks, bad to all others)


Experimentar:
https://github.com/tooreht/django-jsonsuit
https://github.com/mbraak/django-mptt-admin
https://github.com/mbi/django-rosetta
