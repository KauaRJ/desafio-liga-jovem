# inicializando personagem
# pyright: reportUndefinedVariable=false

init python:

    class Personagem:
        def __init__(self, nome, vida, ataque, defesa, itens=[]):
            self.nome = nome
            self.vida = vida
            self.ataque = ataque
            self.defesa = defesa
            self.itens = itens

        def atacar(self, alvo):
            dano = max(0, self.ataque - alvo.defesa)
            renpy.say(None, f"{self.nome} ataca {alvo.nome} causando {dano} de dano!")
            alvo.defender(dano)

        def defender(self, dano):
            self.vida -= dano
            renpy.say(None, f"{self.nome} sofreu {dano} de dano, HP restante: {self.vida}")