# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="publication/publication_list.html"), name='publication_list'),
    path('detail/', TemplateView.as_view(template_name="publication/publication_detail.html"), name='publication_detail'),
    path('edit/',  TemplateView.as_view(template_name="publication/publication_form.html"), name='publication_form'),

]
