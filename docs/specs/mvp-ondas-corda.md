# Spec do MVP — Gerador de Gráficos para Física Experimental 2

## 1. Motivação

O objetivo deste MVP é criar uma ferramenta local e simples para gerar gráficos científicos a partir dos dados coletados nos experimentos de Física Experimental 2 da UnB.

Durante as aulas, os relatórios precisam ser finalizados rapidamente, geralmente no mesmo período do experimento. Uma das partes mais demoradas é transformar os dados medidos em gráficos corretos, com ajuste, legenda, unidades, parâmetros e incertezas.

A ferramenta deve reduzir esse trabalho manual.

O foco inicial não é gerar o relatório completo. O foco é:

```text
entrada de dados experimentais
        ↓
cálculos automáticos
        ↓
regressão linear
        ↓
incertezas
        ↓
gráfico científico
        ↓
exportação em PNG
```

O primeiro experimento suportado será:

**Movimento ondulatório: onda na corda**

O roteiro desse experimento pede gráficos específicos envolvendo frequência, comprimento de onda, número harmônico, velocidade e tensão. Também pede análise gráfica, ajuste linear e comparação de coeficientes dentro das incertezas experimentais.

---

## 2. Base acadêmica do MVP

O experimento de ondas na corda tem como objetivo observar ondas estacionárias e estudar a relação entre velocidade, frequência e comprimento de onda. O roteiro também explora leis de Newton, propagação de ondas, reflexão, ondas estacionárias e ferramentas de análise gráfica.

A relação fundamental usada no experimento é:

```text
v = λf
```

O roteiro apresenta essa expressão como a velocidade de propagação da onda.

Para ondas estacionárias com extremidades fixas, o roteiro usa:

```text
λₙ = 2L / n
```

onde `L` é o comprimento da corda e `n` é o número de ventres visíveis.

Para a velocidade de propagação em uma corda tensionada, o roteiro usa:

```text
v = sqrt(τ / μ)
```

onde `τ` é a tensão na corda e `μ` é a densidade linear.

O roteiro solicita explicitamente:

1. calcular a velocidade usando `v = sqrt(τ / μ)`;
2. fazer gráfico de `f` em função de `1/λ`;
3. obter coeficiente angular e incerteza;
4. comparar esse coeficiente com a velocidade calculada;
5. fazer gráfico de `λ` em função de `1/n`;
6. verificar se o coeficiente angular é igual a `2L` dentro das incertezas;
7. fazer gráfico mostrando que `v ∝ sqrt(τ)`. 
As normas do relatório pedem gráficos claros, com dados experimentais na forma de pontos, ajustes na forma de linhas e parâmetros dos ajustes colocados no próprio gráfico, com atenção aos algarismos significativos.

---

## 3. Objetivo do MVP

Criar uma aplicação desktop local capaz de:

1. permitir entrada manual dos dados experimentais;
2. calcular automaticamente grandezas derivadas;
3. gerar gráficos científicos adequados ao experimento;
4. fazer regressão linear;
5. mostrar parâmetros do ajuste com incerteza;
6. mostrar barras de erro quando houver incertezas informadas;
7. exportar o gráfico como PNG em alta resolução;
8. permitir configurar o tamanho da imagem exportada.

---

## 4. Fora do escopo do MVP

O MVP não deve implementar inicialmente:

- geração completa de relatório em PDF;
- editor de texto científico;
- LaTeX completo;
- banco de dados;
- login;
- sincronização em nuvem;
- IA para escrita de análise;
- suporte genérico a todos os experimentos da disciplina;
- interface web;
- Electron;
- Tauri;
- importação automática de arquivos externos;
- exportação para Word ou PDF.

Esses itens podem ser adicionados depois.

O MVP deve resolver bem apenas uma coisa:

**gerar gráficos corretos para o experimento de ondas na corda.**

---

## 5. Stack recomendada

Usar Python.

Stack mínima:

```text
Python 3.12+
Tkinter
NumPy
SciPy
Matplotlib
```

Justificativa:

