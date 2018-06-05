from django.conf import settings
from django.conf.urls.static import static

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'base.html')
