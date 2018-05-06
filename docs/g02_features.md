Lista de funcionalidades do aplicativo

* Controle interno sobre entradas patrimoniais, apresentando caminhos de procedência dos lotes/coleções;
* Exibições e/ou dados sobre conhecimento já produzido na instituição, listando exposições, publicações e artistas relacionados às coleções;
* Metadados estruturados e com legibilidade sobre acervo.
* Criar coleções, de nir conjuntos e criar relações com exposições, publicações, pessoas e entradas patrimoniais (lotes);
* Fazer o download de pesquisas de dados (excel e/ou csv  le);
* Exportar relatório em pdf sobre determinadas pesquisas.
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

***

## Questões

* Avaliar o uso do pacote [django-reversion](https://github.com/etianen/django-reversion)
* Avaliar o uso do [geo-django](https://docs.djangoproject.com/en/2.0/ref/contrib/gis/) para armazenar dados geográficos
* Avaliar o uso do pacote [django-import-export](https://github.com/django-import-export/django-import-export)