- Python tem excelente ecossistema científico.
- Tkinter é suficiente para um MVP simples e já vem com Python.
- NumPy resolve os cálculos vetoriais.
- SciPy permite regressão e ajuste com incerteza.
- Matplotlib gera gráficos científicos em PNG com controle de DPI e tamanho.

Evitar, no MVP:

- PySide6;
- Electron;
- React;
- servidor web;
- banco de dados.

A arquitetura deve permitir trocar a interface no futuro sem reescrever os cálculos. Por isso, separar bem:

```text
interface ≠ física ≠ gráficos ≠ exportação
```

---

## 6. Estrutura sugerida do projeto

```text
physics-lab-graphs/
│
├── app/
│   ├── main.py
│   │
│   ├── ui/
│   │   ├── main_window.py
│   │   └── table_inputs.py
│   │
│   ├── physics/
│   │   ├── waves.py
│   │   └── uncertainty.py
│   │
│   ├── plotting/
│   │   ├── plot_builder.py
│   │   └── styles.py
│   │
│   ├── models/
│   │   ├── data_point.py
│   │   └── fit_result.py
│   │
│   └── export/
│       └── png_exporter.py
│
├── examples/
│   └── ondas_exemplo.csv
│
├── output/
│
├── requirements.txt
└── README.md
```

---

## 7. Funcionalidades principais

### 7.1 Tela inicial

A aplicação deve abrir com uma janela simples contendo:

```text
Experimento:
[ Movimento ondulatório: onda na corda ]

Tipo de gráfico:
[ f × 1/λ ▼ ]

Botões:
[ Novo gráfico ]
[ Gerar gráfico ]
[ Exportar PNG ]
```

No MVP, só haverá um experimento disponível:

```text
Movimento ondulatório: onda na corda
```

Mas a interface deve deixar espaço para adicionar outros no futuro.

---

## 8. Tipos de gráfico suportados

O MVP deve suportar três gráficos.

---

# Gráfico 1 — f em função de 1/λ

## 8.1 Objetivo físico

Verificar que:

```text
f ∝ 1/λ
```

Como:

```text
v = λf
```

então:

```text
f = v · (1/λ)
```

Logo, no gráfico:

```text
y = f
x = 1/λ
```

o coeficiente angular da reta deve representar a velocidade da onda.

## 8.2 Entrada do usuário

A tabela deve permitir inserir:

```text
n
f_Hz
lambda_m
delta_lambda_m
delta_f_Hz
```

Campos:

- `n`: número harmônico;
- `f_Hz`: frequência em hertz;
- `lambda_m`: comprimento de onda em metros;
- `delta_lambda_m`: incerteza do comprimento de onda em metros;
- `delta_f_Hz`: incerteza da frequência em hertz.

`delta_f_Hz` pode ser opcional.

Se o usuário não informar `delta_f_Hz`, usar valor vazio e não desenhar barra de erro vertical.

## 8.3 Cálculos automáticos

Calcular:

```text
x = 1 / λ
y = f
```

Propagar a incerteza de `λ` para `1/λ`:

```text
δx = δλ / λ²
```

Se `delta_lambda_m` não for informado, não mostrar barra horizontal.

## 8.4 Ajuste

Fazer regressão linear:

```text
f = a · (1/λ) + b
```

O resultado deve conter:

```text
a
δa
b
δb
R²
```

Interpretar `a` como velocidade experimental:

```text
v_exp = a
```

Unidade de `a`:

```text
m/s
```

## 8.5 Gráfico exportado

Título sugerido:

```text
Frequência em função do inverso do comprimento de onda
```

Eixo x:

```text
1/λ (m⁻¹)
```

Eixo y:

```text
f (Hz)
```

Texto dentro do gráfico:

```text
Ajuste linear:
f = a(1/λ) + b

a = (... ± ...) m/s
b = (... ± ...) Hz
R² = ...
```

---

# Gráfico 2 — λ em função de 1/n

## 8.6 Objetivo físico

Verificar a relação:

```text
λₙ = 2L / n
```

