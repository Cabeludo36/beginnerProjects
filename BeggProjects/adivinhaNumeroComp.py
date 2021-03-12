"""
ADIVINHA NUMERO DO COMPUTADOR

Objetivo:
Ver se o computador acerta o numero que você quer
"""

import random

h=0
print("Eu (computador) vou tentar adivinhar o número que você quiser, mas eu preciso de uma dica, qual é o número maximo?")
while True:
    while True:
        try:
            while h<=1:
                h=int(input())
                if h<=1:
                    print("!!! Tente um número maior que 1 !!!")
            break
        except TypeError:
            print("!!!!! Coloque um número !!!!!")

    print("""Agora que ja sei o número máximo que devo tentar, aqui estão algumas instruções:

Caso eu acerte escreva [C], caso eu erre porque o número em mente é maior escreva [H], se for menor escreva [L] e se eu perder [P].

Vamos começar!
""")
    l=1
    while True:
        if l!=h:
            tenta=random.randint(l,h) #colova um número randomico entre l e h e coloca na variável tenta
        else:
            tenta=l # caso os números de l e h sejam iguais, serão colocados na variável tenta
        user=input(f"{tenta} é o número que você tem em mente?\n").upper()
        if user=="C":
            print("\nEBAAAAAA ACERTEI!!!!")
            break
        elif user=="H": #caso o número seja maior, l (menor número) será a tentativa
            l=tenta
        elif user=="L": #caso o número seja menor, h (maior número) será a tentativa
            h=tenta
        elif user=="P": 
            print("AWWWWW, que droga =/")
            break
        else:
            print("Tente rever as instruções")
    if input("\nQuer continuar jogando? [S/N]").upper()=="N":
        break