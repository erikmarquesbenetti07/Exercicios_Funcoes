def soma_tres_numeros(a, b, c):
    resultado = a + b + c
    return resultado

# Solicita ao usuário para fornecer os três números
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

# Chama a função para calcular a soma
soma = soma_tres_numeros(a, b, c)

# Exibe o resultado
print(f"A soma de {a}, {b} e {c} é igual a {soma}")