Reescrevendo:

```text
λ = 2L · (1/n)
```

Logo, no gráfico:

```text
y = λ
x = 1/n
```

o coeficiente angular deve ser aproximadamente:

```text
a = 2L
```

## 8.7 Entrada do usuário

A tabela deve permitir inserir:

```text
n
lambda_m
delta_lambda_m
```

Campos:

- `n`: número harmônico;
- `lambda_m`: comprimento de onda em metros;
- `delta_lambda_m`: incerteza no comprimento de onda.

A tela também deve permitir informar:

```text
L_m
delta_L_m
```

onde:

- `L_m`: comprimento da corda em metros;
- `delta_L_m`: incerteza no comprimento da corda.

## 8.8 Cálculos automáticos

Calcular:

```text
x = 1 / n
y = λ
```

Como `n` é inteiro e sem incerteza experimental relevante no MVP, não calcular incerteza horizontal.

Se `delta_lambda_m` for informado, mostrar barra de erro vertical.

Calcular valor esperado:

```text
2L
```

e incerteza:

```text
δ(2L) = 2δL
```

## 8.9 Ajuste

Fazer regressão linear:

```text
λ = a · (1/n) + b
```

O resultado deve conter:

```text
a
δa
b
δb
R²
```

Comparar:

```text
a ≈ 2L
```

A interface deve mostrar:

```text
coeficiente angular = a ± δa
valor esperado = 2L ± 2δL
```

E indicar se são compatíveis dentro das incertezas.

Critério simples para compatibilidade no MVP:

```text
abs(a - 2L) <= δa + 2δL
```

Se for compatível:

```text
Compatível dentro das incertezas: sim
```

Caso contrário:

```text
Compatível dentro das incertezas: não
```

## 8.10 Gráfico exportado

Título sugerido:

```text
Comprimento de onda em função de 1/n
```

Eixo x:

```text
1/n
```

Eixo y:

```text
λ (m)
```

Texto dentro do gráfico:

```text
Ajuste linear:
λ = a(1/n) + b

a = (... ± ...) m
b = (... ± ...) m
R² = ...

2L = (... ± ...) m
```

---

# Gráfico 3 — v em função de √τ

## 8.11 Objetivo físico

Mostrar graficamente que:

```text
v ∝ √τ
```

O roteiro pede variar a massa pendurada, encontrar a frequência para uma configuração com `n = 2`, montar tabela com `f`, `v`, `m` e `τ`, e mostrar graficamente a proporcionalidade entre `v` e `√τ`.

## 8.12 Entrada do usuário

A tabela deve permitir inserir:

```text
m_kg
f_Hz
lambda_m
delta_m_kg
delta_f_Hz
delta_lambda_m
```

Campos:

- `m_kg`: massa pendurada em quilogramas;
- `f_Hz`: frequência em hertz;
- `lambda_m`: comprimento de onda em metros;
- `delta_m_kg`: incerteza da massa;
- `delta_f_Hz`: incerteza da frequência;
- `delta_lambda_m`: incerteza do comprimento de onda.

A constante gravitacional deve ser configurável, mas ter valor padrão:

```text
g = 9.8 m/s²
```

O roteiro usa `g = 9,8 m/s²`.

## 8.13 Cálculos automáticos

Calcular tensão:

```text
τ = m · g
```

Calcular velocidade:

```text
v = λ · f
```

Calcular eixo x:

```text
x = √τ
```

Calcular eixo y:

```text
y = v
```

Propagar incerteza de τ:

```text
δτ = g · δm
```

Propagar incerteza de √τ:

```text
δx = δτ / (2√τ)
```

Propagar incerteza de v:

```text
δv = v · sqrt((δλ/λ)² + (δf/f)²)
```

Se alguma incerteza não for informada, não desenhar a respectiva barra de erro.

## 8.14 Ajuste

Fazer regressão linear:

```text
v = a · √τ + b
```

O resultado deve conter:

```text
a
δa
b
δb
R²
```

Unidade de `a`:

