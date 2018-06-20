# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# project guia imports
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('froala_editor/', include('froala_editor.urls')),
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('collection/', views.CollectionList.as_view(), name='collection'),
    path('collection/<slug:slug>/', views.CollectionDetail.as_view(), name='collection_detail'),
    path('exhibition/', views.exhibition, name='exhibition'),
    path('publication/', views.publication, name='publication'),
    path('person/', include('person.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
