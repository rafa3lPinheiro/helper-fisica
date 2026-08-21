# Spec da issue #5 - Propagacao de incertezas

## Objetivo

Implementar as propagacoes de incerteza usadas pelos tres fluxos de graficos
do experimento de ondas na corda.

## Escopo

Criar `app/physics/uncertainty.py` com funcoes puras e vetoriais para:

- incerteza de `1/lambda`;
- incerteza da tensao `tau = m * g`;
- incerteza de `sqrt(tau)`;
- incerteza da velocidade `v = lambda * f`.

Expor as funcoes em `app.physics` e cobrir os contratos com testes unitarios.

## Fora de escopo

- Validacao de entradas da UI.
- Mensagens de erro.
- Regressao linear e incerteza dos parametros do ajuste.
- Formatacao textual de valores, como `valor +/- incerteza`.
- Decisao de quais barras de erro serao desenhadas no grafico.

## Contratos de dominio

### `inverse_wavelength_uncertainty`

Calcula:

```text
delta_x = delta_lambda / lambda**2
```

Recebe arrays NumPy de comprimento de onda e sua incerteza, ambos em metros;
retorna a incerteza de `1/lambda`, em `m^-1`.

### `tension_uncertainty`

Calcula:

```text
delta_tau = g * delta_mass
```

Recebe a incerteza da massa em quilogramas e `g` em `m/s^2`; retorna a
incerteza da tensao em newtons. O default de `g` e `9.8`.

### `sqrt_tension_uncertainty`

Calcula:

```text
delta_x = delta_tau / (2 * sqrt(tau))
```

Recebe tensao em newtons e sua incerteza; retorna a incerteza de `sqrt(tau)`.

### `wave_speed_uncertainty`

Calcula:

```text
delta_v = v * sqrt((delta_lambda/lambda)**2 + (delta_f/frequency)**2)
```

Recebe `lambda`, `frequency`, `delta_lambda` e `delta_frequency`; retorna a
incerteza da velocidade em `m/s`.

## Decisoes

- As funcoes serao vetoriais e operarao com NumPy, seguindo `waves.py`.
- As funcoes serao puras, sem UI, IO, estado global ou Matplotlib.
- Esta camada recebe incertezas explicitas. A ausencia de uma incerteza sera
  representada pelas camadas superiores, que decidirao quando nao desenhar a
  barra correspondente.
- A formatacao de apresentacao fica fora desta issue para manter separadas
  matematica e exibicao.

## Criterios de aceite

- `app/physics/uncertainty.py` existe.
- As quatro funcoes sao importaveis via `app.physics`.
- As formulas retornam valores esperados para arrays simples.
- O resultado preserva a forma dos arrays de entrada.
- A suite de testes passa com `python -m pytest`.

## Testes esperados

Cobrir valores conhecidos para cada formula, `g` default e customizado, e
entradas vetoriais com mais de um ponto.

## Dependencias

- Issue #1: scaffold Python.
- Issue #2: setup basico de testes.
- Issue #4: funcoes fisicas fundamentais.
- Spec principal: `docs/specs/mvp-ondas-corda.md`, secoes 8 e 12.
