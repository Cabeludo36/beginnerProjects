grafos:dict = { # dicionario com os grafos
    "A": ["B","C"],
    "B": ["D","E"],
    "C": ["E","G"],
    "D": [],
    "E": ["F"],
    "G": [],
    "F": ["<3"],
    "<3": []
}

fila:list = [] # fila para a busca em largura
visitados:list = [] # lista de visitados

def procuraLargura(visitados:list, grafos:dict, inicio:str, procura:str = None):
    """Função para busca em largura
    Args:
        visitados (list): lista de visitados
        grafos (dict): dicionario com os grafos
        inicio (str): elemento inicial
        procura (str, optional): elemento procurado. Defaults to None.
    """
    # caso o valor procurado seja o inicio
    if inicio == procura:
        return True

    visitados.append(inicio) # adiciona o inicio na lista de visitados
    fila.append(inicio)  # adiciona o inicio na fila para que aja a busca apartir dele

    while fila: # loop que verifica se a fila possui elementos
        atual = fila.pop(0) # remove o primeiro elemento da fila (elemento atual)
        
        for vizinho in grafos[atual]: # percorre os vizinhos do elemento atual (lista do dicionario)
            if vizinho == procura: # verifica se o vizinho é o valor procurado
                return True
            if (vizinho not in visitados): # verifica se o vizinho já foi visitado
                visitados.append(vizinho) # adiciona o vizinho na lista de visitados
                fila.append(vizinho) # adiciona o vizinho na fila
    if procura != None: # caso aja um valor procurado e não seja encontrado
        return False


# Função para imprimir o resultado da busca
def resultadoProcura(procura:str):
    print("\nAchei " + procura + "!, na " + str(len(visitados)+1) + "ª posição 😁")

# função para verificar se o elemento está na fila
def procuraLarguraPrints(visitados:list, grafos:dict, inicio:str, procura:str = None):
    # caso o valor procurado seja o inicio
    if inicio == procura:
        resultadoProcura(procura)
        return

    visitados.append(inicio)
    fila.append(inicio)

    while fila:
        atual = fila.pop(0)
        print(atual, end = ": ")
        print("[", end = "")

        for vizinho in grafos[atual]:
            print(vizinho, end = ", ")
            if vizinho == procura:
                print("]", end = "")
                resultadoProcura(procura)
                return
            if (vizinho not in visitados):
                visitados.append(vizinho)
                fila.append(vizinho)
        print("]", end = ", ")
    if procura != None:
        print("\nNão achei " + procura + " na busca em largura 😢")

if __name__ == "__main__":
    procura = "isso"
    procuraLarguraPrints(visitados, grafos, "A", "isso")
    if procuraLargura(visitados, grafos, "A", procura) and procura != None:
        resultadoProcura(procura)
    elif procura != None:
        print("\nNão achei "+procura+" na busca em largura 😢")