import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    min = 1
    max = 100
    numero_secreto = random.randrange(min, max+1)
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute_str = input(f"Digite um número entre {min} e {max}: ")
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print(f"Você errou! Você deve digitar um número entre {min} e {max}")
            continue

        acertou = chute == numero_secreto;

        if(acertou):
            print(f"Você acertou e fez {pontos}!")
            break
        else:
            if(chute > numero_secreto):
                print("Você errou! O seu chute foi maior que o número secreto.")
            else:
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(chute - numero_secreto)
            pontos -= pontos_perdidos
            if(rodada == total_de_tentativas):
                print(f"O número secreto era {numero_secreto}. Você fez {pontos} pontos")

    print(f"Fim do jogo")

if(__name__ == "__main__"):
    jogar()