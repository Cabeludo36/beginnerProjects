"""
ADIVINHA O NÚMERO

Objetivo:
Adivinhar o número.
"""

import random
top=0
tenta=0
"""
O número de tentativas tem que ser maior ou igual a 1
e o número máximo tem que ser maior que 1
"""
while True:
    while True:
        try:
            while top<=1:
                top = int(input("Qual é o número máximo: "))
            while tenta<1:
                tenta = int(input("Qual é o número máximo de tentativas: "))
            break
        except ValueError:
            print("!!!! Coloque um número !!!!\n")
    """
    Coloca um número randomico entre 1 e o número 
    colocado pelo usuário na variável x
    """
    x=random.randint(1, top)
    tentou = 0
    while True:
        
        #Vê se o número máximo de tentativas foi alcançado
        if tentou == tenta:
            print(f"Você atingiu o máximo de {tenta} tentativas")
            print("VOCÊ PERDEU")
            break
        while True:
            try:
                tentativa = int(input("Que número você acha que é?\n"))
                break
            except ValueError:
                print("!!!! Coloque um número !!!!\n")
        """
        Vê se o número é igual, maior ou menor que x
        para ver se o jogador ganhou
        """
        if tentativa == x:
            print("PARABENS VOCÊ ACERTOU O NÚMERO")
            break
        elif tentativa<x:
            print("Mais alto")
            tentou=+1
        elif tentativa>x:
            print("Mais baixo")
            tentou+=1

    #Pregunta ao usuário se quer continuar
    if input("Quer jogar novamente? [S/N]\n").upper() == "N":
        break