# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
# project guia imports
from . import views


urlpatterns = [
    path('',views.CollectionListView.as_view(),name='collection'),
    path('<pk>/',views.CollectionDetailView.as_view(),name='collection_detail'),
    path('<slug:slug>',views.CollectionDetailView.as_view(),name='collection_detail_slug'),
    path('collection_search/',views.CollectionSearchListView.as_view(),name='blog_search_list_view'),
]
