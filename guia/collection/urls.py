# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.CollectionList.as_view(), name='collection_list'),
    path('<slug:slug>/', views.CollectionDetail.as_view(), name='collection_detail'),
    path('<slug:slug>/edit/',  TemplateView.as_view(template_name="collection/collection_form.html"), name='collection_form'),

]
