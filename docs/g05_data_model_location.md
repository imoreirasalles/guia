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
