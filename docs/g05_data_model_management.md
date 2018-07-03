## Gestão (`management`)

### Áreas de Gestão (`ManagementUnit`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|----------
`id`       | **PK**, Unique, Sequential  | Identificador de cada registro | 001
`created`                       | dateField, NotNull, default=now              | data de criação do registro | 01/01/2018
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

## Aquisição (`acquisition`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`uuid`       | UUIDField  | identificador universal do campo | 392409-dlsdaos-lsdskllsksDEW-0834932
`created`    | dateField, NotNull, default=now   | data de criação do registro | 01/01/2018
`title` | CharField(128), Null, Blank | Título da aquisição |  Compra da coleção...
`method`     | AcquisitionMethod, **FK**, Null, Blank | Método da Aquisição  | 01 - Compra
`source`     | Person, **FK** [1-* ], Null, Blank | Fonte da Aquisição    | João Antunes, filho do fotógrafo...
`dealer`     | Person, **FK** [1-* ] | quem negociou o ativo   | João da Silva
`date_start` | DateField, Null, Blank  | Data de inicio da negociação        | 01/01/2017
`date_end`   | DateField, Null, Blank  | Data de fim da negociação, uso especial em comodato   | 01/01/2017
`abstract`   | TextField  | parágrafo de resumo sobre a aquisição | "esta aquisição entrou para o acervo ims em..."
`full_text`  | TextField  | parágrafo de descrição completa sobre a aquisição | "realizada em 01/05/2016, esta aquisição..."
`other_data` | JSONField  | Dados não estruturados sobre a aquisição  | numero de peças: 500, fotos: 350, etc


### AcquisitionMethod

ID   | title          | description     |
-----|----------------|-----------------|
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
