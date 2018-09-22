# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
# project guia imports
from . import views


urlpatterns = [
    path('',views.EventListView.as_view(),name='event'),
    path('<pk>/',views.EventDetailView.as_view(),name='event_detail'),
    path('<slug:slug>',views.EventDetailView.as_view(),name='event_detail_slug'),
]
