from tipodejogo import TipoDeJogo
from jogador import Jogador

class Corrida(TipoDeJogo):
    def __init__(self):
        super().__init__(pontos_vencedor=15, pontos_perdedor=0)  # Exemplo de pontuação

    def determina_vencedor(self, jogador1: Jogador, jogador2: Jogador):
        if jogador1.tempo < jogador2.tempo:
            return jogador1, jogador2
        elif jogador1.tempo > jogador2.tempo:
            return jogador2, jogador1
        else:
            return None, None  # Empate
