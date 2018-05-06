## USER Specs

O sistema possui 5 diferentes tipos de usuários, com as seguintes especificações de acesso ordenadas do maior ao menor espectro de controle interno.

#### 1. Super Administrador `superadmin`
  - EXIGE autenticação para operar;
  - Tem controle total sobre todo o sistema;
  - Só deve ser criado via manage.py command line;
  - Apenas usuários com conhecimento técnico adequado e permissão de manipulação ampla de dados institucionais deve operar;
  - Pode criar demais usuários;

#### 2. Coordenador `coordinator`
  - EXIGE autenticação para operar;
  - Insere, edita e publica `collections` associadas a sua coordenação ou a coordenações concedidas;

#### 3. Pesquisador `researcher`
  - EXIGE autenticação para operar;

#### 4. Colaborador `collaborator`
  - EXIGE autenticação para operar;

#### 5. Anômimo `anonymous`
  - NÃO EXIGE autenticação para operar;
  - Acessa apenas as páginas públicas do sistema;




Um `Pesquisador` acessa o painel administrativo sem permissão para edição.
