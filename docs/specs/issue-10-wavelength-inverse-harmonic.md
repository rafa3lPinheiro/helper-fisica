# Spec da issue #10 - Fluxo lambda por 1/n

## Objetivo

Implementar o segundo fluxo completo do experimento: calcular `1/n`, ajustar
`lambda` em funcao de `1/n`, calcular o valor esperado `2L` e indicar sua
compatibilidade com o coeficiente angular.

## Escopo

Adicionar em `app/plotting/wave_graphs.py`:

```python
build_wavelength_inverse_harmonic(
    harmonic_n,
    lambda_m,
    length_m,
    delta_lambda_m=None,
    delta_length_m=None,
) -> WavelengthInverseHarmonicResult
```

Criar o dataclass de resultado com:

- `plot_data: PlotData`;
- `fit_result: FitResult`;
- `fit_label: str`;
- `parameter_text: str`;
- `expected_slope: float`;
- `expected_slope_uncertainty: float | None`;
- `compatible_with_expected: bool | None`.

## Fora de escopo

- Interface Tkinter e validacao de campos.
- Incerteza horizontal de `1/n`.
- Exportacao PNG.
- Fluxo `v x sqrt(tau)`.
- Regras avancadas de algarismos significativos.

## Contratos

- `x = 1/n`, `y = lambda`.
- `x_uncertainty` e sempre `None` no MVP.
- `y_uncertainty` recebe `delta_lambda_m` quando informado.
- `expected_slope = 2 * length_m`.
- Se `delta_length_m` existe, `expected_slope_uncertainty = 2 * delta_length_m`.
- Se ambas as incertezas existem, compatibilidade e:
  `abs(a - 2L) <= delta_a + 2 * delta_L`.
- Sem `delta_length_m`, `expected_slope_uncertainty` e
  `compatible_with_expected` sao `None`.
- O texto deve conter ajuste, coeficiente angular, valor esperado, `R2` e o
  resultado da compatibilidade.

## Decisoes

- O resultado nomeado evita uma tupla extensa e deixa explicitos os valores
  usados pela UI e pelo builder.
- Compatibilidade sem incerteza de `L` e indeterminada, nao falsa.
- A unidade do coeficiente angular e do valor esperado e `m`.

## Criterios de aceite

- O fluxo e importavel via `app.plotting`.
- Calcula `1/n`, ajuste e barras verticais opcionais.
- Calcula `2L` e `2 * delta_L` quando possivel.
- Aplica o criterio de compatibilidade da spec principal.
- Produz texto pronto para a caixa do grafico.
- A suite passa com `python -m pytest`.

## Testes esperados

Cobrir fluxo compativel, fluxo incompativel, ausencia de `delta_L`, ausencia de
`delta_lambda` e campos/texto do resultado.

## Dependencias

- Issues #3, #4, #5 e #6: modelos, funcoes fisicas, incertezas e regressao.
- Issue #7: contrato de entrada do builder.
- Issue #9: formatacao de valores com incerteza e padrao de fluxos.
- Spec principal: `docs/specs/mvp-ondas-corda.md`, secoes 8.6 a 8.10.
