# core django imports
from django.conf import settings
from django.core import signing
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model, authenticate, login as login_django
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, FormView, ListView, TemplateView, UpdateView

# Project guia imports
from home.models import Post
from collection.models import Collection
from exhibition.models import Exhibition
from publication.models import Publication
from event.models import Event
from person.models import Person

from .forms import ForgotPasswordForm, ResetPasswordForm, UserForm


User = get_user_model()


class PostList(ListView):
    context_object_name = "post_list"
    template_name = "home.html"

    def get_queryset(self):
        return Post.objects.all().order_by('-created')[0:1]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = context['object_list']
        if posts:
            context['first_image_id'] = posts[0].capture.first().id_auto_series
            image_list = [str(index) for index in range(posts[0].capture.count())]
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


class ForgotPasswordView(FormView):
    form_class = ForgotPasswordForm
    template_name = 'forgot_password.html'

    def form_valid(self, form):
        user = form.cleaned_data['username']
        self.sendmail(user)
        return redirect('forgot-password-success')

    def sendmail(self, user):
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = user.email
        data = {
            'id': user.id,
            'last_login': '',
        }
        if user.last_login:
            data['last_login'] = user.last_login.strftime('%Y-%m-%d %H:%M:%S')

        link = reverse('reset-password-form', kwargs={'token': signing.dumps(data)})

        html_content = _('''
        Follow the link to update your password in the IMS Guide: <a href="{base_url}{link}">click here</a>.<br>
        If you did not request a password change, disregard this email.<br><br>
        IMS Guide.
        ''').format(base_url=settings.BASE_URL, link=link)
        text_content = _('''
        Follow the link to update your password in the IMS Guide: {base_url}{link}
        If you did not request a password change, disregard this email.

        IMS Guide.
        ''').format(base_url=settings.BASE_URL, link=link)

        subject = _('Reset password - Institute Moreira Salles')
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()


class ForgotPasswordSuccessView(TemplateView):
    template_name = 'forgot_password_success.html'


class ResetPasswordUpdateView(UpdateView):
    model = User
    form_class = ResetPasswordForm
    template_name = 'reset_password_form.html'

    def get_object(self):
        data = signing.loads(self.kwargs['token'])
        try:
            user = User.objects.get(id=data['id'])
            return user

        except User.DoesNotExist:
            return None
        return user

    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)

        data = signing.loads(self.kwargs['token'])
        if self.object.last_login.strftime('%Y-%m-%d %H:%M:%S') != data['last_login']:
            raise Http404(_('Page not found'))

        return result

    def form_valid(self, form):
        data = form.cleaned_data
        user = self.object
        user.set_password(data['new_password'])
        user.save()

        authenticated_user = authenticate(
            self.request,
            username=user.username,
            password=data['new_password']
        )
        login_django(self.request, authenticated_user)
        return redirect('home')
