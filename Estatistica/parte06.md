# Tutorial sobre Estatística
## 🎲🎲 Teorema de Bayes
- Teorema que busca obter a probabilidade de um evento com base em experiências passadas 

Probabilidade condicional: 

P(A∣B) = P(A∩B) / P(B) 

⬇️

Teorema de Bayes:

P(A∣B) = P(A) * P(B∣A) / P(B)

### Exemplos:
- Qual a probabilidade do resultado do lançamento de um dado ser 4, sabendo que o resultado foi par?
1) P(A) [ser 4] = 1/6
2) P(B) [ser par] = 1/2
3) P(B|A) [ser par, dado que é 4] = 1

P(A∣B) = P(A) * P(B∣A) / P(B)

P(A∣B) = 1/6 * 1 / 1/2 

P(A∣B) = 1/3

- Lancei 2 dados. Qual a probabilidade do resultado de um dado ser 3, dado que o resultado do outro dado foi 2?
1) P(A) [ser 3] = 1/6
2) P(B) [ser 2] = 1/6
3) P(B|A) [ser 2, dado primeiro é 3] = 1/6

P(A∣B) = P(A) * P(B∣A) / P(B)

P(A∣B) = 1/6 * 1/6 / 1/6

P(A∣B) = 1/6

- Monty Hall: Há três portas fechadas. Atrás de uma dessas portas há um prêmio valioso e atrás das outras duas não há nada. O participante escolhe inicialmente uma das portas, mas ela não é aberta de imediato. Em seguida, o apresentador, que sabe o que está por trás de cada porta, abre uma das duas portas restantes, sempre revelando um bode. Após isso, ele oferece ao participante a chance de manter sua escolha original ou trocar para a outra porta que ainda permanece fechada. A pergunta central do problema é: o participante deve manter sua escolha inicial ou trocar de porta para aumentar suas chances de ganhar o carro?

1) P(E1) [Prêmio na porta 1] = 1/3
2) P(E2) [Prêmio na porta 2] = 1/3
3) P(E3) [Prêmio na porta 3] = 1/3
---
4) Evento D - Porta 1 está vazia

P(E∣D) = P(E) * P(D∣E) / P(D)

- P(E1∣D) = P(E1) * P(D∣E1) / P(D) -> 1/3 * 0 / 1 = 0

- P(E2∣D) = P(E2) * P(D∣E2) / P(D) -> 1/3 * 1 / 1 = 1/3

- P(E3∣D) = P(E3) * P(D∣E3) / P(D) -> 1/3 * 1 / 1/2 = 1/6