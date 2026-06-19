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

# --- Configuração do Experimento ---
# Vamos testar o algoritmo com vetores de tamanhos crescentes
tamanhos = [100, 500, 1000, 2000, 3000, 4000, 5000]

instrucoes_melhor = []
instrucoes_medio = []
instrucoes_pior = []

for n in tamanhos:
    # 1. Melhor Caso
    vetor_melhor = [random.randint(0, 10) for _ in range(n)]
    _, inst_melhor = counting_sort_analise(vetor_melhor)
    instrucoes_melhor.append(inst_melhor)
    
    # 2. Caso Médio
    vetor_medio = [random.randint(0, n) for _ in range(n)]
    _, inst_medio = counting_sort_analise(vetor_medio)
    instrucoes_medio.append(inst_medio)
    
    # 3. Pior Caso
    vetor_pior = [random.randint(0, n * 10) for _ in range(n)]
    _, inst_pior = counting_sort_analise(vetor_pior)
    instrucoes_pior.append(inst_pior)

plt.figure(figsize=(10, 6))

plt.plot(tamanhos, instrucoes_melhor, label='Melhor Caso (k = 10)', color='green', marker='o')
plt.plot(tamanhos, instrucoes_medio, label='Caso Médio (k = n)', color='blue', marker='s')
plt.plot(tamanhos, instrucoes_pior, label='Pior Caso (k = n * 10)', color='red', marker='x')

plt.title('Análise de Complexidade do Counting Sort', fontsize=14)
plt.xlabel('Tamanho do Vetor de Entrada (n)', fontsize=12)
plt.ylabel('Quantidade de Instruções Executadas', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)

plt.show()