from django.conf import settings
from django.conf.urls.static import static
from django.utils import timezone

from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden
from django.views.generic import DetailView, ListView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required

from django.shortcuts import render


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')

def error404(request):
    return HttpResponseNotFound(render(request, '404.html'))

def error403(request):
    return HttpResponseForbidden(render(request, '403.html'))

def error500(request):
    return HttpResponseServerError(render(request, '500.html'))

def exhibition(request):
    return render(request, 'exhibition_list.html')


def publication(request):
    return render(request, 'publication_list.html')


class BaseDraftListView(ListView):
    def get_queryset(self):
        return self.model.objects.published()


class BaseDraftDetailView(DetailView):
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.is_draft:
            raise Http404(_('Page not found'))
        return obj
