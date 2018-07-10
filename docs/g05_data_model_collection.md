Este modelo de dados está em construção, tendo como referência projetos como a [NYPL Digital Collections](http://api.repo.nypl.org/#data-model), o [MoMA Exhibition History](https://github.com/MuseumofModernArt/exhibitions) e o [Getty ULAN](https://www.getty.edu/research/tools/vocabularies/ulan/about.html).

![Modelo UML](images/ims_collections_guide_uml.png)

------------

## Coleção

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

------------

###  Coleção (`collection`)

Field Name  | Django Type Field | Field Description  | Example
------------|-------------------|--------------------|------------
`uuid`                          | UUIDField, **PK**, Unique, Sequential   | Identificador único universal do objeto  |  123e4567-e89b-12d3-a456-426655440000
`created`                       | dateField, NotNull, default=now         | Data de criação do registro | 01/01/2018
`id`                            | CharField(32), Editable, Null, Blank    | Identificador único atribuido manualmente pelo IMS | ABC123
`id_old`                        | JSONField, Null, Blank                  | Códigos já utilizados para identificar a Coleção | {"Instituição 1": "ABC", "Instituição 2": "123"}
`management_unit`               | ManagementUnit **FK**[0..1], Null, Blank| Qual coordenação é responsável pela Coleção | Coord. de Fotografia
`aggregation_type`              | AggregationType, **FK** [0..1], Null, Blank | Tipos de agregação | Arquivo, Coleção, Conjunto
`title`                         | CharField(256), Null, Blank             | Título da Coleção | Biblioteca de Fulano de Tal
`slug`                          | SlugField(128), Null, Blank             | Slug para URLs | biblioteca-fulado
`image_feature`    | ImageField(upload_to='/model/date_now-namefile.extesion'), Null, Blank| campo de imagem | /collection/2018_01_30-ligia_fagundes_teles.jpg|
`image_feature_caption`    | CharField(256), Null, Blank| Legenda da imagem   | Retrato de Ligia Fagundes Telles|
`date_start`                    | DateField, Null, Blank                      | Data inicial do conteúdo da Coleção. Esse campo não tem a pretensão de ser preciso, ele atuará na busca de informações (search by date) | 02/08/2018
`date_start_caption`            | CharField(128), Null, Blank             | Data inicial descrita em linguagem natural que aparecerá na ficha da coleção.  | 02/08/2018
`date_end`                      | DateField, Null, Blank                  | Data final do conteúdo da Coleção. Esse campo não tem a pretensão de ser preciso, ele atuará na busca de informações (search by date)  | 02/08/2018
`date_end_caption`              | CharField(128), Null, Blank             | Data final descrita em linguagem natural que aparecerá na ficha da coleção. | 02/08/2018
`description_level`             | DescriptionLevel, **FK** [0..1], Null, Blank| Nível de descrição | 0 - Controle Inicial
`genre_tags`                    | Genre, **FK** [0..\*], Null, Blank      | Gênero Documental | Iconográfico, Texual
`abstract`                      | TextField, Null, Blank                  | Breve apresentação da Coleção | A coleção em 3,5 tweets.
`location_generic`              | Location **FK**[0..1], Null, Blank      | Informação generica sobre a localização da coleção  | IMS Paulista
`location_specific`             | CharField(128), Null, Blank             | Informação específica sobre a localização da coleção  | Armário 1A Prateleira 2B
`dimension`                     | JSONField, Null, Blank                  | Quantificação preliminar da dimensão | {"Metros lineares": "200", "Envólucros": "500"}
`inventary_status`              | NullBooleanField, Null, Blank           | Status do inventário da coleção | True
`inventary_last_date`           | DateField, Null, Blank                  | Data do último inventário realizado | Data
`inventary_data`                | JSONField                               | Quantificação preliminar do inventário | {"Fotografias": "1439", "Cadernos": "12"}
`acquisitions`                  | Acquisition **FK**[0..\*], Null, Blank  | aquisições vinculadas à coleção  | AcquisitionID-1, AcquisitionID-2
`items_total`               | PositiveIntegerField, Null, Blank      | Número total de itens na Coleção | 15000
`items_processed`           | PositiveIntegerField, Null, Blank      | Número total de itens processados | 5000
`items_online`              | PositiveIntegerField, Null, Blank      | Número total de itens disponíveis online | 500
`access_condition`          | AccessCondition, **FK** [0..1], Null, Blank | Condição de Acesso | Parcial - Em processamento
`access_local_status`           | NullBooleanField, Null, Blank           | Verdadeiro ou falso | Sim
`access_local_url`              | URLField, Null, Blank                   | Url de acesso ao material na internet | URL
`access_online_status`          | NullBooleanField, Null, Blank           | Verdadeiro ou falso (sim ou não)  | Sim
`access_online_url`             | URLField, Null, Blank                   | Url de acesso ao material na internet | URL
`full_text`                     | TextField, Null, Blank                  | Texto completo sobre a Coleção   | Texto grande, com vários parágrafos.
`containers`                    | Container **FK**[0..\n], Null, Blank   | Conjuntos | Conjunto1, Conjunto2, etc..
`related_persons`               | Person **FK**[0..\*], Null, Blank      | Pessoas relacionadas  | Ligia Fagundes Teles
`related_exhibitions`           | Exhibition **FK**[0..\*], Null, Blank  | Exposições relacionadas | Retrospectiva Ligia
`related_publications`          | Publication **FK**[0..\*], Null, Blank | Publicações relacionadas | Caderno de Literatura
`related_events`                | Events **FK**[0..\*], Null, Blank      | Eventos relacionados | Clube de Leitura
`other_data`                    | JSONField                              | Informação sem estrutura definida pelo modelo | {"Notas do bisneto do doador de segundo grau": "Lorem ipsum"}


###  Conjunto (`Container`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`uuid`     | UUIDField, **PK**, Unique, Sequential | Identificador único universal |  123e4567-e89b-12d3-a456
`created`  | DateTimeField, NotNull, default=now   | Cata de criação do registro | 01/01/2018
`id`       | CharField(64), Unique, Null, Blank    | Código atribuído ao Conjunto para controle interno da instituição. Esse valor tem de ser editável |  001002
`collection_mother` | Collection **FK**[0..1], NotNull    | Coleção mãe desse Conjunto  | Coleção Gilberto Ferrez
`container_mother`  | Container **FK**[0..1], Null, Blank | Conjunto mãe desse Conjunto | Arquivo Marc Ferrez
`aggregation_type`  | AggregationType **FK**[0..1], Null, Blank      | Tipologia do conjunto |  Conjunto
`title`             | CharField(128), Null, Blank                    | Título do conjunto | Panoramas do Rio de Janeiro
`description_level` | DescriptionLevel, **FK** [0..1]                | Nível de descrição | 1 - Descrição Básica
`abstract` | TextField, Null, Blank | Breve apresentação do conjunto | Formado a partir da produção autoral do fotógrafo...





