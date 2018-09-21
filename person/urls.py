# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# project guia imports
from . import views

urlpatterns = [
    path('', views.PersonListView.as_view(), name='person'),
    path('<pk>/', views.PersonDetailView.as_view(), name='person_detail'),
    path('<slug:slug>', views.PersonDetailView.as_view(), name='person_detail_slug'),
]
