from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden
from django.shortcuts import render
from django.utils import timezone


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