```text
(m/s) / √N
```

## 8.15 Gráfico exportado

Título sugerido:

```text
Velocidade da onda em função da raiz da tensão
```

Eixo x:

```text
√τ (√N)
```

Eixo y:

```text
v (m/s)
```

Texto dentro do gráfico:

```text
Ajuste linear:
v = a√τ + b

a = (... ± ...) (m/s)/√N
b = (... ± ...) m/s
R² = ...
```

---

## 9. Interface

A interface deve ser funcional e objetiva.

Não precisa ser bonita no primeiro MVP, mas precisa ser clara.

### 9.1 Layout geral

```text
┌────────────────────────────────────────────────────────────┐
│ Gerador de Gráficos — Física Experimental 2                │
├────────────────────────────────────────────────────────────┤
│ Experimento: Movimento ondulatório: onda na corda          │
│ Tipo de gráfico: [ f × 1/λ ▼ ]                             │
├───────────────────────┬────────────────────────────────────┤
│ Dados                 │ Preview                            │
│                       │                                    │
│ tabela editável       │ gráfico matplotlib                 │
│                       │                                    │
│ [Adicionar linha]     │                                    │
│ [Remover linha]       │                                    │
│                       │                                    │
├───────────────────────┴────────────────────────────────────┤
│ Largura PNG: [1600] Altura PNG: [1000] DPI: [300]           │
│ [Gerar gráfico] [Exportar PNG]                              │
└────────────────────────────────────────────────────────────┘
```

### 9.2 Controles obrigatórios

A tela deve conter:

```text
Tipo de gráfico
Tabela de dados
Botão adicionar linha
Botão remover linha
Botão gerar gráfico
Botão exportar PNG
Campo largura em pixels
Campo altura em pixels
Campo DPI
Área de preview
```

### 9.3 Presets de exportação

Criar presets:

```text
Relatório:
largura = 1600 px
altura = 1000 px
dpi = 300

Alta resolução:
largura = 2400 px
altura = 1500 px
dpi = 300

Rápido:
largura = 1000 px
altura = 625 px
dpi = 150
```

O usuário pode alterar manualmente os valores.

---

## 10. Requisitos de gráfico

Todos os gráficos devem ter:

- título;
- eixo x com unidade;
- eixo y com unidade;
- pontos experimentais;
- barras de erro, quando houver incerteza;
- reta de ajuste linear;
- legenda;
- grade discreta;
- caixa de texto com os parâmetros do ajuste;
- exportação em PNG;
- fundo branco;
- boa legibilidade para relatório.

### 10.1 Estilo visual

Usar um estilo limpo e acadêmico.

Evitar visual poluído.

Recomendações:

```text
figsize proporcional a 16:10 ou 8:5
dpi padrão 300
fonte entre 10 e 12 pt
marcadores visíveis
linha de ajuste contínua
grade leve
```

Não usar tema escuro.

---

## 11. Ajuste linear

Criar uma função genérica:

```python
def linear_fit(x, y, sigma_y=None):
    ...
```

Ela deve retornar:

```python
FitResult(
    slope: float,
    slope_uncertainty: float,
    intercept: float,
    intercept_uncertainty: float,
    r_squared: float
)
```

### 11.1 Implementação sugerida

Pode usar:

```python
scipy.optimize.curve_fit
```

Modelo:

```python
def model(x, a, b):
    return a * x + b
```

Se houver `sigma_y`, usar ponderação:

```python
curve_fit(model, x, y, sigma=sigma_y, absolute_sigma=True)
```

Se não houver `sigma_y`, fazer ajuste não ponderado.

O desvio dos parâmetros vem da matriz de covariância:

```python
perr = np.sqrt(np.diag(pcov))
```

Calcular `R²` manualmente:

```python
ss_res = sum((y - y_pred)²)
ss_tot = sum((y - mean(y))²)
r_squared = 1 - ss_res / ss_tot
```

---

## 12. Incertezas

Criar funções em `physics/uncertainty.py`.

### 12.1 Inverso do comprimento de onda

Para:

