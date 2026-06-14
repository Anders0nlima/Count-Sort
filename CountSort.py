def counting_sort(vetor):
    if len(vetor) == 0:
        return vetor
    
    maior_elemento = max(vetor)

    vetor_contagem = [0] * (maior_elemento + 1)

    for numero in vetor:
        vetor_contagem[numero] += 1

    for i in range(1 , len(vetor_contagem)):
        vetor_contagem[i] += vetor_contagem[i - 1]
    
    vetor_saida = [0] * len(vetor)

    for i in range(len(vetor) -1, -1, -1):
        numero_atual = vetor[i]

        posicao_correta = vetor_contagem[numero_atual] - 1

        vetor_saida[posicao_correta] = numero_atual

        vetor_contagem[numero_atual] -= 1

    return vetor_saida



vetor_desordenado = [9, 5, 2, 4, 2, 8, 5]
vetor_ordenado = counting_sort(vetor_desordenado)

print(f"Vetor Original: {vetor_desordenado}")
print(f"Vetor Ordenado: {vetor_ordenado}")