# core django imports
from django.contrib.auth import get_user_model, authenticate, login as login_django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import CreateView, TemplateView

# Project guia imports
from home.models import Post
from collection.models import Collection
from exhibition.models import Exhibition
from publication.models import Publication
from event.models import Event
from person.models import Person

from .forms import UserForm

User = get_user_model()


def login(request):
    return render(request, 'login.html')


class PostList(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['collection_total'] = Collection.objects.all().count()
        if (Post.objects.order_by('id_auto_series').exists()):
            post = Post.objects.latest('capture')
            context['first_image_id'] = post.capture.first().id_auto_series
            image_list = [str(index) for index in range(post.capture.count())]
            context['image_list'] = image_list
        else:
            context['first_active_image'] = ''

        return context

    def collection_total(self):
        collection_total = Collection.objects.published().count()
        return collection_total

    def exhibition_total(self):
        exhibition_total = Exhibition.objects.published().count()
        return exhibition_total

    def publication_total(self):
        publication_total = Publication.objects.published().count()
        return publication_total

    def event_total(self):
        event_total = Event.objects.published().count()
        return event_total

    def person_total(self):
        person_total = Person.objects.published().count()
        return person_total


class UserCreateView(CreateView):
    form_class = UserForm
    model = User
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        authenticated_user = authenticate(
            self.request,
            username=user.username,
            password=form.cleaned_data['password']
        )
        login_django(self.request, authenticated_user)
        return redirect('home')
