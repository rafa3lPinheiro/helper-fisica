# Issue #2 - Qualidade basica do projeto

## Objetivo

Configurar uma base minima de testes para sustentar o desenvolvimento
incremental do nucleo cientifico do MVP.

Esta issue introduz Pytest e define o comando padrao de validacao local.

## Escopo realizado

Foram criados ou atualizados:

- `pyproject.toml`;
- `requirements-dev.txt`;
- `tests/test_main.py`;
- `README.md`.

## Fora de escopo

- Lint e formatacao automatica com Ruff.
- Type checking com MyPy.
- CI no GitHub Actions.
- Testes de calculos fisicos.
- Testes de interface Tkinter.
- Testes de geracao de imagem.

## Contratos estabelecidos

### Dependencias de desenvolvimento

Ferramentas usadas apenas para desenvolvimento ficam em `requirements-dev.txt`.

Esse arquivo referencia as dependencias de runtime:

```text
-r requirements.txt
pytest
```

Com isso, `requirements.txt` permanece focado no necessario para executar a
aplicacao.

### Configuracao do Pytest

`pyproject.toml` centraliza configuracoes do Pytest:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["."]
```

Significado:

- `testpaths`: os testes vivem em `tests/`;
- `pythonpath`: a raiz do projeto entra no caminho de importacao, permitindo
  imports como `from app.main import main`.

### Teste smoke inicial

O teste `tests/test_main.py` garante que o pacote e o entrypoint minimo sao
importaveis e executaveis.

## Decisoes

- Adicionar Pytest agora porque o nucleo cientifico exigira TDD simples e
  barato.
- Nao adicionar Ruff nesta etapa para evitar politica de estilo antes de haver
  codigo suficiente.
- Separar dependencias de runtime e desenvolvimento.

## Criterios de aceite

- `requirements-dev.txt` instala Pytest e dependencias do app.
- `pyproject.toml` configura a descoberta de testes.
- Existe pelo menos um teste smoke.
- A suite passa com `python -m pytest`.

## Validacao executada

Foi validado na `.venv` local:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest
```

Resultado observado:

```text
1 passed
```

## Rastreabilidade

- Issue: https://github.com/rafa3lPinheiro/helper-fisica/issues/2
- PR: https://github.com/rafa3lPinheiro/helper-fisica/pull/18
- Commit em `main`: `test: add baseline test setup`

