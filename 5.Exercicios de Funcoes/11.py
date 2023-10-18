from datetime import datetime

def data_por_extenso(data_str):
    try:
        data = datetime.strptime(data_str, '%d/%m/%Y')
        mes_extenso = data.strftime('%B')
        dia = data.day
        ano = data.year
        data_formatada = f"{dia} de {mes_extenso} de {ano}"
        return data_formatada
    except ValueError:
        return "NULL"

# Solicita ao usuário para fornecer uma data
data_str = input("Digite uma data no formato DD/MM/AAAA: ")

data_extenso = data_por_extenso(data_str)
if data_extenso == "NULL":
    print("Data inválida.")
else:
    print(f"A data por extenso é: {data_extenso}")
