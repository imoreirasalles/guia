from django.urls import path
from . import views

urlpatterns = [
	path('', views.ColecaoListView.as_view(), name='colecoes'),
	path('colecao/<str:pk>', views.ColecaoDetailView.as_view(), name='colecao-detalhe'),
	path('exhibitions/', views.ColecaoListView.as_view(), name='exhibitions'),
]
