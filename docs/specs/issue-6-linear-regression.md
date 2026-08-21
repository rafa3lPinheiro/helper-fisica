# Spec da issue #6 - Regressao linear com incerteza

## Objetivo

Implementar o ajuste linear generico usado pelos tres graficos do MVP,
retornando coeficientes, incertezas dos parametros e `R2`.

## Escopo

Criar `app/physics/regression.py` com:

```python
linear_fit(x, y, sigma_y=None) -> FitResult
```

Usar `scipy.optimize.curve_fit` para ajustar:

```text
y = a * x + b
```

Expor `linear_fit` em `app.physics` e criar testes unitarios.

## Fora de escopo

- Validacao e conversao dos campos da UI.
- Geracao de graficos.
- Comparacao do coeficiente com valores teoricos.
- Formatacao textual dos parametros.
- Ajuste nao linear.

## Contratos de dominio

- `x` e `y` sao arrays NumPy unidimensionais com o mesmo tamanho.
- `sigma_y`, quando informado, e um array de incertezas verticais com o mesmo
  tamanho de `y`.
- Sem `sigma_y`, executar ajuste nao ponderado.
- Com `sigma_y`, usar as incertezas como `sigma` e `absolute_sigma=True`.
- A covariancia de `curve_fit` define as incertezas dos parametros:
  `sqrt(diag(pcov))`.
- `R2` deve ser calculado manualmente por `1 - SS_res / SS_tot`.
- O retorno e `FitResult(slope, slope_uncertainty, intercept,
  intercept_uncertainty, r_squared)`.

## Decisoes

- O modelo linear fica encapsulado no modulo de regressao.
- A funcao nao deve depender de UI, Matplotlib ou estado global.
- A camada de entrada sera responsavel por garantir quantidade minima de pontos
  e valores numericos validos.

## Criterios de aceite

- `app/physics/regression.py` existe.
- `linear_fit` e importavel via `app.physics`.
- Ajuste nao ponderado retorna coeficientes proximos dos valores conhecidos.
- Ajuste ponderado usa `sigma_y` e retorna incertezas finitas.
- `R2` e calculado e armazenado no `FitResult`.
- A suite passa com `python -m pytest`.

## Testes esperados

Cobrir ajuste exato simples, ajuste com ruido e incertezas verticais, campos do
`FitResult` e calculo de `R2`.

## Dependencias

- Issue #1: scaffold Python e SciPy.
- Issue #2: setup basico de testes.
- Issue #3: modelo `FitResult`.
- Spec principal: `docs/specs/mvp-ondas-corda.md`, secao 11.
