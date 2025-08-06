# inicializando inimigos
# pyright: reportUndefinedVariable=false

label menuCombate:

    menu:
        "Atacar":
            $ jogador.atacar(inimigo)
        "Defender":
            $ jogador.defender(0)
        "Usar item":
            $ renpy.say(None, "Você ainda não tem itens.")
        "Fugir":
            "Você fugiu do combate!"
            return

    # Após a ação, volta para o menu
    jump menuCombate
