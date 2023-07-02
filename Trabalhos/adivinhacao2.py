print("Bem-vindo ao jogo da adivinhação")

numero_magico = 42

total_de_tentativas = 0
rodada = 1

nivel = int(input("Qual nivel de dificuldade você deseja seguir? 1-fácil 2-médio 3-dificil" /n))

if(nivel == 1):
    total_de_tentativas = 10
elif(nivel == 2):
    total_de_tentativas = 5
elif(nivel == 3):
    total_de_tentativas = 3
else:
    print("Opção inválida")


for i in total_de_tentativas:
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute = 0

    while (chute < 0 and chute > 100):
        chute = int(input("Tente adivinhar o número magico, faça um chute \n"))

    if (chute == numero_magico):
        print("Você acertou")
    elif (chute > numero_magico):
        print("Errou, chutou alto")
    else:
        print("Errou, chutou baixo")

    rodada = rodada + 1