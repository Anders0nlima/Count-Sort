def counting_sort(vetor):
    if len(vetor) == 0: # caso o vetor esteja vazio (opcional)
        return vetor
    
    #return vetor
    maior_elemento = max(vetor) # 9

    vetor_contagem = [0] * (maior_elemento + 1) 
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for numero in vetor:
        vetor_contagem[numero] += 1
    
    #[0, 0, 2, 0, 1, 2, 0, 0, 1, 1]

    for i in range(1, len(vetor_contagem)):
        vetor_contagem[i] += vetor_contagem[i - 1]
    
    #[0, 0, 2, 2, 3, 5, 5, 5, 6, 7]
    
    vetor_saida = [0] * len(vetor)
    #[0, 0, 0, 0, 0, 0, 0]

    for i in range(len(vetor) -1, -1, -1):
        numero_atual = vetor[i] #9
        posicao_correta = vetor_contagem[numero_atual] - 1 #6
        vetor_saida[posicao_correta] = numero_atual 
        #[0, 2, 4, 0, 5, 8, 9]
        vetor_contagem[numero_atual] -= 1
        #[2, 2, 4, 5, 5, 8, 9]

    return vetor_saida

vetor = [0]
print(counting_sort(vetor))