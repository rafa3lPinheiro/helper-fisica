# Spec da issue #12 - Interface Tkinter do MVP

## Objetivo

Criar a janela desktop funcional do MVP para escolher o experimento e o tipo de
grafico, editar dados, gerar preview Matplotlib e exportar PNG.

## Escopo

Implementar em `app/ui/main_window.py`:

- `create_app(root) -> MainWindow`;
- selecao do experimento `Movimento ondulatorio: onda na corda`;
- selecao dos tres tipos de grafico;
- tabela editavel com linhas adicionaveis e removiveis;
- campos de largura, altura e DPI;
- preview Matplotlib;
- botoes `Gerar grafico` e `Exportar PNG`;
- integracao com os tres fluxos de `app.plotting`;
- integracao com `app.export` usando dialogo de salvamento.

Atualizar `app.main` para iniciar o Tkinter.

## Fora de escopo

- Validacao detalhada e mensagens especificas de dominio.
- Importacao de CSV.
- Persistencia de dados.
- Temas escuros ou personalizacao visual avancada.
- Novos experimentos.

## Contratos de comportamento

- Layout dividido: controles/tabela a esquerda e preview dominante a direita.
- A tabela muda suas colunas conforme o tipo de grafico.
- A primeira linha vem preenchida com valores de exemplo para facilitar o uso.
- `Gerar grafico` atualiza o preview e habilita `Exportar PNG`.
- `Exportar PNG` permanece desabilitado antes de uma figura valida.
- A configuracao de exportacao usa defaults de `ExportConfig`.
- O callback da UI apenas coleta dados e chama os fluxos cientificos.
- Erros de conversao basica sao exibidos por dialogo; regras detalhadas ficam
  para a issue #13.

## Decisoes de UI/UX

- Bancada de trabalho com o grafico como area visual dominante.
- `Gerar grafico` e a acao primaria; exportacao e secundaria e contextual.
- Rotulos visiveis acompanham todos os campos.
- A tabela e usada porque comparar linhas e colunas e central no experimento.
- Fundo claro, espacamento e hierarquia de secoes comunicam agrupamento antes
  de usar decoracao.

## Criterios de aceite

- `python -m app.main` abre a janela Tkinter.
- O usuario consegue alternar os tres tipos de grafico.
- O usuario consegue adicionar/remover linhas e editar valores.
- O preview mostra o grafico gerado.
- Exportacao salva PNG pelo dialogo do sistema.
- O entrypoint deixa de imprimir apenas texto.
- Testes nao interativos cobrem configuracao dos tipos de grafico e entrypoint.

## Testes esperados

Cobrir mapeamento dos tipos de grafico, defaults dos campos e que `main` chama a
janela. Validacao visual manual sera registrada na issue #13.

## Dependencias

- Issues #7 a #11: builder, exportacao e tres fluxos cientificos.
- Spec principal: `docs/specs/mvp-ondas-corda.md`, secoes 9 e 19.
- Direcao UI/UX: `docs/product/ui-ux-direction.md`.
