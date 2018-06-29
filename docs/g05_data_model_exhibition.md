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
