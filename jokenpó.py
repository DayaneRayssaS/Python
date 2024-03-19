import random

def ganhador():
    if (escolha_jogador == escolha_computador):
            return "empate"
    elif(
            (escolha_jogador == "papel" and escolha_computador == "pedra") or
            (escolha_jogador == "tesoura" and escolha_computador == "papel") or
            (escolha_jogador == "pedra" and escolha_computador == "tesoura")
        ):
           
            return "voce ganhou"
        else:
            return "voce perdeu"
        
def JogarJokenpo():
    opcoes = ["pedra", "papel","tesoura"]
    vitorias = 0
    derrotas = 0

    print("ola, tudo bom!")
    print("ESCOLHA: pedra, papel ou tesoura")

    while True:
        escolha_jogador = input("Sua escolha:")
        if escolha_jogador not in opcoes:
            print("escolha invalida. Tente novamente.")
            continue 

        escolha_computador = random.choice(opcoes)

        print(f"Computador escolheu: {escolha_computador}")

       reultado = ganhador(escolha_jogador, escolha_computador)
        print(resultado)

        if resultado == "voce venceu!"
            vitorias += 1
        elif resultado == "voce perdeu":
            derrotas =+ 1 

       print(f"voce tem {vitorias} vitorias e {derrotas} derrotas")

       jogar_novamente = input("voce Quer jogar novamente?").lower()

       if jogar-novamente != "sim":
            break

if __name__ == "__main__":
    JogarJokenpo()