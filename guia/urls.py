# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _

# project guia imports
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('collection/', include('collection.urls')),
    path('exhibition/', views.exhibition, name='exhibition'),
    path('publication/', views.publication, name='publication'),
    path('person/', include('person.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# default: "Django Administration"
admin.site.site_header = _('My Project')

# default: "Site administration"
admin.site.index_title = _('Input and Admin Data')

# default: "Django site admin"
admin.site.site_title = _('Admin Panel')
