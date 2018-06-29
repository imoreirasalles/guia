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
