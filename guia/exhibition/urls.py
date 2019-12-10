# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="exhibition/exhibition_list.html"), name='exhibition_list'),
    path('detail/', TemplateView.as_view(template_name="exhibition/exhibition_detail.html"), name='exhibition_detail'),
    path('edit/',  TemplateView.as_view(template_name="exhibition/exhibition_form.html"), name='exhibition_form'),

]
