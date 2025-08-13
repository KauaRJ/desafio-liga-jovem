# Hi there! This is the Ren'Py tutorial game. It's actually a fairly bad
# example of Ren'Py programming style - the examples we present in the game
# itself are good, but to make them easy to present we wind up doing
# some non-standard high-level things.
#
# So feel free to poke around, but if you're really looking for an example
# of good Ren'Py programming style, consider checking out The Question
# instead.

# Declare the characters.
define console = Character(_('Console'), color="#c8ffc8")

init python:
    # Classe do Jogador
    class Jogador:
        def __init__(self, nome):
            self.nome = nome
            self.vida = 100
            self.vida_maxima = 100
            self.inteligencia = 10
            self.pontuacao_pratica = 0  # Variável para a pontuação acumulada
            self.habilidades = ["Condicional", "Laço", "Vetor"]

    # Classe do Inimigo (ou Desafio)
    class Desafio:
        def __init__(self, nome, vida, dificuldade, pontos):
            self.nome = nome
            self.vida = vida
            self.dificuldade = dificuldade
            self.pontos = pontos
            self.ataque_base = 15

    # Cria uma instância do jogador
    store.Jogador = Jogador("Heroi")

# Exemplo de como iniciar a tela de combate
label start_combat:
    call screen combat_screen
    $ result = _return
    
    if result == "attack":
        "Lógica de ataque será implementada aqui"
    elif result == "inventory":
        "Lógica de inventário será implementada aqui"
    elif result == "defend":
        "Lógica de defesa será implementada aqui"
    elif result == "run":
        "Lógica de fuga será implementada aqui"
    
    return

# The game starts here.
#begin start
label start:
    scene black with fade
    call start_combat
    return
#end start

label modo_DungeonCrawler:
    "Bem-vindo ao Modo Prática! Aqui você pode treinar conceitos específicos."

    # Adicione a lógica para os desafios de prática aqui.
    # Por exemplo, um menu que permite escolher qual tópico praticar.
    
    menu:
        "Praticar If/Else":
            jump desafio_if_else_pratica
        "Praticar Loops":
            jump desafio_loops_pratica
        "Voltar ao Menu Principal":
            return

    