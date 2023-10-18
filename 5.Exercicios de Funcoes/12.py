import random

def embaralhar_string(string):
    # Converte a string para letras minúsculas (ou maiúsculas, se desejado)
    string = string.lower()  # Para garantir que todas as letras sejam em caixa baixa
    lista_caracteres = list(string)
    random.shuffle(lista_caracteres)
    string_embaralhada = ''.join(lista_caracteres)
    return string_embaralhada

# Solicita ao usuário para fornecer uma palavra
palavra = input("Digite uma palavra: ")

# Chama a função para embaralhar a palavra
palavra_embaralhada = embaralhar_string(palavra)

# Exibe o resultado em caixa alta
print(f"A palavra embaralhada é: {palavra_embaralhada.upper()}")
