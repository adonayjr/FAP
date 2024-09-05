from abc import ABC, abstractmethod

class TipoDeJogo(ABC):
    def __init__(self, pontos_vencedor, pontos_perdedor):
        self.pontos_vencedor = pontos_vencedor
        self.pontos_perdedor = pontos_perdedor

    @abstractmethod
    def determina_vencedor(self, jogador1, jogador2):
        pass
