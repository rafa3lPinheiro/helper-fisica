# Spec da issue #11 - Fluxo v por sqrt(tensao)

## Objetivo

Implementar o terceiro fluxo completo do experimento: calcular tensao,
velocidade, raiz da tensao, incertezas e ajuste linear de `v` em funcao de
`sqrt(tensao)`.

## Escopo

Adicionar em `app/plotting/wave_graphs.py`:

```python
build_velocity_sqrt_tension(
    mass_kg,
    frequency_hz,
    lambda_m,
    delta_mass_kg=None,
    delta_frequency_hz=None,
    delta_lambda_m=None,
    g=9.8,
) -> VelocitySqrtTensionResult
```

Criar o dataclass de resultado com:

- `plot_data: PlotData`;
- `fit_result: FitResult`;
- `fit_label: str`;
- `parameter_text: str`;
- `tension_n: NDArray`;
- `speed_m_s: NDArray`.

## Fora de escopo

- Interface Tkinter e validacao de campos.
- Comparacao com densidade linear teorica.
- Exportacao PNG.
- Fluxos dos outros dois graficos.

## Contratos

- `tension = mass * g`.
- `speed = lambda * frequency`.
- `x = sqrt(tension)` e `y = speed`.
- Quando `delta_mass_kg` existe, `x_uncertainty` usa
  `delta_tension = g * delta_mass` e `delta_x = delta_tension / (2 * sqrt(tension))`.
- `y_uncertainty` so existe quando `delta_lambda_m` e `delta_frequency_hz`
  existem juntos, usando propagacao relativa da velocidade.
- Incertezas ausentes produzem `None` na barra correspondente.
- O ajuste usa `y_uncertainty` como `sigma_y` quando disponivel.
- Labels: `sqrt(tau) (sqrt(N))` e `v (m/s)`.
- A constante `g` tem default `9.8` e pode ser alterada.

## Decisoes

- O resultado nomeado tambem expoe tensao e velocidade para a UI e para
  mensagens de verificacao, sem recalcular essas grandezas.
- Nao fazer propagacao parcial de `v`: uma das duas incertezas ausentes torna a
  incerteza vertical indisponivel.
- O texto usa unidade de coeficiente angular `(m/s)/sqrt(N)`.

## Criterios de aceite

- O fluxo e importavel via `app.plotting`.
- Calcula tensao, velocidade, `sqrt(tensao)` e ajuste.
- Propaga corretamente as incertezas disponiveis.
- Aceita `g` customizado.
- Produz texto com `a`, `b` e `R2`.
- A suite passa com `python -m pytest`.

## Testes esperados

Cobrir calculos completos, `g` customizado, todas as incertezas, ausencia de
`delta_m`, ausencia de uma das incertezas de velocidade e texto do ajuste.

## Dependencias

- Issues #3, #4, #5 e #6: modelos, fisica, incertezas e regressao.
- Issue #7: contrato de entrada do builder.
- Issue #9: formatacao de valores e padrao dos fluxos.
- Spec principal: `docs/specs/mvp-ondas-corda.md`, secoes 8.11 a 8.15.
