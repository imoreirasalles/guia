## Features List 1.0
> *** Legendas: ***
> CRUD: Create, Read, Update, Disable;

#### Logging Disable Data
  - Toda manipulação de dados, para todos os modelos, deve ser feita em modo log, isto é, os dados não devem ser efetivamente apagados e sim desabilitados. Essa feature visa facilitar a auditoria de dados no sistema.
  - Essa feature faz parte da construção de todas as classes/métodos do sistema;

#### Importação e Exportação em Lote (csv/xls)
  - Os cadastros que deverão ter essa funcionalidade são: Eventos, Exposições, Publicações, Coleções, Contratos e Conjuntos;
  - O sistema deve permitir exportação(output) de dados para todos os tipos de usuários, inclusive os públicos;
  - O sistema deve permitir exportação(output) de dados a partir do resultado de uma busca (search result);
  - O sistema deve permitir importação (input) de dados apenas aos usuários autorizados a edição/alteração de classes;
  - O formato de importação/exportação deve ser csv / xls file;

#### Exportação de resultados em pdf
  - Exportar relatório em `.pdf` sobre determinados resultados de uma busca (search result);

#### CRUD de USUÁRIOS - `User`
  - Via Django Admin, by superadmin;
  - Implementar login via social network (gmail account);
  - Implementar diferentes perfis de usuário (ver user roles specs);

#### CRUD de CONTRATOS - `Contract`
  - Via Django Admin e templates, por ;

#### CRUD de ESPAÇO e SUBESPAÇO - `space`, `subspace`
  - Via Django Admin, by superadmin;
  - Implementar classe para registros os espaços(sedes) do IMS (MG, RJ e SP);
  - Implementar classe para registro dos subespaços viculados ao espaços-mãe (ex.: biblioteca é subespaço do espaço 'IMS Paulista');
  - Vincular subespaços a classe `event` e `exhibition` para registro e recuperação de itinerancia de eventos e exposições;

#### CRUD de EVENTOS - `Event`
  - Via Django Admin e templates, by ...; TODO: completar com perfil de usuários autorizado;
  - 1 Exposição pode ter 0 até N Eventos;
  - 1 Evento pode ter 0 até N Exposições;

#### CRUD de EXPOSIÇÕES - `Exhibition`
  - Via Django Admin e templates,

Na itinerância de `Exposição` exibir a sequência de edições.

Ex.: `IMS Paulista (Galeria 2) > IMS Rio (Casa) > Maison Européenne de la Photographie`

#### CRUD de PUBLICAÇÕES - `Publication`

## Diferença entre `Publicação` e folheteria
Considerar que uma publicação é todo projeto editorial consolidado num produto comercial. Ex.: livro, catálogo de exposição, DVD, etc. Já a folheteria distribuída gratuítamente não será considerada uma publicação autônoma, mas um documento anexado a outra entidade.

**Exemplos**

Uma `Publicação` _Catálogo da Exposição_ está relacionada a uma `Exposição`

Um `Evento` _Mostra de Cinema_ tem como documentação anexa um folder da sua programação

#### CRUD de COLEÇÕES - `Collection`


4. Fundamentos para implementação de procedimentos Spectrum
  - Controle de entradas patrimoniais, apresentando caminhos de procedência dos lotes/coleções
  - Controle de laudos de conservação e outros relatórios técnicos gerados na instituição

5. Outros
* Criar coleções, de n conjuntos e criar relações com exposições, publicações, pessoas e entradas patrimoniais (lotes);
* Exibições e/ou dados sobre conhecimento já produzido na instituição, listando exposições, publicações e artistas relacionados às coleções;
* Definir um Modelo de Dados desejável, elencando os principais dados que devem constar nas visualizações do guia. Este modelo é o desenho e a seleção de dados já presentes no sistema de gestão de acervos;
* Documento descritivo com de definição de ACESSOS E PERMISSÕES (User roles);
* Documento descritivo com CASOS DE USO, descrevendo funções do sistema como criação e edição de coleções, importação de dados, tipos de relatórios, etc;

## Upload semântico de documentos

Organizar semanticamente os arquivos na pasta `STATIC`, renomeando arquivos conforme vocabulário controlado. Upload simples feito pelo admin do Django, na primeira versão só aceita `.jpg` e `.pdf`

**Exemplos**

Upload de imagem destaque de uma `Coleção`:

`STATIC` > `Collections` > `collection_slug` > `timestamp` + `collection_slug` + `imagem-destaque.jpg`

Upload de lista de obras utilizada numa `Edição` de uma `Exposição`:

`STATIC` > `Exhibitions` > `expo_slug` > `timestamp` + `expo_ed_slug` + `lista-de-obras.pdf`

&nbsp;

## Features List 2.0

#### CRUD de ITEM do acervo
  - Todo item deve conter uma página de exibição própria;
  - Toda página do item exibe Itens relacionados a este;
  - Considerar a relação de Itens com a mesma informação em diferentes suportes, frequentemente relacionando uma matriz com diversas reproduções. Essa informação pode aparecer como uma listagem de `Itens relacionados` na página de detalhe.

**Exemplos**
- `Negativo` e suas diversas reproduções _vintages_ e posteriores;
- `Fonograma` presente em diversos discos;
