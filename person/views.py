# core django imports
from django.shortcuts import render
from django.http import HttpResponse


def person(request):
    return render(request, 'person.html')
