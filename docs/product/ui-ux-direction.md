# Direcao inicial de UI/UX

## Contexto

O MVP e uma ferramenta desktop local para transformar dados experimentais em
graficos cientificos prontos para relatorio. A interface deve favorecer entrada
rapida, verificacao visual e exportacao confiavel.

## Padrao recomendado

O padrao de interface mais adequado e uma bancada de trabalho cientifica:

- painel de dados e configuracoes a esquerda;
- preview do grafico como area dominante a direita;
- resultados do ajuste proximos do grafico;
- acoes principais poucas e visiveis;
- exportacao configuravel no mesmo fluxo.

## Principios

- Clareza antes de decoracao.
- Grafico como conteudo principal.
- Tabela para dados experimentais, porque a comparacao entre linhas e colunas e
  parte central do trabalho.
- Validacao perto da linha ou campo afetado.
- Mensagens de erro especificas, com linguagem de dominio.
- Uso semanticamente restrito de cor: erro, aviso, compatibilidade e sucesso.
- Nada de tema escuro no MVP, para manter legibilidade academica e exportacao em
  fundo branco.

## Implicacoes para o MVP

- `Gerar grafico` deve ser a acao primaria.
- `Exportar PNG` deve ficar disponivel apos existir um grafico valido.
- Presets de exportacao devem reduzir decisao manual, mas permitir ajuste fino.
- O usuario deve conseguir ver rapidamente: dados inseridos, grafico gerado,
  parametros do ajuste e erros de validacao.
- A interface nao deve esconder regras fisicas importantes em tooltips.

## Referencias consultadas

- Tableau Visual Best Practices:
  https://help.tableau.com/current/blueprint/en-us/bp_visual_best_practices.htm
- Tableau Dashboard Best Practices:
  https://help.tableau.com/current/pro/desktop/en-us/dashboards_best_practices.htm
- Nielsen Norman Group - erros em formularios:
  https://www.nngroup.com/articles/errors-forms-design-guidelines/
- Nielsen Norman Group - escolha de graficos:
  https://www.nngroup.com/articles/choosing-chart-types/

