def converter_horas(horas, minutos):
    if horas < 12:
        periodo = 'A.M.'
        if horas == 0:
            horas = 12  # 0 horas em 12 horas é 12 A.M.
    else:
        periodo = 'P.M.'
        if horas != 12:
            horas -= 12  # Converte horas de 24 para 12 horas, exceto 12 P.M.
    return horas, minutos, periodo

def exibir_horas(horas, minutos, periodo):
    print(f"A hora é: {horas}:{minutos:02d} {periodo}")

while True:
    try:
        horas = int(input("Digite as horas (0-23): "))
        minutos = int(input("Digite os minutos (0-59): "))
        
        if 0 <= horas <= 23 and 0 <= minutos <= 59:
            horas, minutos, periodo = converter_horas(horas, minutos)
            exibir_horas(horas, minutos, periodo)
        else:
            print("Horas ou minutos fora do intervalo válido.")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números inteiros.")

    repetir = input("Deseja converter outra hora? (S para Sim, qualquer outra tecla para sair): ").strip().lower()
    if repetir != 's':
        break
