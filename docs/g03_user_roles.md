## USER Specs

O sistema possui 5 diferentes tipos de usuários, com as seguintes especificações de acesso ordenadas do maior ao menor espectro de controle interno.


#### 1. Super Administrador `superadmin`
  - EXIGE autenticação para operar;
  - Tem controle total sobre todo o sistema;
  - Apenas usuários com conhecimento técnico adequado e permissão de manipulação ampla de dados institucionais deve operar;
  - Pode criar qualquer um dos demais usuários;


#### 2. Coordenador `coordinator`
  - EXIGE autenticação para operar;
  - Insere, edita e publica uma `collection` associadas a sua coordenação ou a coordenações concedidas;

##### 2.1 Coordenador de Programação `exhibitor`
  - EXIGE autenticação para operar;
  - Função principal é aprovar Eventos que estejam em uma fila;

##### 2.2 Coordenador Editorial `publisher`
- EXIGE autenticação para operar;
- Função principal é aprovar Publicações que estejam em uma fila;

#### 3. Gestor de Contratos `contractmanager`
  - EXIGE autenticação para operar;
  - Insere, edita e publica `contract`;


#### 4. Pesquisador `researcher`
  - EXIGE autenticação para operar;
  - Possui acesso tanto pelo django admin quanto por templates;
  - NÃO insere, NÃO edita, NÃO publica dados, faz apenas consultas;


#### 5. Colaborador `collaborator`
  - EXIGE autenticação para operar;
  - Possui acesso tanto pelo django admin quanto por templates;
  - Insere, edita e publica `collections` associadas a sua coordenação;


#### 5. Anômimo `anonymous`
  - NÃO EXIGE autenticação para operar;
  - NÃO possui acesso ao Painel Django Admin;
  - Acessa apenas as páginas públicas do sistema;

### Sobre a lógica de acesso

Um coordenador pode criar instâncias de qualquer classe (`Collection`, `Publication`, `Event`, ou outra coisa), e só poderá editar as instâncias que estão sob sua responsabilidade. Um colaborador pode participar de mais de uma equipe, e editar aquilo que está sob responsabilidade de seus coordenadores.

Talvez a questão de quem tem acesso aos dados administrativos também possa ser respondida dessa maneira, centralizando essa organização em um _Coordenador Administrativo_. Ficaria assim:

  - Coordenador Acervo (edita qualquer `Coleção`)
    - Coordenador Fotografia
       - Colaborador A
       - Colaborador B
    - Coordenador Fotografia Contemporânea
       - Colaborador C
       - Colaborador D
    - Etc..
  - Coordenador Exposição (edita qualquer `Exposição`)
  - Coordenador Publicação (edita qualquer `Publicação`)
  - Coordenador Evento (edita qualquer `Evento`)
  - Coordenador Administrativo (visualiza tudo, mas edita apenas dados sensíveis)
       - Colaborador E
       - Colaborador F
