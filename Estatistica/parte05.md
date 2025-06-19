# Tutorial sobre Estatística
## 🎲 Probabilidade
### Evento 
- Possíveis resultados observados em um experimento

Ex. lançar uma moeda - CARA |  COROA
Ex. lançar uma dado - 1 | 2 | 3 | 4 | 5 | 6
Ex. Entrevista sobre estado - AM | CE | PE...
Ex. Nota de um estudante - valores contínuos

- Cada evento tem uma probabilidade associada

### Espaço amostral (Ω)
- Espaço onde todas as possibilidade do evento podem ocorrer (são definidos)

### Probabilidade associada ao evento (P(E))
- Axiomas:
1) 0 ≤ P(E) ≤ 1
2) P(E1) + P(E2) + P(E3)... = P(Ω) = 1
(considerando eventos mutuamente exclusivos)

- Como calcular (definir) a probabilidade:
1) Definir uma probabilidade
2) Realizando experimentos
3) Assumindo uma função que gera os dados
4) Experiências passadas (Bayesiana)

### Probabilidade condicional (P(A∣B))
- Probabilidade de um evento acontecer quando se tem uma informação a mais sobre esse evento

P(A\B) -> predizer A, quando ja se sabe B


Ex. Qual a probabilidade de se acertar o valor de um dado de 6 lados, sabendo que é par? 1/3 (P(A\B))
- P(A) [acertar o valor] = 1/6
- P(B) [ser par] = 1/2

-> Esses eventos não são exclusivos, ou seja, há a possibilidade de acontecerem ao mesmo tempo. Dessa forma, não posso soma-los!

->  A ∩ B: sair o número x, e esse número ser par ao mesmo tempo = 1/6

O espaço amostral só muda quando você está calculando uma probabilidade condicional. Mas quando você calcula P(A ∩ B), você ainda está no espaço amostral original, ou seja, aquele com 6 resultados possíveis, porque ainda não condicionou nada.

Portanto:
- P(A∣B) = P(A∩B) / P(B)

P(A∣B) = 1/6 / 1/2 = 1/3

### Probabilidade conjunta (P(A∩B))
- Probabilidade de dois ou mais eventos acontecerem simultaneamente

P(A∩B) = P(A) * P(B∣A) = P(B) * P(A∣B)

Ex.
- P(A) [Sair 3] = 1/6
- P(B) [Sair par] = 1/3
- P(B∣A) [Sair 3 dado que é par] = 0

Portanto: P(A∩B) = 0

- Para eventos independentes, temos:

Ex.
- P(A) [Sair 3 em um dado] = 1/6
- P(B∣A) [Sair 3 em outro dado, dado que saiu 3 no primeiro] = 1/6 (um não interfere no resultado do outro)

Portanto: P(A∩B) = 1/6 * 1/6 = 1/36
​
 

