from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.guide, name='guide'),
	path('colecao/<str:pk>', views.ColecaoDetailView.as_view(), name='colecao-detalhe'),
	path('exhibitions/', views.ColecaoListView.as_view(), name='exhibitions'),
]
