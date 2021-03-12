"""
PEDRA PAPEL E TESOURA

Objetivo:
Ganhar da máquina com uma da opções de pedra papel e tesoura
"""

import random

def tradu(s):
    if s=='t':
        s="Tesoura"
    elif s=='p':
        s="Papel"
    elif s=='r':
        s="Pedra"
    return s

while True:
    while True:
        user=input("""Coloque o elemento que quer usar
        ____________
        |tesoura = t|
        |papel = p  |
        |Pedra = r  |
        |___________|
        """).lower()[0]
        if user=='t' or user=='p' or user=='r':
            break
        else:
            print("Coloque uma opção válida")
    compu=random.choice(['r','p','t'])

    print(f"""
Usuário: {tradu(user)}
Computador: {tradu(compu)}""")
    if user==compu:
        print("EMPATE")
    elif user == 't' and compu == 'p':
        print("VOCÊ GANHOU!!")
    elif user == 'p' and compu == 'r':
        print("VOCÊ GANHOU!!")
    elif user == 'r' and compu == 't':
        print("VOCÊ GANHOU!!")

    elif user == 'r' and compu == 'p':
        print("VOCÊ PERDEU")
    elif user == 't' and compu == 'r':
        print("VOCÊ PERDEU")
    elif user == 'p' and compu == 't':
        print("VOCÊ PERDEU")
    
    if input("Quer continuar jogando? [S/N]").upper()=="N":
        break