###  Item (`Item`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|----------
`uuid`     | UUIDField, **PK**, Unique, Sequential | Identificador único universal |  123e4567-e89b-12d3-a456
`created`  | DateTimeField, NotNull, default=now   | Cata de criação do registro | 01/01/2018
`id`       | CharField(64), Unique, Null, Blank    | Código atribuído ao Conjunto para controle interno da instituição. Esse valor tem de ser editável |  001002
`collection_mother` | Collection **FK**[0..1], NotNull    | Coleção mãe desse Conjunto  | Coleção Gilberto Ferrez
`container_mother`  | Container **FK**[0..1], Null, Blank | Conjunto mãe desse Conjunto | Arquivo Marc Ferrez
`title`    | CharField(128), Null, Blank | nome do item. | Foto Ligia Fagundes Telles em visita ao IMS
`author`   | CharField(128), Null, Blank | nome do item. | Foto Ligia Fagundes Telles em visita ao IMS
`date_start`         | DateField, Null, Blank         | Data inicial | 02/08/2018
`date_start_caption` | CharField(128), Null, Blank    | Legenda data inicial | c. 2018
`date_end`           | DateField, Null, Blank         | Data final   | 02/08/2018
`date_end_caption`   | CharField(128), Null, Blank    | Legenda data final | c. 2020
`captures` | Capture **FK**[0..\n], Null, Blank | conjuntos filhos deste conjunto | conjunto 1, conjunto 2


###  Captura (`Capture`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|----------
`created`  | dateField, NotNull, default=now | data de criação do registro | 01/01/2018
`uuid`     | UUIDField, **PK**, Unique, Sequential | Identificador único universal da captura |  123e4567-e89b-12d3-a456
`title`    | CharField(128), NotNull, Blank, | Título da captura | Cópia scaneada...
`file`     | UPLOAD Null, Blank | campo de Upload | Pode ser imagem, som, video... |
