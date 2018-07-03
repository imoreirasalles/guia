Este modelo de dados está em construção, tendo como referência projetos como a [NYPL Digital Collections](http://api.repo.nypl.org/#data-model), o [MoMA Exhibition History](https://github.com/MuseumofModernArt/exhibitions) e o [Getty ULAN](https://www.getty.edu/research/tools/vocabularies/ulan/about.html).

![Modelo UML](images/ims_collections_guide_uml.png)

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
`containers`| Container **FK**[0..\n], Null, Blank | conjuntos | conjunto 1, conjunto 2
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

### Galeria de apresentação (`Thumbnail`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`uuid`     | UUIDField, **PK**, Unique, Sequential | Identificador único universal do objeto  | 123e4567-e89b-12d3-a456-426655440000
`created`  | dateField, NotNull, default=now | data de criação do registro | 01/01/2018
`title`    | CharField(128), NotNull, Blank, | título do registro | Foto Lígia Fagundes Teles
`image`    | ImageField(upload_to='/model/date_now-namefile.extesion'), Null, Blank| campo de imagem | /collection/2018_01_30-ligia_fagundes_teles.jpg|


###  Conjunto (`Container`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`uuid`     | UUIDField, **PK**, Unique, Sequential                             | Identificador único universal do Conjunto |  123e4567-e89b-12d3-a456
`id`       | CharField(64), Unique, Null, Blank | Identificador único  atribuído a cada Conjunto para controle interno da instituição. Esse valor tem de ser editável |  001002
`aggregation_type` | AggregationType **FK**[0..1], Null, Blank                  | Tipologia do conjunto |  Arquivo
`title`    | CharField(128), Null, Blank                                       | Título do conjunto |  Arquivo pessoal de Marcel Gautherot
`abstract` | TextField, Null, Blank | Breve apresentação do conjunto           |  Formado a partir da produção autoral do fotógrafo...
`items`    | Item, **FK** [0..\*] | Lista de itens que integram a coleção | Item 1, Item 2
`description_level` | DescriptionLevel, **FK** [0..1]                          | Nível de descrição da Coleção | 1 - Descrição Básica
`containers`| Container **FK**[0..\n], Null, Blank | conjuntos filhos deste conjunto | conjunto 1, conjunto 2


###  Item (`Item`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|----------
`uuid`  | UUIDField, **PK**, Unique, Sequential  | Identificador único universal do Conjunto |  123e4567-e89b-12d3-a456
`id`    | CharField(64), Unique, Null, Blank | Identificador único  atribuído a cada Conjunto para controle interno da instituição. Esse valor tem de ser editável |  001002
`title` | CharField(128), Null, Blank | nome do item. | Foto Ligia Fagundes Telles em visita ao IMS
`captures` | Capture **FK**[0..\n], Null, Blank | conjuntos filhos deste conjunto | conjunto 1, conjunto 2

###  Captura (`Capture`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|----------
`uuid`  | UUIDField, **PK**, Unique, Sequential  | Identificador único universal da captura |  123e4567-e89b-12d3-a456

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