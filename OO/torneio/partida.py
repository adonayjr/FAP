class Partida:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.resultado = (None, None)  # (vencedor, perdedor)

    def registra_resultado(self, vencedor, perdedor):
        self.resultado = (vencedor, perdedor)
