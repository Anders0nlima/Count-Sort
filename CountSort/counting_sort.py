def counting_sort(vetor):
    # Caso base: vetor vazio
    if len(vetor) == 0:
        return vetor

    # Etapa 1: Encontrar o maior elemento
    maior_elemento = max(vetor)

    # Etapa 2: Criar vetor de contagem e registrar frequências
    # Cada índice do vetor_contagem representa um valor possível (0 até maior_elemento).
    vetor_contagem = [0] * (maior_elemento + 1)

    for numero in vetor:
        vetor_contagem[numero] += 1
    # Exemplo: vetor = [9, 5, 2, 4, 2, 8, 5]
    #          vetor_contagem = [0, 0, 2, 0, 1, 2, 0, 0, 1, 1]
    #          (o valor 2 aparece 2 vezes, o 5 aparece 2 vezes, etc.)

    # Etapa 3: Soma cumulativa
    # Agora vetor_contagem[i] indica quantos elementos possuem valor ≤ i.
    for i in range(1, len(vetor_contagem)):
        vetor_contagem[i] += vetor_contagem[i - 1]
    # Continuando o exemplo: vetor_contagem = [0, 0, 2, 2, 3, 5, 5, 5, 6, 7]

    # Etapa 4: Construir vetor de saída (de trás para frente)
    # Percorrer de trás para frente garante que a ESTABILIDADE é mantida,
    # ou seja, elementos com mesmo valor preservam a ordem relativa original.
    vetor_saida = [0] * len(vetor)

    for i in range(len(vetor) - 1, -1, -1):
        numero_atual = vetor[i]
        posicao_correta = vetor_contagem[numero_atual] - 1
        vetor_saida[posicao_correta] = numero_atual
        vetor_contagem[numero_atual] -= 1

    return vetor_saida


# demostração
if __name__ == "__main__":
    vetor_original = [9, 5, 2, 4, 2, 8, 5]
    vetor_ordenado = counting_sort(vetor_original)

    print(f"Vetor Original: {vetor_original}")
    print(f"Vetor Ordenado: {vetor_ordenado}")
