# Spec da issue #13 - Validacao e microcopy da UI

## Objetivo

Tornar a interface compreensivel para pessoas que conhecem o experimento, mas
nao precisam memorizar nomes internos de variaveis ou abreviacoes de codigo.

## Escopo deste recorte

- trocar nomes tecnicos dos seletores por descricoes naturais;
- tornar titulos e eixos dos graficos legiveis;
- trocar `+/-` por `±` nos resultados;
- explicar inclinacao e intercepto nas caixas de parametros;
- manter nomes de argumentos Python e chaves de dados inalterados.
- adicionar campos contextuais para `L` e `delta_L` no grafico `lambda x 1/n`;
- remover valores fisicos fixos da interface.

## Dicionario de linguagem

| Uso interno | Texto visivel |
| --- | --- |
| `frequency_inverse_wavelength` | Frequencia em funcao do inverso do comprimento de onda |
| `wavelength_inverse_harmonic` | Comprimento de onda em funcao do inverso do numero harmonico |
| `velocity_sqrt_tension` | Velocidade em funcao da raiz quadrada da tensao |
| `lambda` | comprimento de onda ou `λ`, conforme o contexto |
| `sqrt(tau)` | raiz quadrada da tensao (`√τ`) |
| `a` | inclinacao |
| `b` | intercepto |
| `R2` | coeficiente de determinacao (`R²`) |

## Incertezas e valores de referencia

- O usuario informa as incertezas experimentais na tabela, ao lado da medida.
- A incerteza pode ficar vazia quando nao for conhecida.
- O campo `L` e obrigatorio apenas no grafico `lambda x 1/n`.
- `delta_L` e opcional; sem ele, o valor esperado `2L` aparece sem comparacao
  automatica de compatibilidade.
- A interface nao oferece um botao separado para "mostrar erros": a presenca
  dos valores informados determina as barras de erro.

## Fora de escopo

- Validacao completa de valores e quantidade minima de pontos.
- Alteracao de nomes de funcoes, argumentos ou chaves de dados.
- Mudanca nas formulas ou unidades do dominio.

## Criterios de aceite

- Os tres seletores de grafico usam linguagem natural.
- Titulos, eixos, colunas e parametros sao compreensiveis sem consultar o
  codigo.
- O grafico `lambda x 1/n` nao usa um comprimento da corda fixo no codigo.
- Campos de incerteza ficam proximos das grandezas a que pertencem.
- A unidade continua visivel em cada grandeza.
- Testes atualizados passam sem alterar os contratos cientificos.
