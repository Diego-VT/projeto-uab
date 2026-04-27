# Plano de Testes - TDD

## Projeto

Sistema Web de Controle de Empréstimos de Equipamentos

## Objetivo

Este documento define o plano de testes do projeto, seguindo a abordagem TDD (Test-Driven Development), em que os testes são planejados antes da implementação das funcionalidades principais.

## Ferramentas de Teste

- pytest
- Flask test client
- SQLite em ambiente de teste

## Estratégia

Os testes serão automatizados e organizados por funcionalidade. O foco inicial será validar os fluxos principais do sistema, evitando regressões durante o desenvolvimento.

---

## 1. Testes de Ambiente

### CT001 - Verificar se a aplicação inicia corretamente

**Objetivo:** garantir que a aplicação Flask é criada sem erros.

**Entrada:** chamada da função `create_app()`.

**Resultado esperado:** aplicação Flask criada com sucesso.

---

### CT002 - Verificar rota inicial

**Objetivo:** garantir que a página inicial responde corretamente.

**Entrada:** requisição GET para `/`.

**Resultado esperado:** status HTTP 200.

---

## 2. Testes de Autenticação

### CT003 - Acessar página de login

**Objetivo:** verificar se a tela de login está disponível.

**Entrada:** requisição GET para `/login`.

**Resultado esperado:** status HTTP 200.

---

### CT004 - Login com credenciais válidas

**Objetivo:** permitir acesso ao sistema com usuário e senha corretos.

**Entrada:** e-mail e senha válidos.

**Resultado esperado:** usuário autenticado e redirecionado para o painel.

---

### CT005 - Login com credenciais inválidas

**Objetivo:** bloquear acesso com dados incorretos.

**Entrada:** e-mail ou senha inválidos.

**Resultado esperado:** mensagem de erro e permanência na tela de login.

---

### CT006 - Logout

**Objetivo:** encerrar sessão do usuário.

**Entrada:** usuário autenticado acessa `/logout`.

**Resultado esperado:** sessão encerrada e redirecionamento para login.

---

## 3. Testes de Usuários

### CT007 - Cadastro de usuário solicitante

**Objetivo:** permitir criação de usuário solicitante.

**Entrada:** nome, e-mail e senha.

**Resultado esperado:** usuário salvo no banco com perfil solicitante.

---

### CT008 - Bloquear cadastro com e-mail duplicado

**Objetivo:** evitar usuários com mesmo e-mail.

**Entrada:** tentativa de cadastro com e-mail já existente.

**Resultado esperado:** sistema exibe erro e não duplica o registro.

---

## 4. Testes de Categorias

### CT009 - Cadastro de categoria

**Objetivo:** permitir cadastro de categoria de equipamento.

**Entrada:** nome da categoria.

**Resultado esperado:** categoria salva no banco.

---

### CT010 - Listagem de categorias

**Objetivo:** exibir categorias cadastradas.

**Entrada:** acesso à rota de categorias.

**Resultado esperado:** lista de categorias apresentada ao usuário.

---

## 5. Testes de Equipamentos

### CT011 - Cadastro de equipamento

**Objetivo:** permitir cadastro de equipamento.

**Entrada:** nome, patrimônio, descrição e categoria.

**Resultado esperado:** equipamento salvo com status disponível.

---

### CT012 - Bloquear patrimônio duplicado

**Objetivo:** impedir dois equipamentos com o mesmo número de patrimônio.

**Entrada:** cadastro com patrimônio já existente.

**Resultado esperado:** sistema exibe erro e não salva duplicidade.

---

### CT013 - Listagem de equipamentos disponíveis

**Objetivo:** listar apenas equipamentos disponíveis para empréstimo.

**Entrada:** acesso à página de equipamentos disponíveis.

**Resultado esperado:** equipamentos disponíveis exibidos corretamente.

---

## 6. Testes de Empréstimos

### CT014 - Solicitar empréstimo

**Objetivo:** permitir que um solicitante solicite um equipamento disponível.

**Entrada:** usuário solicitante e equipamento disponível.

**Resultado esperado:** empréstimo criado com status pendente.

---

### CT015 - Aprovar solicitação

**Objetivo:** permitir que responsável aprove uma solicitação.

**Entrada:** responsável aprova empréstimo pendente.

**Resultado esperado:** empréstimo muda para aprovado e equipamento fica indisponível.

---

### CT016 - Rejeitar solicitação

**Objetivo:** permitir rejeição de solicitação.

**Entrada:** responsável rejeita empréstimo pendente.

**Resultado esperado:** empréstimo muda para rejeitado e equipamento permanece disponível.

---

### CT017 - Registrar devolução

**Objetivo:** registrar devolução de equipamento emprestado.

**Entrada:** responsável confirma devolução.

**Resultado esperado:** empréstimo muda para devolvido e equipamento fica disponível.

---

## 7. Testes de Permissão

### CT018 - Bloquear acesso sem login

**Objetivo:** impedir acesso a áreas protegidas.

**Entrada:** usuário não autenticado acessa rota protegida.

**Resultado esperado:** redirecionamento para login.

---

### CT019 - Bloquear ação de solicitante em área administrativa

**Objetivo:** impedir que solicitante cadastre equipamentos.

**Entrada:** usuário solicitante acessa rota administrativa.

**Resultado esperado:** acesso negado.

---

### CT020 - Permitir acesso administrativo ao administrador

**Objetivo:** permitir que administrador acesse área de gestão.

**Entrada:** usuário administrador autenticado.

**Resultado esperado:** acesso permitido.

---

## 8. Testes de Relatórios

### CT021 - Relatório de equipamentos emprestados

**Objetivo:** listar equipamentos atualmente emprestados.

**Entrada:** acesso ao relatório.

**Resultado esperado:** sistema apresenta equipamentos com empréstimos ativos.

---

### CT022 - Relatório de histórico de empréstimos

**Objetivo:** apresentar histórico geral de empréstimos.

**Entrada:** acesso ao relatório histórico.

**Resultado esperado:** sistema exibe empréstimos concluídos, pendentes, aprovados e rejeitados.

---

## 9. Priorização dos Testes

| Prioridade | Casos de Teste |
|---|---|
| Alta | CT001, CT002, CT003, CT004, CT005, CT014, CT015, CT017, CT018 |
| Média | CT007, CT008, CT011, CT012, CT019, CT020 |
| Baixa | CT009, CT010, CT013, CT016, CT021, CT022 |

## 10. Execução dos Testes

Os testes automatizados serão executados com:

```bash
pytest
