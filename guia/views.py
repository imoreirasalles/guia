from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import FormView, TemplateView

from .forms import ForgotPasswordForm


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


class ForgotPasswordView(FormView):
    form_class = ForgotPasswordForm
    template_name = 'forgot_password.html'

    def form_valid(self, form):
        user = form.cleaned_data['username']
        self.sendmail(user)
        return redirect('forgot-password-success')

    def sendmail(self, data):
        pass


class ForgotPasswordSuccessView(TemplateView):
    template_name = 'forgot_password_success.html'