```text
x = 1/λ
```

usar:

```text
δx = δλ / λ²
```

### 12.2 Tensão

Para:

```text
τ = mg
```

usar:

```text
δτ = gδm
```

### 12.3 Raiz da tensão

Para:

```text
x = √τ
```

usar:

```text
δx = δτ / (2√τ)
```

### 12.4 Velocidade

Para:

```text
v = λf
```

usar:

```text
δv = v · sqrt((δλ/λ)² + (δf/f)²)
```

Se uma incerteza estiver ausente, tratar como `None`.

Não forçar cálculo de incerteza quando faltarem dados.

---

## 13. Validação dos dados

O programa deve validar:

- campos numéricos;
- valores positivos para frequência;
- valores positivos para comprimento de onda;
- valores positivos para massa;
- `n` inteiro positivo;
- mínimo de 2 pontos para gerar uma reta;
- idealmente mínimo de 3 pontos para ajuste com incerteza mais confiável.

Mensagens de erro devem ser claras.

Exemplos:

```text
O comprimento de onda deve ser maior que zero.
```

```text
É necessário inserir pelo menos dois pontos para gerar o ajuste linear.
```

```text
O número harmônico n deve ser um inteiro positivo.
```

---

## 14. Exportação PNG

A função de exportação deve salvar o gráfico como `.png`.

Nome padrão sugerido:

```text
grafico_ondas_f_vs_inverso_lambda.png
grafico_ondas_lambda_vs_inverso_n.png
grafico_ondas_v_vs_raiz_tensao.png
```

O usuário deve poder escolher o local do arquivo usando diálogo do sistema.

Usar:

```python
fig.savefig(
    path,
    dpi=dpi,
    bbox_inches="tight"
)
```

A imagem precisa ser gerada a partir da figura do Matplotlib, não por screenshot da interface.

---

## 15. Modelos de dados

### 15.1 FitResult

```python
from dataclasses import dataclass

@dataclass
class FitResult:
    slope: float
    slope_uncertainty: float
    intercept: float
    intercept_uncertainty: float
    r_squared: float
```

### 15.2 PlotData

```python
from dataclasses import dataclass
from typing import Optional
import numpy as np

@dataclass
class PlotData:
    x: np.ndarray
    y: np.ndarray
    x_uncertainty: Optional[np.ndarray]
    y_uncertainty: Optional[np.ndarray]
    x_label: str
    y_label: str
    title: str
```

### 15.3 ExportConfig

```python
from dataclasses import dataclass

@dataclass
class ExportConfig:
    width_px: int = 1600
    height_px: int = 1000
    dpi: int = 300
```

---

## 16. Organização das funções físicas

Arquivo:

```text
app/physics/waves.py
```

Funções:

```python
def inverse_wavelength(lambda_m: np.ndarray) -> np.ndarray:
    ...

def wave_speed(lambda_m: np.ndarray, frequency_hz: np.ndarray) -> np.ndarray:
    ...

def tension_from_mass(mass_kg: np.ndarray, g: float = 9.8) -> np.ndarray:
    ...

def sqrt_tension(tension_n: np.ndarray) -> np.ndarray:
    ...

def inverse_harmonic(n: np.ndarray) -> np.ndarray:
    ...
```

---

## 17. Organização dos gráficos

Arquivo:

```text
app/plotting/plot_builder.py
```

Função principal:

```python
def build_linear_plot(
    plot_data: PlotData,
    fit_result: FitResult,
    fit_label: str,
    parameter_text: str,
    export_config: ExportConfig
):
    ...
```

Essa função deve:

1. criar a figura;
2. desenhar pontos;
3. desenhar barras de erro se existirem;
4. desenhar reta de ajuste;
5. adicionar título;
6. adicionar labels dos eixos;
7. adicionar legenda;
8. adicionar caixa de texto com parâmetros;
9. retornar `fig`.

---

## 18. Formatação dos parâmetros

Criar função simples para formatar valores com incerteza.

Arquivo:

```text
app/physics/uncertainty.py
```

