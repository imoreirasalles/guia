## Objetivos
* Consolidar informações da memória institucional, definindo as classes `Coleção`, `Exposição`, `Publicação`, `Evento`, `Pessoa` e `Lugar` a partir de dados fragmentados em diferentes áreas da instituição
* Estruturar metadados legíveis para cada classe, priorizando a visualização de dados sobre `Coleção`, `Exposição` e `Publicação`
* Estruturar relacionamentos entre cada classe, priorizando a elegância do banco de dados 
* Organizar vocabulários controlados, dicionários, taxonomias e ontologias utilizados na instituição

## Features List

1. Logging Disable Data
  - Toda manipulação de dados, para todos os modelos, deve ser feita em modo log, isto é, os dados não devem ser efetivamente apagados e sim desabilitados. Essa feature visa facilitar a auditoria de dados no sistema.

2. CRUD de usuários
  - Via Django Admin, by superadmin
  - Implementar login via social network (gmail account)
  - Implementar diferentes perfis de usuário (ver user roles specs)

3. I/O para usuários leigos
  - Exportar relatório em `.pdf` sobre determinadas pesquisas
  - Exportar dados em `.csv`/`.xlsx` sobre determinadas pesquisas
  - Importar dados em `.csv`/`.xlsx`sobre determindados atributos de cada classe

4. Fundamentos para implementação de procedimentos Spectrum
  - Controle de entradas patrimoniais, apresentando caminhos de procedência dos lotes/coleções
  - Controle de laudos de conservação e outros relatórios técnicos gerados na instituição

5. Outros
* Criar coleções, de nir conjuntos e criar relações com exposições, publicações, pessoas e entradas patrimoniais (lotes);
* Exibições e/ou dados sobre conhecimento já produzido na instituição, listando exposições, publicações e artistas relacionados às coleções;
* Definir um Modelo de Dados desejável, elencando os principais dados que devem constar nas visualizações do guia. Este modelo é o desenho e a seleção de dados já presentes no sistema de gestão de acervos;
* Documento descritivo com de definição de ACESSOS E PERMISSÕES (User roles);
* Documento descritivo com CASOS DE USO, descrevendo funções do sistema como criação e edição de coleções, importação de dados, tipos de relatórios, etc;

***

## Acessos e permissões

Um `Colaborador` só pode editar coleções sob responsabilidade da sua `Coordenação`.

Um `Coordenador` revisa e publica o conteúdo da sua `Coordenação`.

Um `Pesquisador` acessa o painel administrativo sem permissão para edição.

## Casos de Uso

Um `Usuário` preenche uma ficha de `Coleção`, relacionando `Pessoas` de destaque no conteúdo descrito, assim como `Exposições`, `Publicações` e `Eventos` já realizados pela instituição.

***

## Upload semântico de documentos

Organizar semanticamente os arquivos na pasta `STATIC`, renomeando arquivos conforme vocabulário controlado. Upload simples feito pelo admin do Django, na primeira versão só aceita `.jpg` e `.pdf`

**Exemplos**

Upload de imagem destaque de uma `Coleção`:

`STATIC` > `Collections` > `collection_slug` > `timestamp` + `collection_slug` + `imagem-destaque.jpg`

Upload de lista de obras utilizada numa `Edição` de uma `Exposição`:

`STATIC` > `Exhibitions` > `expo_slug` > `timestamp` + `expo_ed_slug` + `lista-de-obras.pdf`

&nbsp;

## Página do Item exibe Itens relacionados
Considerar a relação de Itens com a mesma informação em diferentes suportes, frequentemente relacionando uma matriz com diversas reproduções. Essa informação pode aparecer como uma listagem de `Itens relacionados` na página de detalhe.

**Exemplos**

`Negativo` e suas diversas reproduções _vintages_ e posteriores

`Fonograma` presente em diversos discos


## Diferença entre `Publicação` e folheteria
Considerar que uma publicação é todo projeto editorial consolidado num produto comercial. Ex.: livro, catálogo de exposição, DVD, etc. Já a folheteria distribuída gratuítamente não será considerada uma publicação autônoma, mas um documento anexado a outra entidade.

**Exemplos**

Uma `Publicação` _Catálogo da Exposição_ está relacionada a uma `Exposição`

Um `Evento` _Mostra de Cinema_ tem como documentação anexa um folder da sua programação

***

## Questões

* Avaliar o uso do pacote [django-reversion](https://github.com/etianen/django-reversion)
* Avaliar o uso do [geo-django](https://docs.djangoproject.com/en/2.0/ref/contrib/gis/) para armazenar dados geográficos
* Avaliar o uso do pacote [django-import-export](https://github.com/django-import-export/django-import-export)
