import random
import matplotlib.pyplot as plt


def counting_sort_analise(vetor):
    instrucoes = 0
    instrucoes += 1
    if len(vetor) == 0:
        return vetor, instrucoes

    maior_elemento = max(vetor)
    instrucoes += len(vetor) + 1

    vetor_contagem = [0] * (maior_elemento + 1)
    instrucoes += (maior_elemento + 1)

    for numero in vetor:
        instrucoes += 1
        vetor_contagem[numero] += 1
        instrucoes += 1

    for i in range(1, len(vetor_contagem)):
        instrucoes += 1
        vetor_contagem[i] += vetor_contagem[i - 1]
        instrucoes += 1

    vetor_saida = [0] * len(vetor)
    instrucoes += len(vetor) + 1

    for i in range(len(vetor) - 1, -1, -1):
        instrucoes += 1
        numero_atual = vetor[i]
        instrucoes += 1
        posicao_correta = vetor_contagem[numero_atual] - 1
        instrucoes += 1
        vetor_saida[posicao_correta] = numero_atual
        instrucoes += 1
        vetor_contagem[numero_atual] -= 1
        instrucoes += 1

    return vetor_saida, instrucoes


# experimento

tamanhos = [100, 500, 1000, 2000, 3000, 4000, 5000]

instrucoes_ordenado = []
instrucoes_aleatorio = []
instrucoes_decrescente = []

for n in tamanhos:
    # melhor caso — vetor já ordenado (crescente)
    vetor_ordenado = list(range(n))
    _, inst_ordenado = counting_sort_analise(vetor_ordenado)
    instrucoes_ordenado.append(inst_ordenado)

    # caso médio — vetor com valores aleatórios
    vetor_aleatorio = [random.randint(0, n) for _ in range(n)]
    _, inst_aleatorio = counting_sort_analise(vetor_aleatorio)
    instrucoes_aleatorio.append(inst_aleatorio)

    # pior caso — vetor em ordem decrescente
    vetor_decrescente = list(range(n, 0, -1))
    _, inst_decrescente = counting_sort_analise(vetor_decrescente)
    instrucoes_decrescente.append(inst_decrescente)

# geração do grafico

plt.figure(figsize=(10, 6))

plt.plot(tamanhos, instrucoes_ordenado, label='Melhor Caso (Vetor Ordenado)',
         color='green', marker='o')
plt.plot(tamanhos, instrucoes_aleatorio, label='Caso Médio (Vetor Aleatório)',
         color='blue', marker='s')
plt.plot(tamanhos, instrucoes_decrescente, label='Pior Caso (Vetor Decrescente)',
         color='red', marker='x')

plt.title('Análise de Complexidade do Counting Sort', fontsize=14)
plt.xlabel('Tamanho do Vetor de Entrada (n)', fontsize=12)
plt.ylabel('Quantidade de Instruções Executadas', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)

plt.tight_layout()
plt.show()
