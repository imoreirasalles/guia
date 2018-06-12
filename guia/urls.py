from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('froala_editor/', include('froala_editor.urls')),
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('collection/', views.collection, name='collection'),
    path('exhibition/', views.exhibition, name='exhibition'),
    path('publication/', views.publication, name='publication'),
    path('person/', views.person, name='person'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