Função:

```python
def format_value_with_uncertainty(value: float, uncertainty: float, unit: str = "") -> str:
    ...
```

No MVP, pode ser simples.

Exemplo de saída aceitável:

```text
(12.43 ± 0.21) m/s
```

Não precisa implementar regras perfeitas de algarismos significativos na primeira versão, mas deixar a função isolada para melhorar depois.

---

## 19. Fluxo do usuário

### Fluxo 1 — gerar gráfico `f × 1/λ`

1. usuário escolhe `f × 1/λ`;
2. preenche `n`, `f`, `λ`, `δλ` e opcionalmente `δf`;
3. clica em `Gerar gráfico`;
4. programa calcula `1/λ`;
5. programa propaga `δ(1/λ)`;
6. programa faz ajuste linear;
7. programa mostra gráfico no preview;
8. usuário clica em `Exportar PNG`;
9. programa salva o arquivo.

### Fluxo 2 — gerar gráfico `λ × 1/n`

1. usuário escolhe `λ × 1/n`;
2. informa `L` e opcionalmente `δL`;
3. preenche `n`, `λ` e `δλ`;
4. clica em `Gerar gráfico`;
5. programa calcula `1/n`;
6. programa faz ajuste linear;
7. programa compara coeficiente angular com `2L`;
8. programa mostra resultado;
9. usuário exporta PNG.

### Fluxo 3 — gerar gráfico `v × √τ`

1. usuário escolhe `v × √τ`;
2. preenche `m`, `f`, `λ` e incertezas opcionais;
3. programa calcula `τ = mg`;
4. programa calcula `√τ`;
5. programa calcula `v = λf`;
6. programa propaga incertezas quando possível;
7. programa faz ajuste linear;
8. programa mostra gráfico;
9. usuário exporta PNG.

---

## 20. Critérios de aceite

O MVP está pronto quando:

- a aplicação abre localmente;
- o usuário consegue selecionar os três tipos de gráfico;
- o usuário consegue inserir dados manualmente;
- o programa calcula as grandezas derivadas;
- o programa gera regressão linear;
- o programa mostra coeficiente angular, intercepto e `R²`;
- o programa mostra incerteza dos parâmetros do ajuste;
- o programa mostra barras de erro quando houver incertezas;
- o programa exporta PNG em alta resolução;
- os eixos têm nomes e unidades corretas;
- os parâmetros do ajuste aparecem no próprio gráfico;
- o gráfico fica adequado para ser inserido no relatório.

---

## 21. README esperado

Criar um `README.md` com:

```text
# Gerador de Gráficos — Física Experimental 2

Ferramenta local para gerar gráficos científicos do experimento de ondas na corda.

## Instalação

python -m venv .venv

Windows:
.venv\Scripts\activate

Linux/Mac:
source .venv/bin/activate

pip install -r requirements.txt

## Execução

python -m app.main
```

Também incluir uma breve explicação dos três gráficos suportados.

---

## 22. requirements.txt

Usar:

```text
numpy
scipy
matplotlib
```

Tkinter não precisa estar no `requirements.txt`, pois geralmente vem com Python. Se houver problema no Linux, documentar no README que pode ser necessário instalar o pacote do sistema.

---

## 23. Observação final de arquitetura

Não colocar os cálculos diretamente dentro dos callbacks da interface.

Evitar código assim:

```python
def on_generate_button_click():
    # cálculos físicos
    # regressão
    # gráfico
    # exportação
```

Preferir:

```python
def on_generate_button_click():
    raw_data = collect_ui_data()
    plot_data = build_plot_data(raw_data)
    fit_result = linear_fit(plot_data.x, plot_data.y, plot_data.y_uncertainty)
    fig = build_linear_plot(plot_data, fit_result, ...)
    show_preview(fig)
```

A interface deve apenas coletar dados e chamar funções.

A física, as incertezas, os ajustes e os gráficos devem ficar em módulos separados.

Isso deixa o MVP simples agora e permite evoluir depois para uma aplicação maior de relatórios.