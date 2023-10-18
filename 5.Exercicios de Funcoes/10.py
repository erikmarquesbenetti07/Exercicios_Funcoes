import random

def jogar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def craps():
    while True:
        input("Pressione Enter para lançar os dados...")
        valor_dados = jogar_dados()
        print(f"Você lançou os dados e obteve um total de {valor_dados}.")

        if valor_dados in (7, 11):
            print("Você ganhou! É um natural.")
            break
        elif valor_dados in (2, 3, 12):
            print("Você perdeu! É um craps.")
            break
        else:
            print(f"Seu Ponto é {valor_dados}. Continue jogando para tentar igualar o Ponto ou tirar um 7.")

        while True:
            input("Pressione Enter para lançar os dados novamente...")
            novo_valor_dados = jogar_dados()
            print(f"Você lançou os dados novamente e obteve um total de {novo_valor_dados}.")
            
            if novo_valor_dados == valor_dados:
                print("Você ganhou! Igualou o Ponto. Parabéns!")
                return
            elif novo_valor_dados == 7:
                print("Você perdeu! Tirou um 7 antes de igualar o Ponto.")
                return

if __name__ == "__main__":
    print("Bem-vindo ao jogo de Craps!")
    while True:
        craps()
        jogar_novamente = input("Deseja jogar novamente? (S para sim, qualquer outra tecla para sair): ").strip().lower()
        if jogar_novamente != 's':
            break
