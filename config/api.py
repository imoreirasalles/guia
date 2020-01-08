from rest_framework import routers
from vocabulary.api import views as vocabulary_views
from collection.api import views as collection_views
# from exhibition.api import views as exhibition_views
# from publication.api import views as publication_views


router = routers.DefaultRouter()
router.register(r'terms', vocabulary_views.TermViewset)
router.register(r'collections', collection_views.CollectionViewset)
# router.register(r'exhibition', exhibition_views.exhibitionViewset)
# router.register(r'publication', publication_views.publicationViewset)
