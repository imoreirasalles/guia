# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
# project guia imports
from . import views


urlpatterns = [
    path('', views.CollectionList.as_view(), name='collection'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.CollectionDetail.as_view(), name='collection_detail'),
]
