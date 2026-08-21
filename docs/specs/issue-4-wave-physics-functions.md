# Issue #4 - Funcoes fisicas de ondas na corda

## Objetivo

Implementar as funcoes fisicas puras usadas pelos fluxos do experimento de
ondas na corda.

Essas funcoes formam a base numerica para transformacoes como `1/lambda`,
`v = lambda * f`, `tau = m * g`, `sqrt(tau)` e `1/n`.

## Escopo

Criar `app/physics/waves.py` com:

- `inverse_wavelength(lambda_m: np.ndarray) -> np.ndarray`
- `wave_speed(lambda_m: np.ndarray, frequency_hz: np.ndarray) -> np.ndarray`
- `tension_from_mass(mass_kg: np.ndarray, g: float = 9.8) -> np.ndarray`
- `sqrt_tension(tension_n: np.ndarray) -> np.ndarray`
- `inverse_harmonic(n: np.ndarray) -> np.ndarray`

Expor as funcoes em `app/physics/__init__.py`.

Criar testes unitarios em `tests/physics/test_waves.py`.

## Fora de escopo

- Validacao de entrada do usuario.
- Mensagens de erro.
- Propagacao de incertezas.
- Regressao linear.
- Compatibilidade entre coeficiente angular e valor esperado.
- Geracao de grafico.
- Interface Tkinter.

## Contratos de dominio

### inverse_wavelength

Calcula:

```text
x = 1 / lambda
```

Entrada:

- `lambda_m`: array NumPy com comprimentos de onda em metros.

Saida:

- array NumPy com inversos em `m^-1`.

### wave_speed

Calcula:

```text
v = lambda * f
```

Entrada:

- `lambda_m`: array NumPy com comprimentos de onda em metros.
- `frequency_hz`: array NumPy com frequencias em hertz.

Saida:

- array NumPy com velocidades em `m/s`.

### tension_from_mass

Calcula:

```text
tau = m * g
```

Entrada:

- `mass_kg`: array NumPy com massas em quilogramas.
- `g`: aceleracao gravitacional em `m/s^2`, com default `9.8`.

Saida:

- array NumPy com tensoes em newtons.

### sqrt_tension

Calcula:

```text
x = sqrt(tau)
```

Entrada:

- `tension_n`: array NumPy com tensoes em newtons.

Saida:

- array NumPy com raiz da tensao em `sqrt(N)`.

### inverse_harmonic

Calcula:

```text
x = 1 / n
```

Entrada:

- `n`: array NumPy com numeros harmonicos.

Saida:

- array NumPy com inversos dos harmonicos.

## Decisoes

- As funcoes devem ser vetoriais e operar com NumPy.
- As funcoes devem ser puras: sem estado global, UI, IO ou Matplotlib.
- Validacoes de dominio ficam para uma camada futura. Esta issue assume entradas
  numericas validas.
- `g = 9.8` deve ser o valor padrao porque a spec principal e o roteiro usam
  esse valor.

## Criterios de aceite

- `app/physics/waves.py` existe.
- As cinco funcoes existem e sao importaveis via `app.physics`.
- Cada funcao retorna os valores esperados para arrays simples.
- A suite de testes passa com `python -m pytest`.

## Testes esperados

Cobrir:

- `inverse_wavelength([0.5, 1.0, 2.0]) == [2.0, 1.0, 0.5]`;
- `wave_speed([0.5, 1.0], [10.0, 20.0]) == [5.0, 20.0]`;
- `tension_from_mass([0.1, 0.2], 9.8) == [0.98, 1.96]`;
- `sqrt_tension([1.0, 4.0, 9.0]) == [1.0, 2.0, 3.0]`;
- `inverse_harmonic([1, 2, 4]) == [1.0, 0.5, 0.25]`.

## Dependencias

- Issue #1: scaffold Python do projeto.
- Issue #2: setup basico de testes com Pytest.
- Spec principal: `docs/specs/mvp-ondas-corda.md`, secao 16.

