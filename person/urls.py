# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# project guia imports
from . import views

urlpatterns = [
    path('', views.person, name='person'),
]
