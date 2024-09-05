class Jogador:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.pontuacao = 0
        self.rounds_vencidos = 0  # Para o jogo de luta
        self.tempo = float('inf')  # Para o jogo de corrida

    def atualiza_pontuacao(self, pontos):
        self.pontuacao += pontos
