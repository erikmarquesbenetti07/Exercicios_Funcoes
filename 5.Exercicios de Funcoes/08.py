def contar_digitos(numero):
    if numero < 0:
        numero = -numero  # Lida com números negativos

    if numero == 0:
        return 1  # 0 tem um dígito

    contagem = 0
    while numero > 0:
        contagem += 1
        numero //= 10  # Divide o número por 10 para remover o último dígito

    return contagem

# Solicita ao usuário para fornecer um número inteiro
numero = int(input("Digite um número inteiro: "))

# Chama a função para contar os dígitos
quantidade_digitos = contar_digitos(numero)

# Exibe o resultado
print(f"O número {numero} tem {quantidade_digitos} dígitos.")
