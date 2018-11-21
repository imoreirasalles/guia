# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.utils.translation import gettext_lazy as _

# project guia imports
from . import views

from exhibition.views import ExhibitionListView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', auth_views.login, name='login'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot-password'),
    path('forgot-password/success/', views.ForgotPasswordSuccessView.as_view(), name='forgot-password-success'),
    path('logout/', auth_views.logout, name='logout'),
    path('base/', views.base, name='base'),
    path('error404/', views.error404, name='error404'),
    path('error403/', views.error403, name='error403'),
    path('error500/', views.error500, name='error500'),
    path('', include('home.urls'), name='home'),
    path('collection/', include('collection.urls')),
    path('exhibition/', include('exhibition.urls')),
    path('publication/', include('publication.urls')),
    path('person/', include('person.urls')),
    path('event/', include('event.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# default: "Django Administration"
admin.site.site_header = _('My Project')

# default: "Site administration"
admin.site.index_title = _('Input and Admin Data')

# default: "Django site admin"
admin.site.site_title = _('Admin Panel')


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
