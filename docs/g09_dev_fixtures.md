
# To dump data

```
python manage.py dumpdata app.model_name --indent 4 > fixtures/file_name.json
```

# To load data

```
python manage.py loaddata fixtures/model_name.json --app app.model_name

or

python manage.py dumpdata --format=json glossary.GenreTag
```

# Example

```
[
  {"model": "glossary.aggregationtype",
    "pk": 1,
    "fields": {
      "created": "2018-08-01T18:34:28.932Z",
      "uuid": "c871fb41-51d6-4ab9-a222-328ea1a7bc6f",
      "title": "Conjunto",
      "slug": "1_conjunto",
      "description": "Agrupamento documentos"
      }
    },
]
