"""
FORCA FORMAT

Objetivo:
Formatar as palavras do arquivo 
palavras, para ser usado em forca.py
"""
palavras=open("palavras.txt", "r")
lista=palavras.read().split("\n")
palavras.close()

palavras=open("palavras.txt", "w")
for i in lista:
    palavras.write(i)
palavras.close()