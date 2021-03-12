"""
RESOLVEDOR DE SODOKU

Resolve problemas de sodoku 3x3 usando backtraking

O problema é uma lista de listas, onde cada sub lista é uma linha no problema
retorna se a solução existir.
Muda o problema para ser a solução (se a solução existir)
"""
def encontrar_proximo_vazio(problema):
    #encontra a próxima linha e coluna no problema que esta vazia --> rep com -1
    #retorna a tupla (linha, coluna) (ou (None, None) se não há nenhum)

    #tenha na cabeça que estamos usando 0-8 para os índices
    for l in range(9):
        for c in range(9):
               if problema[l][c] == -1:
                   return l, c
    return None, None #se não houver mais espaços vazios (-1)

def evalido(problema, suposicao, linha, coluna):
    #vê se a suposiçãoo no linha/coluna do problema é válida
    #retorna True, se não retorna False

    #linhas
    linha_valor = problema[linha]
    if suposicao in linha_valor:
        return False
    
    #coluna
    coluna_valor = []
    for i in range(9):
        coluna_valor.append(problema[i][coluna])
    if suposicao in coluna_valor:
        return False
    
    #Quadrado
    #queremos encontrar aonde o quadrado 3x3 começa
    #e interar nos 3 valores na linha/coluna
    linha_comeca = (linha // 3) * 3 # 1//3 = 0, 5//3=1, ...
    coluna_comeca = (coluna // 3) * 3 

    for l in range(linha_comeca, linha_comeca + 3 ):
        for c in range (coluna_comeca, coluna_comeca + 3):
            if problema[l][c] == suposicao:
                return False
    
    #se chegar aqui, ele passou pelas checagens
    return True

def resolve_sodoku(problema):
     #encontra um lugar no problema para fazer uma suposição
    linha, coluna = encontrar_proximo_vazio(problema)

    #se não houver mais lugares, então acabou, pois só podemos 
    #colocar inputs válidos
    if linha is None:
        return True
    
    #se ainda houver lugares para colocar, então faz uma suposição entre 1-9
    for suposicao in range(1, 10):
        # checa se é uma suposição válida 
        if evalido(problema, suposicao, linha, coluna):
            #se é válido, coloca a suposição no problema
            problema[linha][coluna] = suposicao
            if resolve_sodoku(problema):
                return True
        
        #se não for válido ou, a suposição não resolve o problema,
        #então precisamos fazer backtrack e tentar um novo número
        problema[linha][coluna] = -1 #reseta a suposição

    #se nenhum dos números funcionar, esse problema é impossível
    return False

if __name__=="__main__":
    #-1 = local vazio
    tabela_ex = [
        [ 3,  9,  -1,   -1,  5, -1,   -1, -1, -1],
        [-1, -1,  -1,    2, -1, -1,   -1, -1,  5],
        [-1, -1,  -1,    7,  1,  9,   -1,  8, -1],

        [-1,  5,  -1,   -1,  6,  8,   -1, -1, -1],
        [ 2, -1,   6,   -1, -1,  3,   -1, -1, -1],
        [-1, -1,  -1,   -1, -1, -1,   -1, -1,  4],

        [5,  -1,  -1,   -1, -1, -1,   -1, -1, -1],
        [6,   7,  -1,    1, -1,  5,   -1,  4, -1],
        [1,  -1,   9,   -1, -1, -1,    2, -1, -1]
    ]
    print(resolve_sodoku(tabela_ex))
    print(tabela_ex)