def counting_sort_estavel(vetor):
    # --- etapa 1: vetor de contagem (frequência) ---
    max_preco = max(item[1] for item in vetor)
    # max_preco = 3  (GOOG custa 3)

    vetor_contagem = [0] * (max_preco + 1)
    # [0, 0, 0, 0]  → índices representam preços 0, 1, 2, 3

    for item in vetor:
        preco = item[1]
        vetor_contagem[preco] += 1
    # [0, 2, 0, 1]  → preço 1 aparece 2x, preço 3 aparece 1x

    # --- etapa 2: soma cumulativa (posição final) ---
    for i in range(1, len(vetor_contagem)):
        vetor_contagem[i] += vetor_contagem[i - 1]
    # [0, 2, 2, 3]  → counts[i] = quantos elementos têm chave ≤ i

    # --- etapa 3: construção do vetor de saída ---
    # iteramos de TRÁS PARA FRENTE — isso é o que garante a estabilidade!
    # o primeiro elemento que chega (da iteração reversa) fica na posição maior;
    # o segundo (que veio antes no original) fica na posição menor → ordem preservada.
    vetor_saida = [None] * len(vetor)

    for i in range(len(vetor) - 1, -1, -1):
        item_atual = vetor[i]
        preco = item_atual[1]

        posicao_correta = vetor_contagem[preco] - 1
        vetor_saida[posicao_correta] = item_atual
        vetor_contagem[preco] -= 1
    
    for i in range(0, len(vetor)):
        item_atual = vetor[i]
        preco = item_atual[1]

        posicao_correta = vetor_contagem[preco] - 1
        vetor_saida[posicao_correta] = item_atual
        vetor_contagem[preco] -= 1

    return vetor_saida


acoes = [
    ("A", 3),
    ("B", 1),
    ("C", 1),
]

# Passo a passo:
# i=2 → MSFT (preço 1): counts[1]=2 → posição 1 → counts[1]=1
# i=1 → CSCO (preço 1): counts[1]=1 → posição 0 → counts[1]=0  ← CSCO fica ANTES de MSFT ✓
# i=0 → GOOG (preço 3): counts[3]=3 → posição 2 → counts[3]=2

acoes_ordenadas = counting_sort_estavel(acoes)
print(acoes_ordenadas)
# [('CSCO', 1), ('MSFT', 1), ('GOOG', 3)]