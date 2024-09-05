from jogador import Jogador
from partida import Partida
from tipodejogo import TipoDeJogo

class Torneio:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []
        self.partidas = []

    def adiciona_jogador(self, jogador):
        self.jogadores.append(jogador)

    def gera_ranking(self):
        ranking = sorted(self.jogadores, key=lambda j: j.pontuacao, reverse=True)
        return ranking

    def exibe_ranking(self):
        ranking = self.gera_ranking()
        for i, jogador in enumerate(ranking):
            print(f"{i+1}. {jogador.nome} - Pontuação: {jogador.pontuacao}")

    def calcula_pontuacao(self, tipo_jogo: TipoDeJogo):
        for partida in self.partidas:
            vencedor, perdedor = partida.resultado
            if vencedor and perdedor:
                vencedor, perdedor = tipo_jogo.determina_vencedor(vencedor, perdedor)
                if vencedor:
                    vencedor.atualiza_pontuacao(tipo_jogo.pontos_vencedor)
                if perdedor:
                    perdedor.atualiza_pontuacao(tipo_jogo.pontos_perdedor)

    def gerar_historico_de_partidas(self):
        for partida in self.partidas:
            resultado = partida.resultado[0].nome if partida.resultado[0] else "Empate"
            print(f"Partida: {partida.jogador1.nome} vs {partida.jogador2.nome} - Resultado: {resultado} venceu")
