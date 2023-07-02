print ("Bem vindo ao jogo da forca")

palavra_secreta = 'corinthians'
letra_secreta = ['_', '_', '_', '_','_', '_','_', '_','_', '_','_']

acertou = False
enforcou = False
errou = 0

while (not acertou and not enforcou):
    chute = input ('Qual letra?\n')

    posicao = 0
    for i in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_acertadas[posicao] = letra
        posicao += 1
        else:
            erros += 1
        print(letras_acertadas)
        enforcou = erros == 6


