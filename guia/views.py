from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import render


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')
