# core django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

# Project guia imports
from .models import *


def login(request):
    return render(request, 'login.html')


class PostList(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if (Post.objects.order_by('id_auto_series').exists()):
            post = Post.objects.latest('capture')
            context['first_image_id'] = post.capture.first().id_auto_series
            image_list = [str(index) for index in range(post.capture.count())]
            context['image_list'] = image_list
        else:
            context['first_active_image'] = ''

        return context
