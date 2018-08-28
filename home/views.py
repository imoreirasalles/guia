# core django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

# Project guia imports
from .models import *


class PostList(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "home.html"
