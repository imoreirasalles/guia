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
`type`         | **FK**[0..1] | Livro | Cadernos de Literatura
`other_data`   | JSONField   | Informação sem estrutura definida. | {"Notas do bisneto do doador de segundo grau": "Lorem ipsum"}


###  Tipo de publicação (`PublicationType`)

Field Name | Django Type Field  | Field Description  | Example
-----------|--------------------|--------------------|------------
`created`  | DateTimeField, NotNull, default=now      | Data de criação do registro | 01/01/2018
`title`    | CharField(128), Null, Blank  | Título do tipo | Livro
`description` | TextField, Null, Blank | Breve descrição do tipo
