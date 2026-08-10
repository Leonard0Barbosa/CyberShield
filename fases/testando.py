VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
RESET = "\033[0m"
LIMPAR = "\033[2J\033[H"

vida = 100
vida_maxima = 100


def mostrar_vida():
    tamanho = 30
    porcentagem = vida / vida_maxima

    cheios = int(porcentagem * tamanho)
    vazios = tamanho - cheios

    barra = "█" * cheios + "░" * vazios

    print(f"{VERDE}❤️ VIDA")
    print(f"   [{barra}]")
    print(f"    {vida}/{vida_maxima} HP{RESET}")


def sofrer_dano(dano):
    global vida

    vida -= dano

    if vida < 0:
        vida = 0

    print(f"\n{VERMELHO}💥 Você sofreu {dano} de dano!{RESET}")


# Jogo
while vida > 0:

    print(LIMPAR)

    mostrar_vida()

    print("\n1 - Sofrer 10 de dano")
    print("2 - Sofrer 25 de dano")
    print("3 - Sofrer 50 de dano")
    print("4 - Sair")

    escolha = input("\nEscolha: ")

    if escolha == "1":
        sofrer_dano(10)

    elif escolha == "2":
        sofrer_dano(25)

    elif escolha == "3":
        sofrer_dano(50)

    elif escolha == "4":
        break

    else:
        print(f"{AMARELO}⚠️ Opção inválida!{RESET}")

    input("\nPressione ENTER para continuar...")


if vida <= 0:
    print(LIMPAR)
    print(f"{VERMELHO}💀 VOCÊ MORREU!{RESET}")
