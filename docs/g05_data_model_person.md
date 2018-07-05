## Pessoa (`person`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`uuid`        | UUID   | Identificador único universal da Pessoa no banco de dados da instituição |  123e4567-e89b-12d3-a456-426655440000
`id`          | id    
`person_type` |
`title`         |
`title_index`   | title de citações
`is_staff`      | NullBooleanField, Null, Blank | campo boleano que identifica se uma pessoa é ou não parte do staff ampliado da organização | yes
`is_partner`    | NullBooleanField, Null, Blank | campo boleano que identifica se uma pessoa é ou não parceiro da intituição | yes
`is_feature`    | NullBooleanField, Null, Blank | campo boleano que identifica se uma pessoa é artista, fotografo, etc | yes
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
