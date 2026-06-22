def counting_sort_estavel(vetor):
    maior_nota = max(item[0] for item in vetor)
    # 5

    vetor_contagem = [0] * (maior_nota + 1)
    # [0, 0, 0, 0, 0, 0]

    for item in vetor:
        nota = item[0]
        vetor_contagem[nota] += 1
    # [0, 0, 1, 1, 1, 2] -> frequencia

    for i in range(1, len(vetor_contagem)):
        vetor_contagem[i] += vetor_contagem[i - 1]
    # [0, 0, 1, 2, 3, 5] -> soma acumualtiva

    #------

    vetor_saida = [None] * len(vetor)

    for i in range(len(vetor) - 1, -1, -1):
        item_atual = vetor[i]
        nota = item_atual[0]

        posicao_correta = vetor_contagem[nota] - 1
        vetor_saida[posicao_correta] = item_atual
        vetor_contagem[nota] -= 1

    return vetor_saida

filmes = [
    (3, "AVATAR"),
    (5, "TITANIC"),
    (2, "MATRIX"),
    (5, "BATMAN"),
    (4, "INTERESTELAR")
]

filmes_ordenados = counting_sort_estavel(filmes)

print(filmes_ordenados)

"""
[None, None, None, None, None]

for i in range(len(vetor) - 1, -1, -1):
(len(vetor) - 1) começa do ultimo elemento do vetor
-1 (vai de direita pra esquerda)
-1 (decrementa 1)

primeira passada 
[
 (3, "avatar"), 
 (5, "titanic"),   
 (2, "matrix"), 
 (5, "batman"), 
 (4, "interestelar")
]

item_atual = (4, "interestelar")
nota = 4
posicao_correta = soma_acumulada - 1 = 2

vetor_saida[posicao_correta] = item_atual

[None, None, (4, "interestelar"), None, None]

assim por diante, nessa ordem:
(3, 5, 2, 5, 4)
<--------------
note que o 5 na possição 3 vai ficar mais a direita na ordenção enquanto que o 5 da posição 1 vai ficar mais a esquerda. 

"""
