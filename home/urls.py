# django core imports
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# project guia imports
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('signup/', views.UserCreateView.as_view(), name='signup'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot-password'),
    path('forgot-password/success/', views.ForgotPasswordSuccessView.as_view(), name='forgot-password-success'),
    path('reset-password/<str:token>/', views.ResetPasswordUpdateView.as_view(), name='reset-password-form'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
