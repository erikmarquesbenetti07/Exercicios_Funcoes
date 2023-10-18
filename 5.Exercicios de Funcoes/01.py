def imprimir_padrao(n):
    for i in range(1, n + 1):
        # Use o valor de 'i' para repetir o número 'i' vezes na linha
        for j in range(i):
            print(i, end=" ")
        print()  # Pula para a próxima linha

# Solicita ao usuário para fornecer o valor de 'n'
n = int(input("Digite um valor para n: "))

# Chama a função para imprimir o padrão
imprimir_padrao(n)
