# inicializando jogo
# pyright: reportUndefinedVariable=false
define e = Character("Eileen")

label start:

    scene black
    "Teste de combate agora!"

    # ▶️ Chamando diretamente o combate
    call combate_turno

    "Fim do teste. Você voltou ao menu principal."

    return