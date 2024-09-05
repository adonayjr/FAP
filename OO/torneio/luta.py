from tipodejogo import TipoDeJogo
from jogador import Jogador

class Luta(TipoDeJogo):
    def __init__(self):
        super().__init__(pontos_vencedor=10, pontos_perdedor=0)  # Exemplo de pontuação

    def determina_vencedor(self, jogador1: Jogador, jogador2: Jogador):
        if jogador1.rounds_vencidos > jogador2.rounds_vencidos:
            return jogador1, jogador2
        elif jogador1.rounds_vencidos < jogador2.rounds_vencidos:
            return jogador2, jogador1
        else:
            return None, None  # Empate
