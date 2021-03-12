"""
FORCA

Objetivo:
Descobrir a palavra, antes que o desenho do 
personagem enforcado seja completado.

NOTA: O arquivo "1formatPalavras.py" deve ser 
executado primeiro, para evitar problemas com a 
formatação das palavras em "palavras.txt".

NOTA2: Os arquivos "1formatPalavras.py", "palavras.txt"
e "2forca.py" devem estar na mesma pasta.
"""
import random

def forca(palavra):
    jogo=[] #lista para colocar as informações da tela
    jogo+="_ "*len(palavra) #ira mostrar a quantidade de letras na palavra
    acerto=0 #a cada acerto é +1 até que o numero de elementos 
            #na palavra seja atingido assim ganhando
    ja_tentou=[] #letras ja inceridas
    while True:
        s="" #string que o jogador ve no console
        for i in jogo:
            s+=i
        print(s)
        print()
        letra=input("Digite a letra: ") #user digita a letra que acha que é
        letra=letra[0] #pega apenas a primeria letra que o user colocou
        if letra in ja_tentou: #se o user colocar uma letra ja incerida
            print(f"Tente uma letra que ainda não tenha usado\nLetras já inceridas: {ja_tentou}")
        else:
            ja_tentou.append(letra) # adiciona na lista de letras ja inceridas
            for i in range(len(palavra)):
                if palavra[i]==letra:
                    jogo[i*2]=letra #devido ao espaco na linha 46 é necessário multiplicar i por
                                    #2 para que a letra certa seja incerida no local correto
                    s=""
                    acerto+=1
            if acerto==len(palavra):
                s=""
                for i in jogo:
                    s+=i
                print(s)
                print("VOCÊ GANHOU!!!")
                break
"""
abre o arquivo com as palavras e coloca 
as palavras em uma lista
"""
arq_palavras=open("palavras.txt", "r")
lista=arq_palavras.read().split(";")
arq_palavras.close()
"""
cria um dicionário para ver se há algum caracter
especial na palavra
"""
schar={
"a":["á","à","â","ã"],
"e":["é","è","ê"],
"i":["í","ì","î"],
"o":["ó","ò","õ","ô"],
"u":["ú","ù","û"]
}
palavra = random.choice(lista)
lpalavra=True
for i in palavra:
    for m,n in schar.items():
        for x in n:
            if x == i:
                lpalavra=False

if lpalavra:
    #jogo
    forca(palavra)
else:
    """essa parte "conserta" a palavra para 
    evitar erros no programa"""
    lista_palavra=[]
    index=[]
    for i in palavra:
        for x,y in schar.items():
            if i in y:
                for letra in palavra:
                    lista_palavra.append(letra)
                lista_palavra[palavra.index(i)]=x
                palavra=""
                for letra in lista_palavra:
                    palavra+=letra
    forca(palavra)