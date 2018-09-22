# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
# project guia imports
from . import views


urlpatterns = [
    path('',views.PublicationListView.as_view(),name='publication'),
    path('<pk>/',views.PublicationDetailView.as_view(),name='publication_detail'),
    path('<slug:slug>',views.PublicationDetailView.as_view(),name='publication_detail_slug'),
]
