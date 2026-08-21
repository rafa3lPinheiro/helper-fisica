# Spec da issue #9 - Fluxo f por 1/lambda

## Objetivo

Implementar o primeiro fluxo completo de analise do experimento: transformar
frequencia e comprimento de onda, propagar incertezas, ajustar uma reta e
preparar os textos consumidos pelo builder de graficos.

## Escopo

Criar `app/plotting/wave_graphs.py` com:

```python
build_frequency_inverse_wavelength(
    frequency_hz,
    lambda_m,
    delta_lambda_m=None,
    delta_frequency_hz=None,
) -> tuple[PlotData, FitResult, str, str]
```

O retorno deve conter, nesta ordem:

1. `PlotData` com `x = 1/lambda` e `y = f`;
2. `FitResult` do ajuste `f = a * (1/lambda) + b`;
3. label da reta para a legenda;
4. texto dos parametros para a caixa do grafico.

Adicionar em `app/physics/uncertainty.py` o formatador simples:

```python
format_value_with_uncertainty(value, uncertainty, unit="") -> str
```

## Fora de escopo

- Interface Tkinter e coleta de dados.
- Validacao de campos e mensagens de erro.
- Comparacao de `a` com uma velocidade teorica.
- Exportacao PNG.
- Os fluxos `lambda x 1/n` e `v x sqrt(tau)`.

## Contratos

- `delta_lambda_m=None` produz `x_uncertainty=None`.
- `delta_frequency_hz=None` produz `y_uncertainty=None` e ajuste nao ponderado.
- Quando `delta_frequency_hz` existe, ele e passado como `sigma_y` ao ajuste.
- O label deve ser `Ajuste linear`.
- O texto deve conter `a`, `b`, `R2`, suas incertezas e unidades `m/s` e `Hz`.
- O formatador usa duas casas decimais na primeira versao e inclui a unidade
  somente quando ela for informada.

## Decisoes

- O orquestrador retorna componentes do grafico em vez de criar a figura,
  mantendo calculos, dados e apresentacao desacoplados.
- O formatador permanece no modulo de incerteza por ser uma funcao pequena e
  reutilizavel pelos proximos fluxos.
- A ausencia de incerteza e representada por `None`, sem valores artificiais.

## Criterios de aceite

- `build_frequency_inverse_wavelength` e importavel via `app.plotting`.
- O fluxo calcula `1/lambda`, propaga `delta_lambda` quando informado e ajusta
  a reta correta.
- O ajuste ponderado usa `delta_frequency_hz` quando informado.
- O retorno contem labels e texto com parametros.
- O formatador cobre valor com e sem unidade.
- A suite passa com `python -m pytest`.

## Testes esperados

Cobrir fluxo com as duas incertezas, fluxo sem incertezas opcionais, ajuste e
texto de parametros, alem do formatador isolado.

## Dependencias

- Issues #3, #4, #5 e #6: modelos, funcoes fisicas, incertezas e regressao.
- Issue #7: contrato de entrada do builder.
- Spec principal: `docs/specs/mvp-ondas-corda.md`, secoes 8.1 a 8.5 e 18.
