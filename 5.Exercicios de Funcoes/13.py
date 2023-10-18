def desenhar_retangulo(linhas=1, colunas=1):
    # Limita o número de linhas e colunas dentro dos valores permitidos (entre 1 e 20)
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))

    for i in range(linhas):
        if i == 0 or i == linhas - 1:
            # Primeira e última linha: desenha uma linha horizontal de '+'
            print('+' + '-' * (colunas - 2) + '+')
        else:
            # Linhas intermediárias: desenha '|' nas bordas e espaços no meio
            print('|' + ' ' * (colunas - 2) + '|')

# Solicita ao usuário para fornecer o número de linhas e colunas
linhas = int(input("Digite o número de linhas (entre 1 e 20): "))
colunas = int(input("Digite o número de colunas (entre 1 e 20): "))

# Chama a função para desenhar o retângulo
desenhar_retangulo(linhas, colunas)
