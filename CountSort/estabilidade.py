def counting_sort_estavel(vetor):
    if len(vetor) == 0:
        return vetor

    # Encontrar a maior chave
    maior_chave = max(item[0] for item in vetor)

    # Vetor de contagem: frequência de cada chave
    vetor_contagem = [0] * (maior_chave + 1)

    for item in vetor:
        chave = item[0]
        vetor_contagem[chave] += 1

    # Soma cumulativa (prefix sum)
    for i in range(1, len(vetor_contagem)):
        vetor_contagem[i] += vetor_contagem[i - 1]

    # Construção do vetor de saída — de trás para frente (garante estabilidade!)
    vetor_saida = [None] * len(vetor)

    for i in range(len(vetor) - 1, -1, -1):
        item_atual = vetor[i]
        chave = item_atual[0]

        posicao_correta = vetor_contagem[chave] - 1
        vetor_saida[posicao_correta] = item_atual
        vetor_contagem[chave] -= 1

    return vetor_saida


def verificar_estabilidade(vetor_original, vetor_ordenado):
    # Agrupar por chave, preservando a ordem de aparição
    from collections import defaultdict

    ordem_original = defaultdict(list)
    ordem_ordenada = defaultdict(list)

    for item in vetor_original:
        ordem_original[item[0]].append(item[1])

    for item in vetor_ordenado:
        ordem_ordenada[item[0]].append(item[1])

    # Para cada chave, a sequência de identificadores deve ser idêntica
    for chave in ordem_original:
        if ordem_original[chave] != ordem_ordenada[chave]:
            return False

    return True

# experimento
acoes = [
    (3, "A"),
    (1, "B"),
    (1, "C"),
]

print("Vetor Original:")
for a in acoes:
    print(f"Preço {a[0]}: {a[1]}")

acoes_ordenadas = counting_sort_estavel(acoes)

print("Vetor Ordenado:")
for a in acoes_ordenadas:
    print(f"Preço {a[0]}: {a[1]}")

estavel_2 = verificar_estabilidade(acoes, acoes_ordenadas)