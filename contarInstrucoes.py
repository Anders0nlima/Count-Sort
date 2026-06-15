def counting_sort(vetor):

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

    for i in range(1 , len(vetor_contagem)):
        instrucoes += 1
        vetor_contagem[i] += vetor_contagem[i - 1]
        instrucoes += 1
    
    vetor_saida = [0] * len(vetor)
    instrucoes += len(vetor) + 1

    for i in range(len(vetor) -1, -1, -1):
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



vetor_desordenado = [9, 5, 2, 4, 2, 8, 5]
vetor_ordenado, total_passos = counting_sort(vetor_desordenado)

print(f"Vetor Original: {vetor_desordenado}")
print(f"Vetor Ordenado: {vetor_ordenado}")
print(f"Total de instruções executadas: {total_passos}")