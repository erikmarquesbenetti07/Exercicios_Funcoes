import itertools

def is_quadrado_magico(matriz):
    # Verifica se a soma das linhas, colunas e diagonais é a mesma
    n = len(matriz)
    soma_referencia = sum(matriz[0])
    
    # Verifica as linhas
    for linha in matriz:
        if sum(linha) != soma_referencia:
            return False
    
    # Verifica as colunas
    for j in range(n):
        if sum(matriz[i][j] for i in range(n)) != soma_referencia:
            return False

    # Verifica a diagonal principal
    if sum(matriz[i][i] for i in range(n)) != soma_referencia:
        return False

    # Verifica a diagonal secundária
    if sum(matriz[i][n - 1 - i] for i in range(n)) != soma_referencia:
        return False

    return True

def gerar_quadrados_magicos():
    numeros = list(range(1, 10))
    permutacoes = itertools.permutations(numeros)
    quadrados_magicos = []

    for permutacao in permutacoes:
        matriz = [list(permutacao[i:i+3]) for i in range(0, 9, 3)]
        if is_quadrado_magico(matriz):
            quadrados_magicos.append(matriz)

    return quadrados_magicos

def exibir_quadrado_magico(quadrado):
    for linha in quadrado:
        print(' '.join(map(str, linha)))
    print()

quadrados_magicos = gerar_quadrados_magicos()

if len(quadrados_magicos) > 0:
    print("Quadrados Mágicos encontrados:")
    for quadrado in quadrados_magicos:
        exibir_quadrado_magico(quadrado)
else:
    print("Nenhum quadrado mágico encontrado.")
