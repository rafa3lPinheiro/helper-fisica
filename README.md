# Helper Fisica

Ferramenta local para gerar graficos cientificos do experimento de ondas na corda
da disciplina Fisica Experimental 2.

## Estado

Projeto em fase de planejamento e MVP inicial.

Fonte de verdade atual:

- `docs/specs/mvp-ondas-corda.md`

## Requisitos

- Python 3.12+
- Tkinter disponivel na instalacao local do Python

Dependencias Python do MVP:

- NumPy
- SciPy
- Matplotlib

## Instalacao

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

No Linux ou macOS:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Tkinter normalmente acompanha o Python. Em algumas distribuicoes Linux, pode ser
necessario instalar o pacote de sistema correspondente, como `python3-tk`.

## Execucao

```bash
python -m app.main
```

## Graficos previstos no MVP

- Frequencia em funcao do inverso do comprimento de onda: `f x 1/lambda`
- Comprimento de onda em funcao do inverso do harmonico: `lambda x 1/n`
- Velocidade da onda em funcao da raiz da tensao: `v x sqrt(tau)`

## Fluxo de trabalho

- Planejar e discutir antes de implementar.
- Usar GitHub Issues e Milestones para rastreabilidade.
- Usar Conventional Commits em todos os commits.
- Preferir um commit por issue quando o escopo permitir.
