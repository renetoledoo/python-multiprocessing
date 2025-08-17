# 🐍 Python Multiprocessamento – Aumento de Performance

Exemplo de cálculo pesado em Python e análise de performance.  

![Python](https://img.shields.io/badge/python-3.10-blue?logo=python&logoColor=white)
![Performance](https://img.shields.io/badge/performance-high-green)
![Code](https://img.shields.io/badge/code-example-orange)



##  Função `computar`

A função abaixo realiza um cálculo matemático intenso. Sem qualquer técnica de otimização ou multiprocessamento, levou aproximadamente **9,2 segundos** para processar o intervalo de **1 a 50.000.000** em uma CPU de teste.

```python
import math

def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))
```
#  Análise de Performance – Multiprocessamento em Python

O cálculo realizado pela função `computar` é **CPU-bound**, ou seja, limitado pelo poder de processamento da CPU. Isso significa que a execução sequencial consome bastante tempo para grandes volumes de dados.



## Resultados

- **Execução sequencial:** ~9,2 segundos (processando de 1 a 50.000.000)
- **Execução com multiprocessamento:** ~2 segundos (dividindo o trabalho entre múltiplos núcleos)



##  Explicação

Ao aplicar **multiprocessamento**, o cálculo foi dividido em processos independentes, cada um rodando em um núcleo diferente da CPU. Isso permite:

1. **Paralelismo real:** múltiplos cálculos acontecendo ao mesmo tempo.
2. **Uso eficiente de recursos:** aproveita todos os núcleos disponíveis.
3. **Redução de tempo:** tarefas CPU-bound são concluídas muito mais rápido.



##  Benefícios do Multiprocessamento

- Cada processo roda em **núcleo separado da CPU**, evitando gargalos.
- **Redução significativa do tempo de execução** em tarefas pesadas.
