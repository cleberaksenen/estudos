# Tutorial sobre Estatística
- O Intervalo de Confiança nos traz a informação intervalar dos estimadores (média). Porém, ele por si só, não traz a informação para afirmarmos algo. Assumindo como verdadeira uma hipótese ou não.

## 🎲🔍 Teste de hipótese
- O teste de hipótese é uma técnica estatística usada para avaliar se uma suposição sobre um parâmetro populacional é plausível, com base em dados amostrais.

### Exemplo:
A média de tempo que um usuário leva para fazer um cadastro em um site é de 3 minutos. Redefinindo o fluxo de cadastro, espera-se obter um número abaixo de 2,5 minutos. Como podemos provar que o objetivo foi alcançado?

- Fazemos então um experimento com 120 usuários em cima do novo fluxo de cadastro, obtendo os resultados:
1. Média = 2,1 minutos
2. DP = 0,32 minutos
3. Nível de confiança (1 - α) = 90%

O objetivo foi atingido?
----
1. Calcular IC:
- IC = Média am. ± (T(1 - α) * (DP am.)) / raiz de n

- IC = 2,1 ± (1,658 * 0,32) / 10,95

- IC = 2,1 ± 0,048

- 2,052 ≤ IC ≤ 2,14