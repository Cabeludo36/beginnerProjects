"""
BUSCA BINÁRIA

Busca binária é mais rápida que busca nativa


Busca nativa: checa cada elemento da lista para
ver se é igual ao alvo.

Se for, retorna o index
Se não, retorna -1
"""
import random
import time

def busca_nativa(l, alvo):
    #l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == alvo:
            return i
    return -1

#Busca binária: Usa dividir e conquistar
#Vamos imaginar que a lista está em ordem crescente  
def busca_binaria(l, alvo, menor=None, maior=None):
    if menor is None:
        menor = 0
    if maior is None:
        maior = len(l)-1
    
    if maior < menor:
        return -1

    # l = [1, 3, 5, 10, 12] #deve retornar index 3 (10)
    pontoMed = (menor + maior)//2
    
    if l[pontoMed] == alvo:
        return pontoMed
    elif alvo < l[pontoMed]:
        return busca_binaria(l, alvo, menor, pontoMed-1)
    else:
        #alvo > l[pontomed]
        return busca_binaria(l,alvo, pontoMed+1, maior)

if __name__=="__main__":

     
    #Em uma pequena lista irão retornar o mesmo valor 
    #quase que ao mesmo tempo como em

    ##l = [1, 3, 5, 10, 12]
    ##alvo = 10
    ##print(busca_nativa(l, alvo))
    ##print(busca_binaria(l,alvo))

    #output vai ser:
    #3
    #3

    #Mas em uma lista maior é diferente

    tamanho = 10000
    #faz uma lista com 10000 elementos em ordem crescente
    lista_cres = set()
    while len(lista_cres) < tamanho:
        #Os numeros vao ser entre -30000 e 30000
        lista_cres.add(random.randint(-3*tamanho, 3*tamanho))
    lista_cres = sorted(list(lista_cres))

    start = time.time()
    #vai passar procurando cada elemento da lista de novo e de novo,
    #ou seja, ira rodar 10000 vezes, cada vez procurando um elementeto
    for alvo in lista_cres:
        busca_nativa(lista_cres, tamanho)
    fim = time.time()
    print("Tempo da busca nativa: ", (fim-start)/tamanho, " segundos por volta.")

    #Mesmo procedimento que o de cima, mas busca binaria
    start = time.time()
    for alvo in lista_cres:
        busca_binaria(lista_cres, tamanho)
    fim = time.time()
    print("Tempo da busca binaria: ", (fim-start)/tamanho, " segundos por volta.")
    