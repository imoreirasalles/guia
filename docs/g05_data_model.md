Este modelo de dados está em construção, tendo como referência projetos como a [NYPL Digital Collections](http://api.repo.nypl.org/#data-model), o [MoMA Exhibition History](https://github.com/MuseumofModernArt/exhibitions) e o [Getty ULAN](https://www.getty.edu/research/tools/vocabularies/ulan/about.html).

![Modelo UML](images/ims_collections_guide_uml.png)

## Coleção

_Definir o que é `Coleção`, sob quais critérios._

É composta pelos seguintes elementos:

```
Coleção     (Collection)
Conjunto    (Container)
Item        (Item)
Captura     (Capture)
```

Coleções são feitas por um ou mais Itens, que por sua vez são organizados em Conjuntos. Uma coleção pode conter zero ou mais Conjuntos, que por sua vez podem conter zero ou mais Conjuntos e/ou zero ou mais Items, criando uma hierarquia em árvore. Nem todos os Itens pertencem a uma Coleção, mas a maioria sim. Items são compostos por uma ou mais Capturas que representam aspectos físicos, como a página de um livro ou a frente de uma fotografia. Cada Captura tem um arquivo digital correspondente, como uma imagem, vídeo, áudio ou documento.

```
| -- Coleção
    | -- Conjunto
        | -- Item
            | -- Captura 1
        | -- Item
            | -- Captura 1
            | -- Captura 2
    | -- Conjunto
        | -- Item
        | -- Item
            | -- Captura 1
        | -- Conjunto
            | -- Item
            | -- Item
                | -- Captura 1
```

Uma **Coleção**(`collection`) é composta pelos seguintes atributos:

Nome do campo            | Tipo           | Descrição                | Exemplo
-------------------------|----------------|--------------------------|------------
`uuid`        | UUIDField      | Identificador único universal |  123e4567-e89b-12d3-a456-426655440000
`id_human`    | CharField(10)  | Identificador único para controle interno da instituição |  ABC123
`id_old`      | JSONField      | Dicionário de códigos já utilizados para identificar a Coleção | {"Instituição 1": "ABC", "Instituição 2": "123"}
`title`       | CharField(200) | Título da Coleção | Biblioteca de Fulano de Tal
`slug`        | SlugField      | Slug para URLs | biblioteca-fulado
`abstract`    | TextField(500) | Breve apresentação da Coleção | A coleção em 3,5 tweets.
`fulltext`    | TextField      | Texto completo sobre a Coleção | Textão...
`type`        | TIPO_COLECAO   | Vocabulário controlado | Arquivo, Coleção, Conjunto
`doc_genre`   | GENERO_DOCUMENTAL   | Vocabulário controlado | Cartográfico, Iconográfico, Literário
`dimension`   | JSONField      | Quantificação preliminar da dimensão | {"Metros lineares": "200", "Envólucros": "500"}
`begin_date`  | DateField    | Data inicial do conteúdo da Coleção | 02/08/2018
`end_date`    | DateField    | Data final do conteúdo da Coleção | 02/08/2018
`itens_total`          | PositiveIntegerField  | Número total de itens na Coleção | 15000
`itens_processed`      | PositiveIntegerField  | Número total de itens processados | 5000
`itens_online`         | PositiveIntegerField  | Número total de itens disponíveis online | 500
`access_condition`     | ACCESS_CONDITION  | Vocabulário controlado | Total, Parcial, Restrito
`access_local_status`  | NullBooleanField  | Verdadeiro ou falso | Total
`access_local_path`    | URLField          | Vocabulário controlado | URL
`access_online_status` | NullBooleanField  | Verdadeiro ou falso | Parcial
`access_online_path`   | URLField          | Vocabulário controlado | URL
`location_generic`     | CharField(100)    | Vocabulário controlado | URL
`location_specific`    | CharField(100)    | Vocabulário controlado | URL
`inventary_status`     | NullBooleanField  | Vocabulário controlado | URL
`inventary_last_date`  | DateField         | Vocabulário controlado | URL
`inventary_data`       | JSONField         | Quantificação preliminar do inventário | {"Fotografias": "1439", "Cadernos": "12"}
`other_data`           | JSONField         | Informação sem estrutura definida pelo modelo | {"Notas do bisneto do doador de segundo grau": "Lorem ipsum"}


Um **Conjunto** (`Container`) é composto pelos seguintes atributos:

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`id`       | Número  | Identificador único numérico atribuído a cada Conjunto para controle interno da instituição |  001002
`uuid` | UUID | Identificador único universal do Conjunto |  123e4567-e89b-12d3-a456
`type`     | String  | Tipologia do conjunto |  Arquivo
`title`    | String  | Título do conjunto |  Arquivo pessoal de Marcel Gautherot
`abstract` | String  | Breve apresentação do conjunto |  Formado a partir da produção autoral do fotógrafo...



Um **Item** é composto pelos seguintes atributos:

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`uuid`| UUID   | Identificador único universal do Item |  123e4567-e89b-12d3-a456-426655440000

## Exposição

_Definir o que é `Exposição`, sob quais critérios._

Uma Exposição pode ter diversas Edições:


```
| -- Exposição
    | -- Edição 1
    | -- Edição 2
| -- Exposição
    | -- Edição 1
```


Uma **Exposição** `exhibition` é composta pelos seguintes atributos:

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`id`       | Número  | Identificador único numérico atribuído a cada Exposição para controle interno da instituição | 0326
`uuid`     | UUID    | Identificador único universal da Exposição |     123e4567-e89b-12d3-a456-426655440000
`title` | String  | Título completo da Exposição | Conflitos: fotografia e violência política no Brasil
`slug` | String  | Apelido curto e intuitivo para construção de atalhos e URLs  | Conflitos
`abstract`| String  | Breve resumo da Exposição escrito em Markdown | A exposição procura contradizer a imagem do Brasil como país pacífico e oferece um olhar sobre a história nacional que colabora...
`date_start` | Data    | Data da primeira abertura da Exposição | 25/11/2017
`date_end`| Data    | Data do último encerramento da Exposição  | 25/02/2018
`url`   | String  | Endereço web da Exposição do site da instituição | museu.edu/expo/conflitos
`team`  | JSON    | Ficha técnica geral da Exposição, com a atribuição da equipe principal | {"Curadoria": "Heloisa Espada", "Assistente de Curadoria": "Tiê Higashi"}

A itinerância da exposição é composta por **Edições**, que contém os seguintes atributos:

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`id`           | Número  | Identificador único da Edição composto com ExhibitionNumber |  0326-02
`place`        | String  | Local de realização da Edição | IMS Paulista
`begin_date`   | Data    | Data de abertura da Edição, quando conhecida | 02/05/2018
`end_date`     | Data    | Data de encerramento da Edição, quando conhecida  | 02/08/2018
`roles`        | JSON    | Ficha técnica específica da Edição, com a atribuição de toda equipe envolvida | {"Produção": "Equipe"; "Montagem": "Equipe"}


## Publicação

_Definir o que é `Publicação`, sob quais critérios._

- Diferença entre `Publicação` e folheteria:
  - Considerar que uma publicação é todo projeto editorial consolidado num produto comercial. Ex.: livro, catálogo de exposição, DVD, etc. Já a folheteria distribuída gratuítamente não será considerada uma publicação autônoma, mas um documento anexado a outra entidade.
- **Exemplos**
  - Uma `Publicação` _Catálogo da Exposição_ está relacionada a uma `Exposição`
  - Um `Evento` _Mostra de Cinema_ tem como documentação anexa um folder da sua programação

Nome do campo      | Tipo   | Descrição  | Exemplo
-------------------|--------|--------------------------|------------
`uuid`         | UUID   | Identificador único universal da Publicação |  123e4567-e89b-12d3-a456-426655440000
`id`           | Número  | Identificador único numérico atribuído a cada Publicação para controle interno da instituição | 201803
`title`        | String | Título completo da Publicação | Marc Ferrez
`slug`         | String | Título curto da Publicação | Marc Ferrez
`abstract`     | String | Breve resumo da Publicação escrito em Markdown | A exposição procura contradizer a imagem do Brasil como país pacífico e oferece um olhar sobre a história nacional que colabora...
`author`       | JSON   | Ficha técnica dos  | {"Autor": "Pessoa 1", "Autor": "Pessoa 2"}
`release_date` | Date   | Data de publicação | 02/08/2014
`publisher`    | Date   | Nome da editora | Companhia das Letras
`size`         | JSON   | Dimensão da publicação em centímetros | {"largura": "10", "altura": "10", "prof": "10"}
`pages`        | Date   | Data de morte da pessoa | 12/01/1923
`type`         | String | Gênero da Pessoa (binário) | Homem
`type`         | String | Gênero da Pessoa (binário) | Homem


## Evento

_Definir o que é `Evento`, sob quais critérios._

Nome do campo          | Tipo    | Descrição                | Exemplo
-----------------------|---------|--------------------------|------------
`uudi`           | UUID    | Identificador único universal do Evento |  0326-02
`id`             | Número  | Identificador único do Evento para controle interno da instituição |  0326-02
`title`          | String  | Título do evento | Palestra do fulano de tal
`slug`           | String  | Título intuitivo do evento | IMS Paulista
`begin_date`     | Data    | Data de início do Evento, quando conhecida | 02/05/2018
`end_date`       | Data    | Data de fim do Evento, quando conhecida  | 02/08/2018
`type`           | String  | Tipo do Evento  | Palestra
`place`          | String  | Local de realização do Evento  | Museu de Arte
`abstract`       | String  | Breve apresentação do Evento | IMS Paulista
`roles`          | JSON    | Ficha técnica específica do Evento | {"Palestrante": "Equipe", "Filmagem": "Equipe"}


## Pessoa

_Definir o que é `Pessoa`, sob quais critérios._

Nome do campo        | Tipo   | Descrição  | Exemplo
---------------------|--------|--------------------------|------------
`uuid`        | UUID   | Identificador único universal da Pessoa no banco de dados da instituição |  123e4567-e89b-12d3-a456-426655440000
`slug`        | String | Nome da pessoa para exibição pública | Marc Ferrez
`name_first`  | String | Primeiro nome da Pessoa | Marc
`name_last`   | String | Sobrenome da Pessoa | Ferrez
`begin_date`  | Date   | Data de nascimento da pessoa | 07/12/1843
`end_date`    | Date   | Data de morte da pessoa | 12/01/1923
`gender`      | String | Gênero da Pessoa (binário) | Homem
`nation`      | String | País de atuação, frequentemente distinto do país de origem | Brasileiro
`role`        | String | Principal papel profissional de atuação  | Fotógrafo
`institution` | String | Principal instituição de atuação  | Casa Marc Ferrez & Cia.
`bio_short`   | String | Biografia curta da Pessoa | Principal fotógrafo brasileiro do século XIX, dono de uma obra que se equipara à dos maiores nomes da fotografia em todo o mundo, Marc Ferrez é o mais significativo fotógrafo do período...
`bio_full`    | String | Biografia completa da Pessoa | Principal fotógrafo brasileiro do século XIX, dono de uma obra que se equipara à dos maiores nomes da fotografia em todo o mundo, Marc Ferrez é o mais significativo fotógrafo do período... ...
`url`         | String | Endereço web da Pessoa no site da instituição | museu.edu/pessoa/marc-ferrez
`lod`         | JSON   | Dicionário de UIDs em projetos de Linked Open Data, como Virtual International Authority File (VIAF), Wikidata (WIKI), Union List of Artist Names (ULAN) ou Photographers’ Identities Catalog (PIC) | {"VIAF": "69111120", "WIKI": "Q3180571", "ULAN": "500037201", "PIC": "1758"}

## Aquisição

Nome do campo            | Tipo       | Descrição  | Exemplo
-------------------------|------------|------------|------------
`uuid`       | UUIDField  | ...        | ...
`method`     | METODO_AQUISICAO | ...  | ...
`source`     | Person 1-* | ...        | ...
`dealer`     | Person 1-* | ...        | ...
`begin_date` | DateField  | ...        | ...
`end_date`   | DateField  | ...        | ...
`abstract`   | TextField  | ...        | ...
`other_data` | JSONField  | ...        | ...
