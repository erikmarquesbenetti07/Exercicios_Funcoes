def verifica_positivo_negativo(numero):
    if numero > 0:
        return 'P'
    elif numero <= 0:
        return 'N'

# Solicita ao usuário para fornecer um número
numero = float(input("Digite um número: "))

# Chama a função para verificar se o número é positivo ou negativo
resultado = verifica_positivo_negativo(numero)

# Exibe o resultado
print(f"O valor é {resultado}")
