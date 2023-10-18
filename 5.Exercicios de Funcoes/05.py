def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)  # Calcula o valor do imposto
    custo_com_imposto = custo + imposto  # Adiciona o imposto ao custo
    return custo_com_imposto

# Solicita ao usuário para fornecer a taxa de imposto e o custo do item
taxaImposto = float(input("Digite a taxa de imposto (em porcentagem): "))
custo = float(input("Digite o custo do item: "))

# Chama a função para calcular o custo com imposto
custo_com_imposto = somaImposto(taxaImposto, custo)

# Exibe o custo com imposto
print(f"O custo com imposto é: {custo_com_imposto:.2f}")
