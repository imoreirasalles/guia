# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
# project guia imports
from . import views


urlpatterns = [
    path('',views.PublicationList.as_view(),
        name='publication'),
    # path('<pk>/',views.PublicationDetail.as_view(),
    #     name='publication_detail'),
    # path('<slug:slug>',views.PublicationDetail.as_view(),
    #     name='publication_detail_slug'),
]
