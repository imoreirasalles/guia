Este modelo de dados está em construção, tendo como referência projetos como a [NYPL Digital Collections](http://api.repo.nypl.org/#data-model), o [MoMA Exhibition History](https://github.com/MuseumofModernArt/exhibitions) e o [Getty ULAN](https://www.getty.edu/research/tools/vocabularies/ulan/about.html).

![Modelo UML](https://github.com/buccalon/guia/blob/master/uml.png)

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

&nbsp;

Uma **Coleção** é composta pelos seguintes atributos:

Nome do campo            | Tipo           | Descrição                | Exemplo
-------------------------|----------------|--------------------------|------------
`collection_uuid`        | UUID           | Identificador único universal |  123e4567-e89b-12d3-a456-426655440000
`collection_id_human`    | CharField(10)  | Identificador único para controle interno da instituição |  001002
`collection_id_old`      | JSON           | Dicionário de todos os códigos já utilizados para identificar a Coleção | {"Instituição 1": "ABC", "Instituição 2": "123"}
`collection_title`       | CharField(200) | Título completo da Coleção | Biblioteca de Fulano de Tal
`collection_slug`        | CharField(200) | Título curto da Coleção | Biblioteca Fulado
`collection_abstract`    | TextField(500) | Breve apresentação da Coleção | 02/08/2018
`collection_fulltext`    | TextField()    | Breve apresentação da Coleção | 02/08/2018
`collection_type`        | TIPO_COLECAO     | Vocabulário controlado | Arquivo, Coleção, Conjunto
`collection_doc_genre`   | GENERO_DOCUMENTAL     | Vocabulário controlado | Cartográfico, Iconográfico, Literário
`collection_dimension`   | JSON           | Quantificação preliminar dos objetos identificados | {"Fotografias": "1439", "Cadernos": "12"}
`collection_begin_date`  | DateField()    | Data inicial do conteúdo da Coleção | 02/08/2018
`collection_end_date`    | DateField()    | Data final do conteúdo da Coleção | 02/08/2018
`collection_itens_total` | Number         | Número total de itens na Coleção | 15000
`collection_itens_processed` | Number     | Número total de itens processados | 5000
`collection_itens_online` | Number        | Número total de itens disponíveis online | 500
`collection_access_condition` | ACCESS_CONDITION        | Vocabulário controlado | Parcial
`collection_access_local_status` | Boolean | Verdadeiro ou falso | Total
`collection_access_local_path` | CharField()      | Vocabulário controlado | URL
`collection_access_online_status` | Boolean        | Verdadeiro ou falso | Parcial
`collection_access_online_path` | CharField()      | Vocabulário controlado | URL
`collection_location_generic` | CharField(100)  | Vocabulário controlado | URL
`collection_location_specific` | CharField(100)  | Vocabulário controlado | URL
`collection_inventary_status` | Boolean()  | Vocabulário controlado | URL
`collection_inventary_last_date` | DateField()  | Vocabulário controlado | URL


&nbsp;

Um **Conjunto** é composto pelos seguintes atributos:

Nome do campo        | Tipo    | Descrição                | Exemplo
---------------------|---------|--------------------------|------------
`container_id`       | UUID    | Identificador único do Conjunto criado a partir do `collection_id` |  001002-01
`container_type`     | String  | Tipologia do conjunto |  Arquivo
`container_title`    | String  | Título do conjunto |  Arquivo pessoal de Marcel Gautherot
`container_abstract` | String  | Breve apresentação do conjunto |  Formado a partir da produção autoral do fotógrafo...

&nbsp;

Um **Item** é composto pelos seguintes atributos:

Nome do campo     | Tipo    | Descrição                | Exemplo
------------------|---------|--------------------------|------------
`item_uuid`       | UUID    | Identificador único universal do Item |  123e4567-e89b-12d3-a456-426655440000

&nbsp;

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


Uma **Exposição** é composta pelos seguintes atributos:

Nome do campo       | Tipo    | Descrição                | Exemplo
--------------------|---------|--------------------------|------------
`expo_uuid`         | UUID    | Identificador único universal da Exposição |     123e4567-e89b-12d3-a456-426655440000
`expo_id`           | Número  | Identificador único numérico atribuído a cada Exposição para controle interno da instituição | 0326
`expo_title`        | String  | Título completo da Exposição | Conflitos: fotografia e violência política no Brasil
`expo_slug`         | String  | Apelido curto e intuitivo para construção de atalhos e URLs  | Conflitos
`expo_abstract`     | String  | Breve resumo da Exposição escrito em Markdown | A exposição procura contradizer a imagem do Brasil como país pacífico e oferece um olhar sobre a história nacional que colabora...
`expo_begin_date`   | Data    | Data da primeira abertura da Exposição | 25/11/2017
`expo_end_date`     | Data    | Data do último encerramento da Exposição  | 25/02/2018
`expo_url`          | String  | Endereço web da Exposição do site da instituição | museu.edu/expo/conflitos
`expo_roles`        | JSON    | Ficha técnica geral da Exposição, com a atribuição da equipe principal | {"Curadoria": "Heloisa Espada", "Assistente de Curadoria": "Tiê Higashi"}

&nbsp;

A itinerância da exposição é composta por **Edições**, que contém os seguintes atributos:

Nome do campo          | Tipo    | Descrição                | Exemplo
-----------------------|---------|--------------------------|------------
`expo_ed_id`           | Número  | Identificador único da Edição composto com ExhibitionNumber |  0326-02
`expo_ed_place`        | String  | Local de realização da Edição | IMS Paulista
`expo_ed_begin_date`   | Data    | Data de abertura da Edição, quando conhecida | 02/05/2018
`expo_ed_end_date`     | Data    | Data de encerramento da Edição, quando conhecida  | 02/08/2018
`expo_ed_roles`        | JSON    | Ficha técnica específica da Edição, com a atribuição de toda equipe envolvida | {"Produção": "Equipe"; "Montagem": "Equipe"}

&nbsp;

## Publicação

_Definir o que é `Publicação`, sob quais critérios._

- Diferença entre `Publicação` e folheteria:
  - Considerar que uma publicação é todo projeto editorial consolidado num produto comercial. Ex.: livro, catálogo de exposição, DVD, etc. Já a folheteria distribuída gratuítamente não será considerada uma publicação autônoma, mas um documento anexado a outra entidade.
- **Exemplos**
  - Uma `Publicação` _Catálogo da Exposição_ está relacionada a uma `Exposição`
  - Um `Evento` _Mostra de Cinema_ tem como documentação anexa um folder da sua programação

Nome do campo      | Tipo   | Descrição  | Exemplo
-------------------|--------|--------------------------|------------
`pub_uuid`         | UUID   | Identificador único universal da Publicação |  123e4567-e89b-12d3-a456-426655440000
`pub_id`           | Número  | Identificador único numérico atribuído a cada Publicação para controle interno da instituição | 201803
`pub_title`        | String | Título completo da Publicação | Marc Ferrez
`pub_slug`         | String | Título curto da Publicação | Marc Ferrez
`pub_abstract`     | String | Breve resumo da Publicação escrito em Markdown | A exposição procura contradizer a imagem do Brasil como país pacífico e oferece um olhar sobre a história nacional que colabora...
`pub_author`       | JSON   | Ficha técnica dos  | {"Autor": "Pessoa 1", "Autor": "Pessoa 2"}
`pub_release_date` | Date   | Data de publicação | 02/08/2014
`pub_publisher`    | Date   | Nome da editora | Companhia das Letras
`pub_size`         | JSON   | Dimensão da publicação em centímetros | {"largura": "10", "altura": "10", "prof": "10"}
`pub_pages`        | Date   | Data de morte da pessoa | 12/01/1923
`pub_type`         | String | Gênero da Pessoa (binário) | Homem
`pub_type`         | String | Gênero da Pessoa (binário) | Homem

&nbsp;

## Evento

_Definir o que é `Evento`, sob quais critérios._

Nome do campo          | Tipo    | Descrição                | Exemplo
-----------------------|---------|--------------------------|------------
`event_uudi`           | UUID    | Identificador único universal do Evento |  0326-02
`event_id`             | Número  | Identificador único do Evento para controle interno da instituição |  0326-02
`event_title`          | String  | Título do evento | Palestra do fulano de tal
`event_slug`           | String  | Título intuitivo do evento | IMS Paulista
`event_begin_date`     | Data    | Data de início do Evento, quando conhecida | 02/05/2018
`event_end_date`       | Data    | Data de fim do Evento, quando conhecida  | 02/08/2018
`event_type`           | String  | Tipo do Evento  | Palestra
`event_place`          | String  | Local de realização do Evento  | Museu de Arte
`event_abstract`       | String  | Breve apresentação do Evento | IMS Paulista
`event_roles`          | JSON    | Ficha técnica específica do Evento | {"Palestrante": "Equipe", "Filmagem": "Equipe"}

&nbsp;

## Pessoa

_Definir o que é `Pessoa`, sob quais critérios._

Nome do campo        | Tipo   | Descrição  | Exemplo
---------------------|--------|--------------------------|------------
`person_uuid`        | UUID   | Identificador único universal da Pessoa no banco de dados da instituição |  123e4567-e89b-12d3-a456-426655440000
`person_slug`        | String | Nome da pessoa para exibição pública | Marc Ferrez
`person_name_first`  | String | Primeiro nome da Pessoa | Marc
`person_name_last`   | String | Sobrenome da Pessoa | Ferrez
`person_begin_date`  | Date   | Data de nascimento da pessoa | 07/12/1843
`person_end_date`    | Date   | Data de morte da pessoa | 12/01/1923
`person_gender`      | String | Gênero da Pessoa (binário) | Homem
`person_nation`      | String | País de atuação, frequentemente distinto do país de origem | Brasileiro
`person_role`        | String | Principal papel profissional de atuação  | Fotógrafo
`person_institution` | String | Principal instituição de atuação  | Casa Marc Ferrez & Cia.
`person_bio_short`   | String | Biografia curta da Pessoa | Principal fotógrafo brasileiro do século XIX, dono de uma obra que se equipara à dos maiores nomes da fotografia em todo o mundo, Marc Ferrez é o mais significativo fotógrafo do período...
`person_bio_full`    | String | Biografia completa da Pessoa | Principal fotógrafo brasileiro do século XIX, dono de uma obra que se equipara à dos maiores nomes da fotografia em todo o mundo, Marc Ferrez é o mais significativo fotógrafo do período... ...
`person_url`         | String | Endereço web da Pessoa no site da instituição | museu.edu/pessoa/marc-ferrez
`person_lod`         | JSON   | Dicionário de UIDs em projetos de Linked Open Data, como Virtual International Authority File (VIAF), Wikidata (WIKI), Union List of Artist Names (ULAN) ou Photographers’ Identities Catalog (PIC) | {"VIAF": "69111120", "WIKI": "Q3180571", "ULAN": "500037201", "PIC": "1758"}

&nbsp;
