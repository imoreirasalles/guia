## USER Specs

O sistema possui 5 diferentes tipos de usuários, com as seguintes especificações de acesso ordenadas do maior ao menor espectro de controle interno.


#### 1. Super Administrador `superadmin`
  - EXIGE autenticação para operar;
  - Tem controle total sobre todo o sistema;
  - Possui acesso tanto pelo django admin quanto por templates;
  - Só deve ser criado via manage.py command line;
  - Apenas usuários com conhecimento técnico adequado e permissão de manipulação ampla de dados institucionais deve operar;
  - Pode criar demais usuários;


#### 2. Coordenador `coordinator`
  - EXIGE autenticação para operar;
  - Possui acesso tanto pelo django admin quanto por templates;
  - Insere, edita e publica uma `collection` associadas a sua coordenação ou a coordenações concedidas;


#### 3. Gestor de Contratos `contractmanager`
  - EXIGE autenticação para operar;
  - Possui acesso tanto pelo django admin quanto por templates;
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
