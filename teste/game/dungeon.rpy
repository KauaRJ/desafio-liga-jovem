# inicializando dungeon
# pyright: reportUndefinedVariable=false

init python:
    pos_x = 0
    pos_y = 0

label explorar_dungeon:

    "Você está na posição: [pos_x], [pos_y]."

    menu:
        "Cima":
            $ pos_y -= 1
        "Baixo":
            $ pos_y += 1
        "Esquerda":
            $ pos_x -= 1
        "Direita":
            $ pos_x += 1
        "Parar de explorar":
            "Você decide sair da dungeon por agora."
            return

    jump explorar_dungeon