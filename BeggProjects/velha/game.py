from player import humanoplayer, randomComputerPlayer, GeniusComputerPlayer
import time

class velha:
    def __init__(self):
        self.tela = [' ' for _ in range(9)] #lista que representa uma tabela 3x3
        self.enquanto_vencedor = None #rastreia o jogador que estiver ganhando

    def print_tela(self):
        for linha in [self.tela[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(linha) + ' |')
    
    @staticmethod
    def print_tela_num():
        # 0 | 1 | 2 (nos fala o numero que corresponde a posição)
        num_tela=[[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for linha in num_tela:
            print('| ' + ' | '.join(linha) + ' |')

    def movimentos_disponiveis(self):
        movimentos = []
        for (i, local) in enumerate(self.tela):
            #['x], 'x', 'x'] --> [(0,'x'), (1, 'x'), (2, 'o')]
            if local == ' ':
                movimentos.append(i)
        return movimentos
    
    def lugares_disponiveis(self):
        return ' ' in self.tela
    
    def num_lugares_disponiveis(self):
        return self.tela.count(' ')

    def faz_movimento(self, local, letra):
        #se for um movimento valido, faz a jogada
        #e retorna True. Se invalido, retorna False
        if self.tela[local] == ' ':
            self.tela[local] = letra
            if self.vencedor(local, letra):
                self.enquanto_vencedor = letra
            return True
        return False
    
    def vencedor(self, local, letra):
        #ganhador precisa ter a letra em 3 lugares seguidos
        #checa linha
        lin_ind = local // 3
        linha = self.tela[lin_ind*3 : (lin_ind + 1) * 3]
        if all(cada_lugar == letra for cada_lugar in linha):
            return True
        
        #checa coluna
        col_ind = local % 3
        coluna = [self.tela[col_ind+i*3] for i in range(3)]
        if all(cada_lugar == letra for cada_lugar in coluna):
            return True
        
        #checa diagonal
        #somente se o local for um dos numeros pares (0, 2, 4, 6, 8)
        #que são os unicos movimentos possíveis de ganhar na diagonal
        if local % 2 == 0:
            diagonal1 = [self.tela[i] for i in [0, 4, 8]] #esquerda para a direita
            if all(cada_lugar == letra for cada_lugar in diagonal1):
                return True
            diagonal2 = [self.tela[i] for i in [2, 4, 6]] #direita para a esquerda
            if all(cada_lugar == letra for cada_lugar in diagonal2):
                return True
        
        #se todos falharem
        return False

def jogar(jogo, x_jogador, o_jogador, print_jogo=True):
    #retorna o vencedor do jogo (a letra) ou None se for um empate
    if print_jogo:
        jogo.print_tela_num()
    
    letra='X' #primeira letra
    #rodar enquanto ouver lugares disponíveis
    while jogo.lugares_disponiveis():
        #pega a jogada do jogador certo
        if letra == 'O':
            local = o_jogador.pega_jogo(jogo)
        else:
            local = x_jogador.pega_jogo(jogo)
        #função que faz o movimento
        if jogo.faz_movimento(local, letra):
            if print_jogo:
                print(letra + f" faz o movimento para {local}")
                jogo.print_tela()
                print('') #linha vazia
            
                if jogo.enquanto_vencedor:
                    if print_jogo:
                        print(letra + " GANHOU!!!")
                        input()
                    return letra
            #altera a letra depois da jogada
            #muda o jogador
            if letra =='X':
                letra = 'O'
            else:
                letra = 'X'

    #pequena pausa
    time.sleep(0.8)
    if print_jogo:
        print("Empate")

if __name__ == '__main__':
    x_jogador = humanoplayer('X')
    o_jogador = GeniusComputerPlayer('O')
    t = velha()
    jogar(t, x_jogador, o_jogador, print_jogo=True)