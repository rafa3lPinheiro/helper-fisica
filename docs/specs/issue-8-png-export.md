# Spec da issue #8 - Exportacao PNG

## Objetivo

Salvar figuras Matplotlib como PNG usando configuracoes reutilizaveis de
tamanho e resolucao para relatorio, alta resolucao e exportacao rapida.

## Escopo

Criar `app/export/png_exporter.py` com:

```python
export_png(figure, output_path, export_config) -> Path
get_export_preset(name) -> ExportConfig
```

Presets:

| Nome | Largura | Altura | DPI |
| --- | ---: | ---: | ---: |
| `relatorio` | 1600 px | 1000 px | 300 |
| `alta_resolucao` | 2400 px | 1500 px | 300 |
| `rapido` | 1000 px | 625 px | 150 |

Expor as funcoes pelo pacote `app.export` e criar testes unitarios.

## Fora de escopo

- Dialogo de selecao de arquivo do sistema.
- Interface Tkinter.
- Exportacao para PDF, SVG ou outros formatos.
- Criacao ou alteracao do conteudo da figura.
- Criacao automatica de diretorios.

## Contratos

- `export_png` recebe uma figura Matplotlib e um caminho de destino.
- O caminho retornado e um `Path` e termina em `.png`.
- Se o caminho nao tiver extensao, adicionar `.png`; se tiver outra extensao,
  substitui-la por `.png`.
- A figura deve ser salva com `dpi` do `ExportConfig`, fundo branco e
  `bbox_inches="tight"`.
- A figura deve ter seu tamanho atualizado para `width_px / dpi` por
  `height_px / dpi` antes do salvamento.
- `get_export_preset` retorna uma nova instancia de `ExportConfig`.
- Preset desconhecido deve gerar `ValueError` com mensagem clara.

## Decisoes

- O exporter nao fecha a figura; o ciclo de vida da figura pertence ao fluxo
  que a criou.
- O exporter nao cria diretorios ausentes, evitando efeitos colaterais
  implicitos no caminho escolhido pelo usuario.
- Os presets ficam em uma tabela central para permitir uso futuro na UI.

## Criterios de aceite

- `app/export/png_exporter.py` existe.
- `export_png` e `get_export_preset` sao importaveis via `app.export`.
- Os tres presets retornam os valores da spec principal.
- Um arquivo PNG valido e criado com a configuracao selecionada.
- Caminhos sem extensao recebem `.png`.
- Preset desconhecido gera erro.
- A suite passa com `python -m pytest`.

## Testes esperados

Cobrir os tres presets, dimensoes/DPI aplicados a figura, arquivo PNG criado,
normalizacao da extensao e erro para preset inexistente.

## Dependencias

- Issue #3: modelo `ExportConfig`.
- Issue #7: builder de figuras Matplotlib.
- Spec principal: `docs/specs/mvp-ondas-corda.md`, secoes 9 e 14.
