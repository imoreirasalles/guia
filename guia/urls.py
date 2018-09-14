# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.utils.translation import gettext_lazy as _

# project guia imports
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('base/', views.base, name='base'),
    path('notfound404/', views.notfound404, name='notfound404'),
    path('', include('home.urls'), name='home'),
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
