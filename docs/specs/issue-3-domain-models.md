# Issue #3 - Modelos de dados do dominio

## Objetivo

Criar os modelos de dados basicos que serao compartilhados pelo nucleo
cientifico, geracao de graficos, exportacao e interface.

Esta issue implementa os dataclasses descritos na spec principal:

- `FitResult`
- `PlotData`
- `ExportConfig`

## Escopo

Criar modelos independentes da UI em `app/models/`.

Arquivos esperados:

- `app/models/fit_result.py`
- `app/models/plot_data.py`
- `app/models/export_config.py`
- `app/models/__init__.py`

Os modelos devem permitir imports publicos assim:

```python
from app.models import ExportConfig, FitResult, PlotData
```

## Fora de escopo

- Validacao completa de dados experimentais.
- Calculos fisicos.
- Propagacao de incertezas.
- Ajuste linear.
- Geracao de graficos.
- Interface Tkinter.
- Exportacao PNG.

## Contratos de dominio

### FitResult

Representa o resultado de uma regressao linear.

Campos:

- `slope: float`
- `slope_uncertainty: float`
- `intercept: float`
- `intercept_uncertainty: float`
- `r_squared: float`

### PlotData

Representa os dados ja transformados para plotagem.

Campos:

- `x: np.ndarray`
- `y: np.ndarray`
- `x_uncertainty: Optional[np.ndarray]`
- `y_uncertainty: Optional[np.ndarray]`
- `x_label: str`
- `y_label: str`
- `title: str`

Incertezas podem ser `None` quando o usuario nao informar os valores
necessarios para barras de erro.

### ExportConfig

Representa a configuracao de tamanho e resolucao da imagem exportada.

Campos e valores padrao:

- `width_px: int = 1600`
- `height_px: int = 1000`
- `dpi: int = 300`

## Decisoes

- Os modelos devem ser dataclasses simples.
- Os modelos nao devem depender de Tkinter, Matplotlib ou callbacks da UI.
- `PlotData` pode depender de NumPy porque a spec principal define arrays NumPy
  como contrato entre calculo e plotagem.
- Validacoes de dominio ficam para camadas futuras, para nao misturar estrutura
  de dados com regras de entrada do usuario.

## Criterios de aceite

- Os tres dataclasses existem nos modulos esperados.
- Os modelos sao importaveis por `from app.models import ...`.
- `ExportConfig()` retorna os defaults da spec.
- `FitResult` armazena corretamente os parametros do ajuste.
- `PlotData` aceita arrays NumPy e incertezas opcionais.
- A suite de testes passa com `python -m pytest`.

## Testes esperados

Criar testes unitarios em `tests/models/` cobrindo:

- defaults de `ExportConfig`;
- atribuicao de valores em `FitResult`;
- criacao de `PlotData` com incertezas `None`;
- criacao de `PlotData` com arrays de incerteza.

## Dependencias

- Issue #1: scaffold Python do projeto.
- Issue #2: setup basico de testes com Pytest.
- Spec principal: `docs/specs/mvp-ondas-corda.md`, secao 15.

