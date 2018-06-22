Este modelo de dados está em construção, tendo como referência projetos como a [NYPL Digital Collections](http://api.repo.nypl.org/#data-model), o [MoMA Exhibition History](https://github.com/MuseumofModernArt/exhibitions) e o [Getty ULAN](https://www.getty.edu/research/tools/vocabularies/ulan/about.html).

![Modelo UML](images/ims_collections_guide_uml.png)

## Coleção

É composta pelos seguintes elementos:

```
Coleção     (Collection)
Conjunto    (Set)
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

###  Coleção (`collection`)

Field Name  | Django Type Field | Field Description  | Example
------------|-------------------|--------------------|------------
`uuid`                          | UUIDField, **PK**, Unique, Sequential         | Identificador único universal do objeto  |  123e4567-e89b-12d3-a456-426655440000
`created`                       | dateField, NotNull, default=now              | data de criação do registro | 01/01/2018
`id`                            | CharField(32), Editable, Null, Blank          | Identificador único atribuido manualmente pelo IMS | ABC123
`id_old`                        | JSONField, Null, Blank                        | Dicionário de códigos já utilizados para identificar a Coleção | {"Instituição 1": "ABC", "Instituição 2": "123"}
`title`                         | CharField(256), Null, Blank                  | Título da Coleção | Biblioteca de Fulano de Tal
`slug`                          | SlugField(128), Null, Blank                  | Slug para URLs | biblioteca-fulado
`abstract`                      | TextField, Null, Blank                       | Breve apresentação da Coleção | A coleção em 3,5 tweets.
`fulltext`                      | TextField, Null, Blank                       | Texto completo sobre a Coleção   | Texto grande, com vários parágrafos.
`description_level`             | DescriptionLevel, **FK** [0..\*], Null, Blank | Nível de descrição da Coleção | 1 - Descrição Básica
`aggregation_type`              | AggregationType, **FK** [0..1], Null, Blank  | Vocabulário controlado | Arquivo, Coleção, Conjunto
`genre_tags`                    | Genre, **FK** [0..\*], Null, Blank            | Vocabulário controlado | Cartográfico, Iconográfico, Literário
`dimension`                     | JSONField, Null, Blank                       | Quantificação preliminar da dimensão | {"Metros lineares": "200", "Envólucros": "500"}
`date_start`                    | DateField, Null, Blank                       | Data inicial do conteúdo da Coleção. Esse campo não tem a pretensão de ser preciso, ele atuará na busca de informações (search by date) | 02/08/2018
`date_start_caption`            | CharField(128), Null, Blank                  | Data inicial descrita em linguagem natural que aparecerá na ficha da coleção.  | 02/08/2018
`date_end`                      | DateField, Null, Blank                       | Data final do conteúdo da Coleção. Esse campo não tem a pretensão de ser preciso, ele atuará na busca de informações (search by date)  | 02/08/2018
`date_end_caption`              | CharField(128), Null, Blank                   | Data final descrita em linguagem natural que aparecerá na ficha da coleção. | 02/08/2018
`thumbnail`                     | thumbnail **FK**[0..\*], Null, Blank          | imagens de demonstração associadas ao registro | / collection / 2018_01_30_ligia_fagundes_teles.jpg
`author`                        | Person **FK**[0..\*], Null, Blank       | autoridades sobre a coleção.  | Ligia Fagundes Teles
`sets`                          | Set **FK**[0..\*], Null, Blank               | Lista de conjuntos que integram a coleção | Conjunto 1, Conjunto 2
`items`                         | Item, **FK** [0..\*], Null, Blank            | Lista de itens que integram a coleção | Item 1, Item 2
`items_total`                   | PositiveIntegerField, Null, Blank            | Número total de itens na Coleção | 15000
`items_processed`               | PositiveIntegerField, Null, Blank            | Número total de itens processados | 5000
`items_online`                  |  PositiveIntegerField, Null, Blank            | Número total de itens disponíveis online | 500
`access_condition`              | AccessCondition, **FK** [0..1], Null, Blank   | Vocabulário controlado | Total, Parcial, Restrito
`access_local_status`           | NullBooleanField, Null, Blank                | Verdadeiro ou falso | Sim
`access_online_status`          | NullBooleanField, Null, Blank                 | Verdadeiro ou falso (sim ou não)  | Sim
`access_link`             | URLField, , Null, Blank                            | Url de acesso ao material na internet | URL
`location_generic`              | Location **FK**[0..1], Null, Blank           | Informação generica sobre a localização da coleção  | IMS Paulista
`location_specific`             | CharField(128), Null, Blank                  | Informação específica sobre a localização da coleção  | IMS Paulista
`inventary_status`              | NullBooleanField, Null, Blank                | Status do inventário da coleção | Sim
`inventary_last_date`           | DateField, Null, Blank                       | Data do último inventário realizado | URL
`inventary_data`                | JSONField                                    | Quantificação preliminar do inventário | {"Fotografias": "1439", "Cadernos": "12"}
`management_unit`               | ManagementUnit **FK**[0..1], Null, Blank     | Qual coordenação é responsável pela Coleção | Coord. de Fotografia
`other_data`                    | JSONField                                    | Informação sem estrutura definida pelo modelo | {"Notas do bisneto do doador de segundo grau": "Lorem ipsum"}

### Nível de Descrição (`DescriptionLevel`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`id`          | **PK**, Sequential | id único do nível de descrição | 001
`created`     | dateField, NotNull, default=now | data de criação do registro | 01/01/2018
`title`       | CharField(128), Null, Blank | título do nível de descrição    | 0. Controle Inicial
`description` | CharField(512),Null, Blank, | descrição do campo | Conferência, identificação e localização da aquisição para estabelecimento de controle patrimonial.


Exemplos de instâncias que vão constar neste modelo:

ID    | Name                    | Description     |
------|-------------------------|--------------|
0     | Controle inicial        | Conferência, identificação e localização da aquisição para estabelecimento de controle patrimonial. |
1     | Descrição Básica        | Registro de informações de procedência, proveniência e contextualização. |
2     | Descrição Intermediária | Identificação de informações para produção do arranjo, a partir da função primária e tipologia documental. Registro de informações de série, autoria, data de produção e caracterização formal. |
3     | Descrição Avançada      | Descrição individual dos documentos. Registro de informações primárias ou atribuídas, em cruzamento com fontes externas. Documentação retrospectiva, reconstituição de usos e referências ao documento em seu contexto de produção, apresentação e circulação. Conjuntos de documentos podem ser descritos em lote. |
4     | Pesquisa especializada  | Elaboração de argumento interpretativo e construção de conhecimento novo a partir da seleção e co-relação de documentos. Apresentação, mediação e interpretação para fins de difusão de conhecimento. Redação de legendas expandidas e textos de inéditos. |


### Tipo de Agregação (`AggregationType`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`id`       | **PK**, Sequential | id único do nível de descrição | 001
`created`  | dateField, NotNull, default=now | data de criação do registro | 01/01/2018
`title`      | CharField(128), NotNull, Blank, | Tipo de Agregação | Coleção
`description`   | CharField(512)     | descrição do campo | Conjuntos de __documentos reunidos intencionalmente__ por uma pessoa ou instituição |

Exemplos de instâncias que vão constar neste modelo:

ID  | Title        | Description     |
----|--------------|--------------|
1   | Coleção      | Conjuntos de __documentos reunidos intencionalmente__ por uma pessoa ou instituição |
2   | Arquivo      | Conjuntos de __documentos produzidos e acumulados__ por uma pessoa ou instituição __no desempenho de suas atividades__ |
3   | Biblioteca   | Conjuntos de __livros e publicações reunidos__ por uma pessoa ou instituição |
4   | Conjunto     | Agrupamento documentos |

### Generos do(s) Conteúdo(s) (`GenreTags`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`id`       | **PK**, Sequential | id único do nível de descrição | 001
`created`  | dateField, NotNull, default=now | data de criação do registro | 01/01/2018
`title`      | CharField(128), NotNull, Blank, | Tipo de Agregação | Audiovisual
`description`   | CharField(512)     | descrição do campo| Filmes cinematográficos, fitas magnéticas, vídeo digital e demais suportes audiovisuais.|

Exemplos de instâncias que vão constar neste modelo:

ID  | Title          | Descriptio             |
----|----------------|----------------------|
1   | Audiovisual    | Filmes cinematográficos, fitas magnéticas, vídeo digital e demais suportes audiovisuais. |
2   | Bibliográfico  | Livros, jornais, revistas, catálogos e brochuras. |
3   | Cartográfico   | Mapas e plantas arquitetônicas. |
4   | Fotográfico    | Fotografias em papel, slides, negativos, cromos e demais suportes fotográficos. |
5   | Iconográfico   | Desenhos, gravuras, caricaturas, charges, cartazes e peças gráficas. |
6   | Nato-digital   | Documentos originalmente gerados em computadores. |
7   | Sonoro         | Discos, fitas, cds e álbums. |
8   | Textual        | Cadernos, manuscritos, impressos e folheteria. |
9   | Tridimensional | Objetos tridimensionais. |

### Galeria de apresentação (`thumbnail`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`uuid`     | UUIDField, **PK**, Unique, Sequential | Identificador único universal do objeto  | 123e4567-e89b-12d3-a456-426655440000
`created`  | dateField, NotNull, default=now | data de criação do registro | 01/01/2018
`title`    | CharField(128), NotNull, Blank, | título do registro | Foto Lígia Fagundes Teles
`image`    | ImageField(upload_to='/model/date_now-namefile.extesion'), Null, Blank| campo de imagem | /collection/2018_01_30-ligia_fagundes_teles.jpg|


###  Conjunto (`sets`)*

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`uuid`     | UUIDField, **PK**, Unique, Sequential                             | Identificador único universal do Conjunto |  123e4567-e89b-12d3-a456
`id`       | CharField(64), Unique, Null, Blank | Identificador único  atribuído a cada Conjunto para controle interno da instituição. Esse valor tem de ser editável |  001002
`aggregation_type` | AggregationType **FK**[0..1], Null, Blank                  | Tipologia do conjunto |  Arquivo
`title`    | CharField(128), Null, Blank                                       | Título do conjunto |  Arquivo pessoal de Marcel Gautherot
`abstract` | TextField, Null, Blank | Breve apresentação do conjunto           |  Formado a partir da produção autoral do fotógrafo...
`items`    | Item, **FK** [0..\*] | Lista de itens que integram a coleção | Item 1, Item 2
`description_level` | DescriptionLevel, **FK** [0..1]                          | Nível de descrição da Coleção | 1 - Descrição Básica
`sets_child`| Sets **FK**[0..\n], Null, Blank | conjuntos filhos deste conjunto | conjunto 1, conjunto 2


* O nome `sets` deve ser utilizado para no plural para não conflitar com a palavra reservada `set`.

###  Item (`item`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|----------
`uuid`  | UUIDField, **PK**, Unique, Sequential  | Identificador único universal do Conjunto |  123e4567-e89b-12d3-a456
`id`    | CharField(64), Unique, Null, Blank | Identificador único  atribuído a cada Conjunto para controle interno da instituição. Esse valor tem de ser editável |  001002
`title` | CharField(128), Null, Blank | nome do item. | Foto Ligia Fagundes Telles em visita ao IMS


### Condições de Acesso (`AccessCondition`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|----------
`id`          | **PK**, Unique, Sequential  | Identificador de cada registro |
`title_short` | CharField(64), Unique, Null, Blank | Identificador textual único da condição de acesso |  Livre
`title_long`  | CharField(128), Null, Blank | Título longo da condição de acesso |  Acesso pleno
`description`| TextField, Null, Blank | Descrição completa da condição de acesso | Todos os documentos originais ou seus representantes digitais estão disponíveis para consulta.

Exemplos de instâncias que vão constar neste modelo:

ID      | Access    | title            | description         |
--------|-----------|------------------|---------------------|
0       | Livre     | Acesso pleno     | Todos os documentos originais ou seus representantes digitais estão disponíveis para consulta.
1       | Parcial   | Em processamento | Existem documentos em processamento técnico (inventário, identificação, ordenação, higienização, acondicionamento, digitalização ou restauro) ou em uso (empréstimo para exposições ou em consulta por outros pesquisadores).
2       | Parcial   | Estado de conservação | Existem documentos cujo estado de conservação coloca em risco a estabilidade ou a própria existência dos mesmos.
3       | Restrito  | Direito autoral  | Existem restrições ao acesso aos documentos por questões de direito autoral. O pesquisador pode solicitar acesso mediante autorização expressa do titular, herdeiro ou detentor dos referidos direitos.
4       | Restrito  | Contratual       | Existem restrições ao acesso aos documentos por questões contratuais definidas por cláusulas especificadas no processo de aquisição.
5       | Restrito  | Segurança institucional | Existem restrições ao acesso aos documentos por questões de risco à seguraça operacional. Aplica-se exclusivamente a documentos do arquivo institucional.
6       | Restrito  | Informação privada | Existem restrições ao acesso aos documentos por questões de privacidade envolvendo informações de cunho extritamente privado de terceiros.


### Áreas de Gestão (`ManagementUnit`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|----------
`id`       | **PK**, Unique, Sequential  | Identificador de cada registro | 001
`title` | CharField(128), Null, Blank | Título da unidade de gerenciamento |  Coordenação de Acervos
`description`| TextField, Null, Blank | Descrição completa da unidade de gerenciamento | A coordenação de Acervos tem o papel de...

Exemplos de instâncias que vão constar neste modelo:

ID | Title     | description    |
---|-----------|----------------|
01 | Coordenação de Acervo      | A coordenação de Acervos tem o papel de...
02 | Coordenação de Bibliotecas |
03 | Coordenação de Cinema      |
04 | Coordenação de Fotografia  |
05 | Coordenação de Iconografia |
06 | Coordenação de Literatura  |
07 | Coordenação de Música      |

--------

## Exposição

Uma Exposição pode ter diversas Edições:

```
| -- Exposição
    | -- Edição 1
    | -- Edição 2
| -- Exposição
    | -- Edição 1
```

###  Exposição (`exhibition`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`uuid`        | UUID    | Identificador único universal da Exposição |     123e4567-e89b-12d3-a456-426655440000
`id`          | CharField(64), upppercase, obrigatorio  | Identificador único numérico atribuído a cada Exposição para controle interno da instituição | 0326
`title`       | String  | Título completo da Exposição | Conflitos: fotografia e violência política no Brasil
`slug`        | String  | Apelido curto e intuitivo para construção de atalhos e URLs  | Conflitos
`abstract`    | String  | Breve resumo da Exposição escrito em Markdown | A exposição procura contradizer a imagem do Brasil como país pacífico e oferece um olhar sobre a história nacional que colabora...
`date_start`  | Data    | Data da primeira abertura da Exposição | 25/11/2017
`date_end`    | Data    | Data do último encerramento da Exposição  | 25/02/2018
`location`    | FK  | Local de realização da Edição | IMS Paulista
`url`         | String  | Endereço web da Exposição do site da instituição | museu.edu/expo/conflitos
`team`        | JSON    | Ficha técnica geral da Exposição, com a atribuição da equipe principal | {"Curadoria": "Heloisa Espada", "Assistente de Curadoria": "Tiê Higashi"}
`edition`     | FK
`catalog`     | publication, FK [0..\*]
`publication` | publication, FK [0..\*]

###  Edições (`exhibition_edition`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`uuid`         | UUID    | Identificador único universal da Exposição |     123e4567-e89b-12d3-a456-426655440000
`id`           | Número  | Identificador único da Edição composto com ExhibitionNumber |  0326-02
`èxhibition`   | FK, exhibition
`title`        | CharField
`location`     | FK  | Local de realização da Edição | IMS Paulista
`date_start`   | Data    | Data de abertura da Edição, quando conhecida | 02/05/2018
`date_end`     | Data    | Data de encerramento da Edição, quando conhecida  | 02/08/2018
`team`         | JSON    | Ficha técnica específica da Edição, com a atribuição de toda equipe envolvida | {"Produção": "Equipe"; "Montagem": "Equipe"}

## Localização (`location`)

Armazena informações sobre sedes e/ou locais onde ocorre armazenamento, exposição, exibição ou evento de qualquer outra atividade de natureza diversa vinculada a instituição.

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|---------
`id`         | **PK**, Unique, Sequential  | Identificador de cada espaço | 001
`title`      | CharField(128), Null, Blank | Nome do Espaço | IMS Paulista
`street`     | CharField(128), Null, Blank | Logradouro do Espaço | Rua ...
`number`     | CharField(32), Null, Blank | Número do Logradouro do Espaço | 32
`complement` | CharField(128), Null, Blank | Complemento do endereço | Rua ...
`neighborhood`| CharField(64), Null, Blank | Bairro | Consolação
`state`      | CharField(64), Null, Blank | Estado | São Paulo
`city`       | CharField(64), Null, Blank | Cidade | São Paulo
`country`    | CharField(64), Null, Blank | País   | Brasil
`postal_code`| CharField(32), Null, Blank | CEP    | 01200-000
`lat_and_long`| PointField, Null, Blank   | Ponto geográfico de latitude e longitude | 85.3240, 27.7172,srid=4326

--------
## Publicação (`publication`)

- Diferença entre `Publicação` e folheteria:
  - Considerar que uma publicação é todo projeto editorial consolidado num produto comercial. Ex.: livro, catálogo de exposição, DVD, etc. Já a folheteria distribuída gratuítamente não será considerada uma publicação autônoma, mas um documento anexado a outra entidade.
- **Exemplos**
  - Uma `Publicação` _Catálogo da Exposição_ está relacionada a uma `Exposição`
  - Um `Evento` _Mostra de Cinema_ tem como documentação anexa um folder da sua programação

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`uuid`         | UUID      | Identificador único universal da Publicação |  123e4567-e89b-12d3-a456-426655440000
`id`           | Número    | Identificador único numérico atribuído a cada Publicação para controle interno da instituição | 201803
`title`        | String    | Título completo da Publicação | Marc Ferrez
`slug`         | String    | Título curto da Publicação | Marc Ferrez
`abstract`     | String    | Breve resumo da Publicação escrito em Markdown | A exposição procura contradizer a imagem do Brasil como país pacífico e oferece um olhar sobre a história nacional que colabora...
`full_text`    | CharField
`author`       | Author, **FK**[0..\*]  |
`date_release` | Date   | Data de publicação | 02/08/2014
`publisher`    | Person, **FK**[0..\*]   | Nome da editora | Companhia das Letras
`dimension`    | JSON   | Dimensão da publicação em centímetros | {"largura": "10", "altura": "10", "prof": "10"}
`pages`        | number | quando tiver pages exibir, senão não exibir
`type`         | fk |  | Homem
`òther_data`


--------

## Evento (`event`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`uuid`          | UUID    | Identificador único universal do Evento |  0326-02
`id`            | Número  | Identificador único do Evento para controle interno da instituição |  0326-02
`title`         | String  | Título do evento | Palestra do fulano de tal
`slug`          | String  | Título intuitivo do evento | IMS Paulista
`date_start`    | Data    | Data de início do Evento, quando conhecida | 02/05/2018
`date_start`    | Data    | Data de fim do Evento, quando conhecida  | 02/08/2018
`type`          | fk      | Tipo do Evento  | Palestra
`location`      | fk      | Local de realização do Evento  | Museu de Arte
`abstract`      | String  | Breve apresentação do Evento | IMS Paulista
`full_text`     | String  | ... | ...
`team`          | JSON    | Ficha técnica específica do Evento | {"Palestrante": "Equipe", "Filmagem": "Equipe"}
`other_data`    | JSON    | Dados não estruturados      | ...


## Tipo de Evento (`event_type`)

ID   | Name          | Helptext     |
-----|---------------|--------------|
1    | Curso         | ... |
2    | Palestra      | ... |
3    | Show          | ... |
4    | Lançamento    | ... |
5    | Etc...        | ... |


--------

## Pessoa (`person`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`uuid`        | UUID   | Identificador único universal da Pessoa no banco de dados da instituição |  123e4567-e89b-12d3-a456-426655440000
`id`          | id    
`person_type` |
`title`         |
`title_index`   | title de citações
`slug`          | String | Nome da pessoa para exibição pública | Marc Ferrez
`date_start`    | Date   | Data de nascimento da pessoa | 07/12/1843
`date_end`      | Date   | Data de morte da pessoa | 12/01/1923
`gender`        | String | Gênero da Pessoa (binário) | Homem
`nation_origin` | String | País de atuação, frequentemente distinto do país de origem | Brasileiro
`nation_main`   | String | País de atuação, frequentemente distinto do país de origem | Brasileiro
`activity_main` | FK | Principal papel profissional de atuação  | Fotógrafo
`abstract`      | String | Biografia curta da Pessoa | Principal fotógrafo brasileiro do século XIX, dono de uma obra que se equipara à dos maiores nomes da fotografia em todo o mundo, Marc Ferrez é o mais significativo fotógrafo do período...
`full_text`     | String | Biografia completa da Pessoa | Principal fotógrafo brasileiro do século XIX, dono de uma obra que se equipara à dos maiores nomes da fotografia em todo o mundo, Marc Ferrez é o mais significativo fotógrafo do período... ...
`url`           | String | Endereço web da Pessoa no site da instituição | museu.edu/pessoa/marc-ferrez
`lod`           | JSON   | Linked open Data Dicionário de UIDs em projetos de Linked Open Data, como Virtual International Authority File (VIAF), Wikidata (WIKI), Union List of Artist Names (ULAN) ou Photographers’ Identities Catalog (PIC) | {"VIAF": "69111120", "WIKI": "Q3180571", "ULAN": "500037201", "PIC": "1758"}

--------

## Aquisição (`acquisition`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`uuid`       | UUIDField  | ...        | ...
`title`      |
`method`     | AcquisitionMethod, FK | ...  | ...
`source`     | Person 1-* | ...        | ...
`dealer`     | Person, fk 1-* | quem negociou o ativo   | ...
`date_start` | DateField  | ...        | ...
`date_end`   | DateField  | usado em comodato        | ...
`abstract`   | TextField  | ...        | ...
`full text`  |
`other_data` | JSONField  | ...        | ...


### AcquisitionMethod

ID   | Name           | Helptext     |
-----|----------------|--------------|
1    | Compra         | Transferência de propriedade com remuneração |
2    | Doação         | Transferência de propriedade sem remuneração |
3    | Comodato       | Empréstimo temporário com prazo determinado |
4    | Transferência  | Mudança de unidade administrativa dentro da mesma instituição |

--------

## Procedimento (`procedure`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`uuid`       | UUID    | Identificador único universal do Procedimento | ...
`id`         | Número  | Identificador único do Procedimento (human-readable) | ...
`title`      | String  | Título do Procedimento | Aquisição de Coleção
`slug`       | String  | Título intuitivo do evento | aquisicao-colecao
`abstract`   | TextField  | Resumo do Procedimento      | ...
`full text`  | TextField  | Descrição do Procedimento   | ...
`other_data` | JSONField  | Dados não estruturados      | ...

--------


## Adopted References
* Django Default Fields https://docs.djangoproject.com/en/2.0/ref/models/fields/
* Django Geo Field https://docs.djangoproject.com/en/2.0/ref/contrib/gis/model-api/


## Declined References
* Django Hash Field
https://github.com/amcat/django-hash-field (It is not necessary, there is a native hash uuid field on django)

* Django Hstore Third part
http://django-hstore.readthedocs.io/en/latest/ (Project with no suport any more. Take a look on issue 161. It was solved with native hstore django field and hstore widget)

* Django Hstore Native
https://docs.djangoproject.com/en/2.0/ref/contrib/postgres/fields/#django.contrib.postgres.fields.HStoreField

* Hstore Widget
https://github.com/PokaInc/django-admin-hstore-widget

* Django Json Field
* Django Json Widget - https://github.com/jmrivas86/django-json-widget, https://pypi.org/project/django-json-widget (It could be useful on future, but at moment we are using hstore)
* Django Pretty Json http://kevinmickey.github.io/django-prettyjson (Good for programmers and geeks, bad to all others)


Experimentar:
https://github.com/tooreht/django-jsonsuit
https://github.com/mbraak/django-mptt-admin
https://github.com/mbi/django-rosetta
