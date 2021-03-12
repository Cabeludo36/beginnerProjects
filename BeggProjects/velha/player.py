import math
import random
class Player:
    # letra x ou o
    def __init__(self, letra):
        self.letra = letra
    # da todos os movimentos do jogador para o jogo
    def paga_jogo(self, jogo):
        pass

class randomComputerPlayer(Player):
    def __init__(self, letra):
        super().__init__(letra)

    def pega_jogo(self, jogo):
        livre = random.choice(jogo.movimentos_disponiveis())
        return livre

class humanoplayer(Player):
    def __init__(self, letra):
        super().__init__(letra)

    def pega_jogo(self, jogo):
        lugar_valido = False
        val = None
        while not lugar_valido:
            livre = input(self.letra + "\'seu turno. Coloque um movimento de 0-8: ")
            #checa se o valor é valido
            try:
                val = int(livre)
                if val not in jogo.movimentos_disponiveis():
                    raise ValueError
                lugar_valido = True
            except ValueError:
                print ("Lugar inválido. Tente novamente")
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letra):
        super().__init__(letra)
    
    def pega_jogo(self, jogo):
        if len(jogo.movimentos_disponiveis()) == 9:
            livre = random.choice(jogo.movimentos_disponiveis()) #escolhe uma opcao randomica se todos os espaços estiverem livres
        else:
            # pega o lugar baseado no algoritmo minimax
            livre = self.minimax(jogo, self.letra) ['posicao']
        return livre

    def minimax(self, estado, player):
        max_player = self.letra #maquina
        outro_player = 'O' if player == 'X' else 'X' #outro jogador

        #checa quem esta ganhando por enquanto
        #caso base
        if estado.enquanto_vencedor == outro_player:
            #retorna a posição e pontos, porque precisamos seguir os pontos
            #para o minimax funcionar
            return {"posicao" : None,
                    "pontos" : 1 * (estado.num_lugares_disponiveis() + 1) if outro_player == max_player else -1 * (
                        estado.num_lugares_disponiveis() + 1)
                    }
        elif not estado.lugares_disponiveis(): #sem posições disponíveis
            return {'posicao': None, 'pontos': 0}
        
        #inicia um dicionário
        if player == max_player:
            best = {'posicao': None, 'pontos': -math.inf} #cada ponto deve maximizar (ser maior)
        else:
            best = {'posicao': None, 'pontos': math.inf} #cada ponto deve minimizar
        
        for movimentos in estado.movimentos_disponiveis():
            #1- fazer o movimento
            estado.faz_movimento(movimentos, player)
            #2- faz minimax simular um jogo depois daquele movimento
            sim_score = self.minimax(estado, outro_player)# agora nós alteramos o jogador 
            
            #3- desfaz o movimento
            estado.tela[movimentos] = ' '
            estado.enquanto_vencedor = None
            sim_score['posicao'] = movimentos #se não isso iria ficar ruim na parte de simular

            #4-update o dicionario se necessário
            if player == max_player:
                if sim_score['pontos'] > best['pontos']:
                    best = sim_score #troca best
            else:
                if sim_score['pontos'] < best['pontos']:
                    best = sim_score

        return best