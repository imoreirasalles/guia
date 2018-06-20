from django.conf import settings
from django.conf.urls.static import static
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from core.models import *
from django.http import HttpResponse
from django.shortcuts import render


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


def exhibition(request):
    return render(request, 'exhibition.html')


def publication(request):
    return render(request, 'publication.html')


# def person(request):
#     return render(request, 'person.html')
