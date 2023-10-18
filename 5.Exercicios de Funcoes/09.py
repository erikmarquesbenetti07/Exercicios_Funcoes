def inverter_numero(numero):
    numero_reverso = 0
    while numero > 0:
        digito = numero % 10
        numero_reverso = numero_reverso * 10 + digito
        numero //= 10
    return numero_reverso

# Solicita ao usuário para fornecer um número inteiro
numero = int(input("Digite um número inteiro: "))

# Chama a função para inverter o número
numero_reverso = inverter_numero(numero)

# Exibe o número reverso
print(f"O reverso do número {numero} é {numero_reverso}")
