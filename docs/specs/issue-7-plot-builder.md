# Spec da issue #7 - Builder de graficos cientificos

## Objetivo

Criar o builder Matplotlib que transforma `PlotData` e `FitResult` em uma
figura cientifica pronta para preview e exportacao.

## Escopo

Criar `app/plotting/plot_builder.py` com:

```python
build_linear_plot(
    plot_data: PlotData,
    fit_result: FitResult,
    fit_label: str,
    parameter_text: str,
    export_config: ExportConfig,
)
```

A funcao deve:

1. criar uma figura com dimensoes derivadas de `ExportConfig`;
2. desenhar pontos experimentais;
3. desenhar barras de erro quando `x_uncertainty` ou `y_uncertainty` existirem;
4. desenhar a reta de ajuste entre o menor e o maior `x`;
5. configurar titulo, labels, legenda e grade discreta;
6. adicionar `parameter_text` em uma caixa dentro dos eixos;
7. retornar a figura Matplotlib.

## Fora de escopo

- Calcular transformacoes fisicas ou regressao.
- Exportar o arquivo PNG.
- Formatar parametros do ajuste.
- Validar dados de entrada da UI.
- Criar a interface Tkinter.

## Contratos de comportamento

- `PlotData` fornece os dados, unidades e titulo que aparecem na figura.
- `FitResult` fornece `slope` e `intercept` para a reta `y = a*x + b`.
- `fit_label` aparece na legenda da reta.
- `parameter_text` aparece em uma caixa de texto dentro dos eixos.
- Incertezas `None` nao geram barras no respectivo eixo.
- A figura usa fundo branco e estilo limpo, adequado para relatorio.
- `ExportConfig` define `figsize` por `width_px / dpi` e `height_px / dpi`,
  alem do DPI da figura.

## Decisoes

- O builder retorna a figura e deixa `savefig` para a issue de exportacao.
- O grafico usa pontos experimentais com `errorbar`, pois esse primitive cobre
  pontos e barras de erro horizontais e verticais no mesmo contrato.
- A caixa de parametros recebe texto pronto da camada superior; o builder nao
  conhece regras de algarismos significativos.
- O eixo x da reta usa exatamente o intervalo observado nos dados.

## Criterios de aceite

- `app/plotting/plot_builder.py` existe.
- `build_linear_plot` e importavel via `app.plotting`.
- A figura contem dados, reta, titulo, labels, legenda e grade.
- A figura usa as dimensoes e o DPI de `ExportConfig`.
- Barras de erro sao desenhadas somente quando as incertezas existem.
- A caixa de parametros aparece na area dos eixos.
- Testes Matplotlib passam com backend nao interativo.

## Testes esperados

Inspecionar a figura retornada para verificar dimensoes, DPI, textos, linhas,
legenda e a presenca ou ausencia de barras de erro.

## Dependencias

- Issue #3: modelos `PlotData`, `FitResult` e `ExportConfig`.
- Issue #6: resultado da regressao linear.
- Spec principal: `docs/specs/mvp-ondas-corda.md`, secoes 10 e 17.
