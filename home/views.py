# core django imports
from django.conf import settings
from django.core import signing
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView, ListView, TemplateView

# Project guia imports
from home.models import Post
from collection.models import Collection
from exhibition.models import Exhibition
from publication.models import Publication
from event.models import Event
from person.models import Person

from .forms import ForgotPasswordForm


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
        collection_total = Collection.objects.all().count()
        return collection_total

    def exhibition_total(self):
        exhibition_total = Exhibition.objects.all().count()
        return exhibition_total

    def publication_total(self):
        publication_total = Publication.objects.all().count()
        return publication_total

    def event_total(self):
        event_total = Event.objects.all().count()
        return event_total

    def person_total(self):
        person_total = Person.objects.all().count()
        return person_total


class ForgotPasswordView(FormView):
    form_class = ForgotPasswordForm
    template_name = 'forgot_password.html'

    def form_valid(self, form):
        user = form.cleaned_data['username']
        self.sendmail(user)
        return redirect('forgot-password-success')

    def sendmail(self, user):
        from_email = settings.EMAIL_HOST_USER
        to = user.email
        data = {
            'id': user.id,
            'last_login': '',
        }
        if user.last_login:
            data['last_login'] = user.last_login.strftime('%Y-%m-%d')

        link = reverse('reset-password', kwargs={'token': signing.dumps(data)})

        html_content = _('''
        Follow the link to update your password in the IMS Guide: <a href="{link}">click here</a>.<br>
        If you did not request a password change, disregard this email.<br><br>
        IMS Guide.
        ''').format(link=link)
        text_content = _('''
        Follow the link to update your password in the IMS Guide: <a href="{link}">click here</a>.<br>
        If you did not request a password change, disregard this email.<br><br>
        IMS Guide.
        ''').format(link=link)

        subject = _('Reset password - Institute Moreira Salles')
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()


class ForgotPasswordSuccessView(TemplateView):
    template_name = 'forgot_password_success.html'


class ResetPasswordFormView(FormView):
    form_class = ForgotPasswordForm
    template_name = 'forgot_password.html'
