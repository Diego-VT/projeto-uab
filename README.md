# Projeto UAB

Ambiente de desenvolvimento Flask configurado no Linux (WSL).

## Como rodar o projeto

1. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```

2. Instale as dependências (caso não tenha feito):
   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```bash
   python run.py
   ```
   Acesse em `http://127.0.0.1:5000`

## Testes

Para rodar os testes:
```bash
pytest
```

## Linting e Formatação

- Para formatar o código com Black:
  ```bash
  black .
  ```
- Para verificar erros com Flake8:
  ```bash
  flake8 .
  ```
