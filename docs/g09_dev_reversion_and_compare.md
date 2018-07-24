## Django Reversion

Ref.: https://github.com/etianen/django-reversion

## [reversion] How to use into `models.py`?

```
import reversion

@reversion.register()
class YourModel(models.Model):

    pass
```

## [reversion] How to use into `admin.py`?

```
from reversion.admin import VersionAdmin

@admin.register(YourModel)
class YourModelAdmin(VersionAdmin):

    pass
```

## Compare
Ref.: https://github.com/jedie/django-reversion-compare

### [compare] How to use into `admin.py`

Inherit from `CompareVersionAdmin` instead of VersionAdmin to get the comparison feature.

admin.py e.g.:

```
from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin

from my_app.models import ExampleModel

class ExampleModelAdmin(CompareVersionAdmin):
    pass

admin.site.register(ExampleModel, ExampleModelAdmin)
```
