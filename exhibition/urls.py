# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
# project guia imports
from . import views


urlpatterns = [
    path('',views.ExhibitionListView.as_view(),name='exhibition'),
    path('<pk>/',views.ExhibitionDetailView.as_view(),name='exhibition_detail'),
    path('<slug:slug>',views.ExhibitionDetailView.as_view(),name='exhibition_detail_slug'),
]
