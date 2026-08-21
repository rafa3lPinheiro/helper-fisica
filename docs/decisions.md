# Decisoes do projeto

## 2026-08-21 - Fluxo de trabalho inicial

O projeto usara GitHub como fonte de rastreabilidade operacional, com Issues e
Milestones para organizar o MVP.

Decisoes:

- O repositorio sera publico no GitHub de Rafa.
- Commits devem seguir Conventional Commits.
- O trabalho deve ser planejado e discutido antes de implementacao.
- A spec inicial do MVP fica em `docs/specs/mvp-ondas-corda.md`.

## 2026-08-21 - Specs pequenas por issue

O projeto deve manter specs pequenas e vivas para cada recorte de implementacao.

Decisoes:

- Antes de implementar uma issue de codigo, criar ou atualizar uma spec em
  `docs/specs/`.
- A spec da issue deve registrar objetivo, escopo, fora de escopo, contratos,
  criterios de aceite, testes esperados e dependencias.
- A issue e o commit devem apontar para o mesmo recorte de trabalho sempre que
  possivel.

Observacao retroativa:

- As issues #1 e #2 foram implementadas antes desta politica ficar explicita.
  Para corrigir o harness do projeto, foram adicionadas specs retroativas para
  registrar objetivo, escopo, contratos, validacao e rastreabilidade desses
  recortes.
