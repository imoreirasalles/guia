# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
# project guia imports
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('signup/', views.UserCreateView.as_view(), name='signup'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
