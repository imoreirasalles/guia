## Gestão (`management`)

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

### Aquisição (`acquisition`)

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
`full_text`  |
`other_data` | JSONField  | ...        | ...


### AcquisitionMethod

ID   | Name           | Helptext     |
-----|----------------|--------------|
1    | Compra         | Transferência de propriedade com remuneração |
2    | Doação         | Transferência de propriedade sem remuneração |
3    | Comodato       | Empréstimo temporário com prazo determinado |
4    | Transferência  | Mudança de unidade administrativa dentro da mesma instituição |

--------

### Procedimento (`procedure`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`uuid`       | UUID    | Identificador único universal do Procedimento | ...
`id`         | Número  | Identificador único do Procedimento (human-readable) | ...
`title`      | String  | Título do Procedimento | Aquisição de Coleção
`slug`       | String  | Título intuitivo do evento | aquisicao-colecao
`abstract`   | TextField  | Resumo do Procedimento      | ...
`full_text`  | TextField  | Descrição do Procedimento   | ...
`other_data` | JSONField  | Dados não estruturados      | ...

