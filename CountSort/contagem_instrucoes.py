def counting_sort_com_contagem(vetor):
    instrucoes = 0

    # Verificação: vetor vazio
    instrucoes += 1  # comparação len(vetor) == 0
    if len(vetor) == 0:
        return vetor, instrucoes

    # Encontrar o maior elemento — percorre todo o vetor (n comparações + 1 atribuição)
    maior_elemento = max(vetor)
    instrucoes += len(vetor) + 1

    # Criar vetor de contagem (k+1 atribuições, onde k = maior_elemento)
    vetor_contagem = [0] * (maior_elemento + 1)
    instrucoes += (maior_elemento + 1)

    # Contar frequências — 2 instruções por iteração (acesso + incremento)
    for numero in vetor:
        instrucoes += 1  # acesso ao elemento
        vetor_contagem[numero] += 1
        instrucoes += 1  # incremento no vetor de contagem

    # Soma cumulativa — 2 instruções por iteração (acesso + soma)
    for i in range(1, len(vetor_contagem)):
        instrucoes += 1  # acesso a vetor_contagem[i-1]
        vetor_contagem[i] += vetor_contagem[i - 1]
        instrucoes += 1  # atribuição da soma

    # Criar vetor de saída (n atribuições + 1 para a criação)
    vetor_saida = [0] * len(vetor)
    instrucoes += len(vetor) + 1

    # Construção do vetor ordenado — 5 instruções por iteração
    for i in range(len(vetor) - 1, -1, -1):
        instrucoes += 1  # acesso a vetor[i]
        numero_atual = vetor[i]
        instrucoes += 1  # cálculo da posição
        posicao_correta = vetor_contagem[numero_atual] - 1
        instrucoes += 1  # atribuição no vetor de saída
        vetor_saida[posicao_correta] = numero_atual
        instrucoes += 1  # decremento do contador
        vetor_contagem[numero_atual] -= 1
        instrucoes += 1  # controle do laço

    return vetor_saida, instrucoes


# demostração
if __name__ == "__main__":
    vetor_desordenado = [9, 5, 2, 4, 2, 8, 5]
    vetor_ordenado, total_passos = counting_sort_com_contagem(vetor_desordenado)

    print(f"Vetor Original:  {vetor_desordenado}")
    print(f"Vetor Ordenado:  {vetor_ordenado}")
    print(f"Total de instruções executadas: {total_passos}")
