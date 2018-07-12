## Models

```
import reversion

@reversion.register()
class YourModel(models.Model):

    pass
```

## Admin

```
from reversion.admin import VersionAdmin

@admin.register(YourModel)
class YourModelAdmin(VersionAdmin):

    pass
```
