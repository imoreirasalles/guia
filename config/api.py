from rest_framework import routers
from collection.api import views as collection_views
from vocabulary.api import views as vocabulary_views


router = routers.DefaultRouter()
router.register(r'collections', collection_views.CollectionViewset)
#router.register(r'terms', vocabulary_views.TermViewset)
