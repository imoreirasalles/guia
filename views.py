from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Colecao, Exhibition

class ColecaoListView(generic.ListView):
	model = Colecao
	context_object_name = 'colecoes'
	queryset = Colecao.objects.all()

class ColecaoDetailView(generic.DetailView):
	model = Colecao

	def colecao_detail_view(request,pk):
		try:
			colecao_id = Colecao.objects.get(pk=pk)
		except Colecao.DoesNotExist:
			raise Http404("Coleção não existe")

		#colecao_id=get_object_or_404(Colecao, pk=pk)

		return render(
			request,
			'guia/colecao_detail.html',
			context={'colecao':colecao_id}
		)

class ExhibitionListView(generic.ListView):
	model = Exhibition
	context_object_name = 'exhibitions'
	queryset = Colecao.objects.all()
