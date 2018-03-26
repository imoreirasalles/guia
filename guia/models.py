from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField, JSONField
import uuid


class Pessoa(models.Model):
	"""
	Model representing people
	"""

	name = models.CharField('Nome', max_length=200)
	date_of_birth = models.DateField('Nascimento', null=True, blank=True)
	date_of_death = models.DateField('Falecimento', null=True, blank=True)
	ocupacao = models.CharField('Ocupação', max_length=200, null=True, blank=True)
	bio_short = models.TextField(
	    'Biografia curta', max_length=300, null=True, blank=True)

	class Meta:
		verbose_name = 'Pessoa'
		ordering = ['name']

	def get_absolute_url(self):
		return reverse('pessoa-info', args=[srt(self.id)])

	def __str__(self):
		return self.name


class Colecao(models.Model):
    AREA_IMS = (
	    ('Acervo', 'Acervo'),
	    ('Biblioteca', 'Biblioteca'),
	    ('Fotografia', 'Fotografia'),
	    ('Iconografia', 'Iconografia'),
	    ('Literatura', 'Literatura'),
	    ('Música', 'Música'),
        )

    ENTRY_MODE = (
	   ('Acumulação', 'Acumulação'),
	   ('Comodato', 'Comodato'),
	   ('Compra', 'Compra'),
       ('Doação', 'Doação'),
       ('Transferência', 'Transferência')
       )

    id = models.CharField('Código (UID)', max_length=20,
                          primary_key=True, help_text="Código de identificação")
    old_id = models.CharField('Códigos anteriores', max_length=140,
                              help_text="Outros códigos de identificação", null=True, blank=True)
    title = models.CharField('Títuto', max_length=300)
    area_ims = models.CharField(
        'Área responsável', max_length=200, choices=AREA_IMS)
    entry_model = models.CharField(
        'Modo de entrada', max_length=200, choices=ENTRY_MODE, null=True, blank=True)
    entry_date = models.DateField(
        'Data de entrada', auto_now=False, auto_now_add=False, null=True, blank=True)
    entry_obs = models.TextField(
        'Observações', help_text='Insira observações sobre a coleção', null=True, blank=True)
    resumo = models.TextField(
        help_text='Faça uma breve descrição da coleção', null=True, blank=True)
    num_itens = models.IntegerField(null=True, blank=True)
    num_itens_online = models.IntegerField(null=True, blank=True)
    pessoas = models.ManyToManyField(Pessoa, blank=True)
    duration = models.DurationField('Duração', null=True)
    teste_json = JSONField(null=True,)
    teste_array = ArrayField(models.CharField(
        max_length=200), blank=True, null=True)


class Meta:
	verbose_name = 'Coleção'
	verbose_name_plural = 'Coleções'
	ordering = ['id']

	def __str__(self):
		"""
		String for representing the Model object.
		"""
		return self.title

	def get_absolute_url(self):
		"""
		Returns the url to access a detail record for this collection.
		"""
		return reverse('colecao-detalhe', args=[str(self.id)])


class Lote(models.Model):
	"""
	Modelo representando Lote (entrada patrimonial)
	"""

	ENTRY_MODE = (
		('Acumulação', 'Acumulação'),
		('Comodato', 'Comodato'),
		('Compra', 'Compra'),
		('Doação', 'Doação'),
		('Transferência', 'Transferência')
	)
	id = models.UUIDField('Identificador', primary_key=True, default=uuid.uuid4, help_text='Identificador do lote de controle patrimonial')
	colecao = models.ForeignKey('Colecao', on_delete=models.SET_NULL, null=True)
	entry_model = models.CharField('Modo de entrada', max_length=200, choices=ENTRY_MODE, null=True, blank=True)
	entry_date = models.DateField('Data de entrada', auto_now=False, auto_now_add=False, null=True, blank=True)
	entry_obs = models.TextField('Observações', max_length=1000, help_text='Insira observações sobre a coleção', null=True, blank=True)

	def __str__(self):
		"""
		String que representa o objeto
		"""
		return str("Data - " + self.entry_model + " - Título da Colecao")


class Exhibition(models.Model):
	"""
	Model representing exhibitions
	"""

	id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4)
	title = models.CharField('Nome', max_length=200)
	date_of_begin = models.DateField('Início', null=True, blank=True)
	date_of_end = models.DateField('Fim', null=True, blank=True)
	location = models.CharField('Local', max_length=200, null=True, blank=True)
	description = models.TextField('Sobre', null=True, blank=True)

	class Meta:
		verbose_name = 'Exposição'
		verbose_name_plural = 'Exposições'
		ordering = ['date_of_begin']

	def get_absolute_url(self):
		return reverse('expo-info', args=[srt(self.id)])

	def __str__(self):
		return self.title


class Publication(models.Model):
	"""
	Model representing publications
	"""

	id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4)
	title = models.CharField('Nome', max_length=200)
	date_of_release = models.DateField('Data de lançamento', null=True, blank=True)
	author = models.CharField('Autor', max_length=200, null=True, blank=True)
	description = models.TextField('Sobre', null=True, blank=True)

	class Meta:
		verbose_name = 'Publicação'
		verbose_name_plural = 'Publicações'
		ordering = ['date_of_release']

	def get_absolute_url(self):
		return reverse('pub-info', args=[srt(self.id)])

	def __str__(self):
		return self.title
