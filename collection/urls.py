# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
# project guia imports
from . import views


urlpatterns = [
    # path('<pk>/',
    #     views.ContainerDetail.as_view(),
    #     name='container_detail'),
    # path('slug/<slug:slug>/',
    #     views.ContainerDetail.as_view(),
    #     name='container_detail_slug'),
    path('',views.CollectionList.as_view(),name='collection'),
    path('<pk>/',views.CollectionDetail.as_view(),name='collection_detail'),
    path('<slug:slug>',views.CollectionDetail.as_view(),name='collection_detail_slug'),
]
