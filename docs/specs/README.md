# Specs do projeto

Este diretorio guarda as especificacoes vivas do projeto.

## Politica

- A spec grande do MVP define o produto e o comportamento esperado em alto nivel.
- Cada issue de implementacao deve ter uma spec curta antes do codigo.
- A spec da issue deve registrar objetivo, escopo, fora de escopo, contratos,
  criterios de aceite, testes esperados e dependencias.
- Quando uma decisao mudar comportamento ou arquitetura, atualizar a spec
  correspondente antes ou junto do codigo.
- Issues pequenas de documentacao ou governanca podem apontar para a propria
  alteracao documental quando nao houver comportamento de aplicacao.

## Specs atuais

- `mvp-ondas-corda.md`: spec principal do MVP.
- `issue-1-python-scaffold.md`: scaffold Python e dependencias do MVP.
- `issue-2-quality-baseline.md`: qualidade basica e setup de testes.
- `issue-3-domain-models.md`: modelos de dados do dominio.
- `issue-4-wave-physics-functions.md`: funcoes fisicas de ondas na corda.
- `issue-5-uncertainty-propagation.md`: propagacao de incertezas das grandezas derivadas.
- `issue-6-linear-regression.md`: regressao linear e incerteza dos parametros.
- `issue-7-plot-builder.md`: builder de graficos cientificos com Matplotlib.
