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
