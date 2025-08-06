# inicializando combate
# pyright: reportUndefinedVariable=false

init python:

    class Personagem:
        def __init__(self, nome, vida, ataque, defesa):
            self.nome = nome
            self.vida = vida
            self.ataque = ataque
            self.defesa = defesa

        def atacar(self, alvo):
            dano = max(0, self.ataque - alvo.defesa)
            renpy.say(None, f"{self.nome} ataca {alvo.nome} causando {dano} de dano!")
            alvo.defender(dano)

        def defender(self, dano):
            self.vida -= dano
            renpy.say(None, f"{self.nome} sofreu {dano} de dano! HP restante: {self.vida}")

label combate_turno:

    python:
        jogador = Personagem("Estudante", 100, 20, 5)
        inimigo = Personagem("Bug Assustador", 80, 15, 3)

    "Um combate começou contra [inimigo.nome]!"

    while jogador.vida > 0 and inimigo.vida > 0:

        "Turno do jogador."

        menu:
            "Atacar":
                $ jogador.atacar(inimigo)
            "Defender":
                $ renpy.say(None, f"{jogador.nome} se defende.")
                $ jogador.defesa += 5
            "Fugir":
                "Você fugiu do combate!"
                return

        if inimigo.vida <= 0:
            "Você venceu!"
            return

        "Turno do inimigo."
        $ inimigo.atacar(jogador)

        if jogador.vida <= 0:
            "Você foi derrotado..."
            return

        $ jogador.defesa = 5

    return