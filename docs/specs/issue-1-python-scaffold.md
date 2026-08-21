# Issue #1 - Scaffold Python e dependencias do MVP

## Objetivo

Criar a fundacao minima do projeto Python para permitir evolucao incremental do
MVP sem implementar ainda os fluxos de produto.

Esta issue corresponde ao primeiro recorte tecnico do projeto: estrutura de
pacotes, ponto de entrada, dependencias de runtime e instrucoes basicas de uso.

## Escopo realizado

Foram criados:

- pacote principal `app/`;
- ponto de entrada `app/main.py`;
- subpacotes de responsabilidade:
  - `app/ui/`;
  - `app/models/`;
  - `app/physics/`;
  - `app/plotting/`;
  - `app/export/`;
- pasta `examples/`;
- `requirements.txt`;
- `.gitattributes`;
- atualizacao do `README.md`.

## Fora de escopo

- Interface Tkinter funcional.
- Modelos de dados do dominio.
- Calculos fisicos.
- Regressao linear.
- Geracao de graficos.
- Exportacao PNG.
- Testes automatizados.

## Contratos estabelecidos

### Estrutura de pacotes

O codigo da aplicacao deve viver dentro de `app/`, separado por responsabilidade.

Responsabilidades iniciais:

- `app/main.py`: entrada da aplicacao.
- `app/ui/`: interface desktop.
- `app/models/`: modelos de dados compartilhados.
- `app/physics/`: calculos fisicos e incertezas.
- `app/plotting/`: montagem de graficos.
- `app/export/`: exportacao de artefatos.

### Execucao

O projeto deve ser executavel por modulo:

```bash
python -m app.main
```

Esse formato preserva imports internos melhores do que executar arquivos soltos.

### Dependencias de runtime

`requirements.txt` deve conter apenas dependencias necessarias para rodar a
aplicacao:

- NumPy;
- SciPy;
- Matplotlib.

Tkinter nao entra no `requirements.txt` porque normalmente acompanha a
instalacao do Python.

## Decisoes

- Usar Python 3.12+.
- Manter o entrypoint minimo ate a issue da interface.
- Separar a arquitetura desde o inicio em interface, dominio fisico, plotagem e
  exportacao.
- Usar `.gitattributes` para reduzir ruido de final de linha entre sistemas.

## Criterios de aceite

- A estrutura de diretorios existe.
- `requirements.txt` lista as dependencias de runtime da spec principal.
- `README.md` explica instalacao e execucao.
- `python -m app.main` executa o entrypoint minimo.

## Validacao executada

Depois da instalacao do Python 3.12.10 e criacao da `.venv`, foi validado:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m app.main
```

Resultado esperado observado:

```text
Helper Fisica - Gerador de Graficos para Fisica Experimental 2
```

## Rastreabilidade

- Issue: https://github.com/rafa3lPinheiro/helper-fisica/issues/1
- PR: https://github.com/rafa3lPinheiro/helper-fisica/pull/17
- Commit em `main`: `chore: scaffold python project`
- Spec principal: `docs/specs/mvp-ondas-corda.md`, secoes 5, 6, 21 e 22.

