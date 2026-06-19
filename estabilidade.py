def counting_sort_estavel(vetor):
    if len(vetor) == 0:
        return vetor

    # 1. Encontrar a maior nota (Acessando o índice 0 da tupla)
    maior_nota = max(item[0] for item in vetor)

    # 2. Vetor de contagem
    vetor_contagem = [0] * (maior_nota + 1)

    # 3. Frequências
    for item in vetor:
        nota = item[0]
        vetor_contagem[nota] += 1

    # 4. Soma Cumulativa
    for i in range(1, len(vetor_contagem)):
        vetor_contagem[i] += vetor_contagem[i - 1]

    # 5. Montagem (De trás para frente GARANTE a estabilidade)
    vetor_saida = [None] * len(vetor)
    
    for i in range(len(vetor) - 1, -1, -1):
        item_atual = vetor[i]
        nota = item_atual[0]
        
        posicao_correta = vetor_contagem[nota] - 1
        vetor_saida[posicao_correta] = item_atual
        vetor_contagem[nota] -= 1

    return vetor_saida

# --- TESTE DE ESTABILIDADE ---
# Repare que Matrix aparece ANTES de Shrek (ambos com nota 5)
filmes = [
    (3, "Homem-Aranha"),
    (5, "Matrix"),
    (2, "Lanterna Verde"),
    (5, "Shrek"),
    (4, "Batman")
]

filmes_ordenados = counting_sort_estavel(filmes)

print("Vetor Original:")
for f in filmes: print(f)

print("\nVetor Ordenado:")
for f in filmes_ordenados: print(f)