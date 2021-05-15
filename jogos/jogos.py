import forca
import adivinhacao

print("*****************")
print("Escolha seu jogo!")
print("*****************")

print("(1) Forca (2) Adivinhacao")
selecionado = input("Digite: ")

if(selecionado == "1"):
    print("Jogando Forca")
    forca.jogar()
elif(selecionado == "2"):
    print("Jogando Adivinhacao")
    adivinhacao.jogar()