# Hi there! This is the Ren'Py tutorial game. It's actually a fairly bad
# example of Ren'Py programming style - the examples we present in the game
# itself are good, but to make them easy to present we wind up doing
# some non-standard high-level things.
#
# So feel free to poke around, but if you're really looking for an example
# of good Ren'Py programming style, consider checking out The Question
# instead.

# Declare the characters.
define e = Character(_('Eileen'), color="#c8ffc8")

init python:
    
    import random # Importar para usar random.choice e random.shuffle
    
    # A list of section and tutorial objects.
    tutorials = [ ]

    class Section(object):
        """
        Represents a section of the tutorial menu.

        `title`
        The title of the section. This should be a translatable string.
        """

        def __init__(self, title):
            self.kind = "section"
            self.title = title

            tutorials.append(self)


    class Tutorial(object):
        """
        Represents a label that we can jump to.
        """

        def __init__(self, label, title, move=True):
            self.kind = "tutorial"
            self.label = label
            self.title = title

            if move and (move != "after"):
                self.move_before = True
            else:
                self.move_before = False

            if move and (move != "before"):
                self.move_after = True
            else:
                self.move_after = False

            tutorials.append(self)

    # Classe do Jogador
    class Jogador:
        def __init__(self, nome):
            self.nome = nome
            self.vida = 100
            self.vida_maxima = 100 # Para barras de vida e recuperação
            self.inteligencia = 10  # Pode influenciar o dano em combate
            self.pontuacao_pratica = 0  # Pontuação acumulada no modo de prática
            self.habilidades = ["Condicional", "Laço", "Vetor", "String", "Matriz", "Função"] # Habilidades baseadas nos tópicos

    # Classe do Inimigo (ou Desafio)
    class Desafio:
        def __init__(self, nome, vida, tipo_desafio, pontos, problema, codigo, opcoes, resposta_correta, nivel_dificuldade):
            self.nome = nome                                                      # Nome do "inimigo" (ex: "Bug de Sintaxe", "Erro de Laço Infinito")
            self.vida = vida                                                      # "Vida" do desafio, que diminui com acertos
            self.tipo_desafio = tipo_desafio                                      # Tópico de lógica (ex: "If/Else", "Loop", "Vetor")
            self.pontos = pontos                                                  # Pontos ganhos ao vencer o desafio
            self.ataque_base = 15                                                  # Dano que o desafio causa ao jogador se ele errar ou passar a vez
            self.problema = problema                                              # Enunciado do problema em texto (ex: "Qual a saída do código?")
            self.codigo = codigo                                                  # Trecho de código a ser exibido (lista de strings, uma linha por item)
            self.opcoes = opcoes                                                  # Lista de strings com as opções de múltipla escolha
            self.resposta_correta = resposta_correta                              # A string exata que corresponde à resposta correta
            self.nivel_dificuldade = nivel_dificuldade                            # Ex: "FAC_Basico", "FAC_Avancado", "FPR_Basico"

    # Cria uma instância do jogador
    store.Jogador = Jogador("Heroi")

    # Dicionário de desafios, agrupados por nível de dificuldade/tópico.
    # Esta é a lista MESTRA de todos os desafios disponíveis.
    store.desafio_por_dificuldade= {
        "FAC_Basico": [
            # --- FAC - Lista de Exercícios II - QUESTÃO 01: IMC ---
            Desafio(
                nome="Calculadora de IMC",
                vida=50,
                tipo_desafio="If/Else",
                pontos=100,
                problema="Um algoritmo calcula o IMC e classifica a pessoa. Qual a condição CORRETA para 'Peso ideal'?",
                codigo=[
                    "float peso, altura, imc;",
                    "// ... código para ler peso e altura ...",
                    "imc = peso / (altura * altura);",
                    "if (imc < 18.5) { printf('Abaixo do peso'); }",
                    "else if (__________) { printf('Peso ideal'); }", # Linha a completar
                    "else if (imc < 30.0) { printf('Sobrepeso'); }"
                ],
                opcoes=[
                    "A. imc >= 18.5 && imc <= 25.0",
                    "B. imc >= 18.5 && imc < 25.0",
                    "C. imc > 18.5 && imc < 25.0",
                    "D. imc >= 18.5 || imc < 25.0"
                ],
                resposta_correta="B. imc >= 18.5 && imc < 25.0",
                nivel_dificuldade="FAC_Basico"
            ),
            # --- FAC - Lista de Exercícios I - QUESTÃO 02: Classificação Nadador ---
            Desafio(
                nome="Classificador de Nadador",
                vida=55,
                tipo_desafio="If/Else Aninhado",
                pontos=110,
                problema="Um algoritmo classifica nadadores por idade. Para um nadador de 15 anos, qual categoria será exibida?",
                codigo=[
                    "int idade = 15;",
                    "if (idade >= 0 && idade <= 4) { printf('infantil A'); }",
                    "else if (idade >= 5 && idade <= 7) { printf('infantil B'); }",
                    "else if (idade >= 8 && idade <= 10) { printf('infantil C'); }",
                    "else if (idade >= 11 && idade <= 13) { printf('juvenil A'); }",
                    "else if (idade >= 14 && idade <= 17) { printf('juvenil B'); }",
                    "else { printf('Adulto'); }"
                ],
                opcoes=[
                    "A. infantil C",
                    "B. juvenil A",
                    "C. juvenil B",
                    "D. Adulto"
                ],
                resposta_correta="C. juvenil B",
                nivel_dificuldade="FAC_Basico"
            ),
            # --- FAC - Lista de Exercícios I - QUESTÃO 03: Peso Ideal ---
            Desafio(
                nome="Calculadora de Peso Ideal",
                vida=60,
                tipo_desafio="Condicionais e Fórmulas",
                pontos=120,
                problema="Um algoritmo calcula o peso ideal. Qual a fórmula para o gênero feminino?",
                codigo=[
                    "float h = 1.70; // altura",
                    "char genero = 'F';",
                    "float peso_ideal;",
                    "if (genero == 'M') {",
                    "   peso_ideal = (72.7 * h) - 58;",
                    "} else if (genero == 'F') {",
                    "   peso_ideal = __________;", # Linha a completar
                    "}"
                ],
                opcoes=[
                    "A. (62.1 * h) - 44.7",
                    "B. (72.7 * h) - 58",
                    "C. (62.1 * h) + 44.7",
                    "D. (72.7 * h) + 58"
                ],
                resposta_correta="A. (62.1 * h) - 44.7",
                nivel_dificuldade="FAC_Basico"
            ),
            # Adicione mais desafios FAC_Basico aqui...
        ],
        "FAC_Intermediario": [
            Desafio(
                nome="Erro de Laço Infinito",
                vida=75,
                tipo_desafio="Loop",
                pontos=150,
                problema="O loop abaixo está errado. O que causa o loop infinito?",
                codigo=["for (int i = 0; i < 10; i--) {"],
                opcoes=["A condição 'i < 10'", "O decremento 'i--'", "A inicialização 'i = 0'"],
                resposta_correta="O decremento 'i--'",
                nivel_dificuldade="FAC_Intermediario"
            ),
            Desafio(
                nome="Vetor Desordenado",
                vida=90,
                tipo_desafio="Vetor",
                pontos=200,
                problema="Corrija o código para ordenar os elementos de um vetor.",
                codigo=["int arr[] = {5, 2, 8, 1};", "for (int i = 0; i < 4; i++) {", "   // Código de ordenação faltando", "}"],
                opcoes=["Usar Bubble Sort", "Usar Selection Sort", "Usar Insertion Sort"],
                resposta_correta="Usar Bubble Sort", # Exemplo
                nivel_dificuldade="FAC_Intermediario"
            ),
            # Adicione mais desafios FAC_Intermediario aqui
        ],
        "FPR_Basico": [
            Desafio(
                nome="Cardápio da Lanchonete",
                vida=90,
                tipo_desafio="Estruturas de Decisão",
                pontos=180,
                problema="Você comprou um 'Cachorro quente'. Qual o código correspondente?",
                codigo=["// Código da lanchonete aqui"],
                opcoes=["100", "101", "102"],
                resposta_correta="100",
                nivel_dificuldade="FPR_Basico"
            ),
            # Adicione mais desafios FPR_Basico aqui
        ],
        # Adicione outros níveis de dificuldade como "FPR_Avancado", "FAC_Avancado" etc.
    }
    




    Section(_("Quickstart"))

    Tutorial("tutorial_playing", _("Player Experience"))
    Tutorial("tutorial_create", _("Creating a New Game"))
    Tutorial("tutorial_dialogue", _("Writing Dialogue"))
    Tutorial("tutorial_images", _("Adding Images"))
    Tutorial("tutorial_simple_positions", _("Positioning Images"))
    Tutorial("tutorial_transitions", _("Transitions"))
    Tutorial("tutorial_music", _("Music and Sound Effects"))
    Tutorial("tutorial_menus", _("Choices and Python"))
    Tutorial("tutorial_input", _("Input and Interpolation"))
    Tutorial("tutorial_video", _("Video Playback"))
    Tutorial("tutorial_nvlmode", _("NVL Mode"), move=None)
    Tutorial("director", _("Tools and the Interactive Director"))
    Tutorial("distribute", _("Building Distributions"))

    Section(_("In Depth"))

    Tutorial("text", _("Text Tags, Escapes, and Interpolation"))
    Tutorial("demo_character", _("Character Objects"))
    Tutorial("simple_displayables", _("Simple Displayables"), move=None)
    Tutorial("demo_transitions", _("Transition Gallery"))

    # Positions and Transforms?
    Tutorial("tutorial_positions", _("Position Properties"))

    # Advanced Transforms?
    Tutorial("tutorial_atl", _("Transforms and Animation"))
    Tutorial("transform_properties", _("Transform Properties"))

    Tutorial("new_gui", _("GUI Customization"))
    Tutorial("styles", _("Styles and Style Properties"), move=None)
    Tutorial("tutorial_screens", _("Screen Basics"), move=None)
    Tutorial("screen_displayables", _("Screen Displayables"), move=None)

    Tutorial("demo_minigame", _("Minigames and CDDs"))
    Tutorial("translations", _("Translations"))

screen tutorials(adj):

    frame:
        xsize 640
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True
            draggable True

            vbox:
                for i in tutorials:

                    if i.kind == "tutorial":

                        textbutton i.title:
                            action Return(i)
                            left_padding 20
                            xfill True

                    else:

                        null height 10
                        text i.title alt ""
                        null height 5

        bar adjustment adj style "vscrollbar"

        textbutton _("That's enough for now."):
            xfill True
            action Return(False)
            top_margin 10


# This is used to preserve the state of the scrollbar on the selection
# screen.
default tutorials_adjustment = ui.adjustment()

# True if this is the first time through the tutorials.
default tutorials_first_time = True

# The game starts here.
#begin start
label start:

#end start

    scene bg washington
    show eileen vhappy
    with dissolve

    # Start the background music playing.
    play music "sunflower-slow-drag.ogg"

    window show

    e "Hi! My name is Eileen, and I'd like to welcome you to the Ren'Py tutorial."

    show eileen happy

    e "In this tutorial, we'll teach you the basics of Ren'Py, so you can make games of your own. We'll also demonstrate many features, so you can see what Ren'Py is capable of."

label tutorials:

    show eileen happy at left
    with move

    if tutorials_first_time:
        $ e(_("What would you like to see?"), interact=False)
    else:
        $ e(_("Is there anything else you'd like to see?"), interact=False)

    $ tutorials_first_time = False
    $ renpy.choice_for_skipping()

    call screen tutorials(adj=tutorials_adjustment)

    $ tutorial = _return

    if not tutorial:
        jump end

    if tutorial.move_before:
        show eileen happy at center
        with move

    $ reset_example()

    call expression tutorial.label from _call_expression

    if tutorial.move_after:
        hide example
        show eileen happy at left
        with move

    jump tutorials

label end:

    show eileen happy at center
    with move

    show _finale behind eileen


    e "Thank you for viewing this tutorial."

    e "If you'd like to see a full Ren'Py game, select \"The Question\" in the launcher."

    e "You can download new versions of Ren'Py from {a=https://www.renpy.org/}https://www.renpy.org/{/a}. For help and discussion, check out the {a=https://lemmasoft.renai.us/forums/}Lemma Soft Forums{/a}."

    e "We'd like to thank Piroshki for contributing my sprites; Mugenjohncel for Lucy, the band, and drawn backgrounds; and Jake for the magic circle."

    e "The background music is \"Sunflower Slow Drag\", by Scott Joplin and Scott Hayden, performed by the United States Marine Band. The concert music is by Alessio."

    show eileen vhappy

    e "We look forward to seeing what you create with Ren'Py. Have fun!"

    window hide

    # Returning from the top level quits the game.
    return

label modo_pratica:
    "Bem-vindo à Masmorra da Lógica! Escolha o que praticar."
    $ renpy.hide_dialogue()
    $ store.jogador = Jogador("Programador") # Reinicia o jogador para cada sessão de prática
    $ store.jogador.vida = store.jogador.vida_maxima

    # Loop principal para permitir que o jogador escolha tópicos repetidamente
    while True:
        "Sua pontuação atual no Modo Prática: [store.jogador.pontuacao_pratica]"
        "Escolha o Nível de Dificuldade/Tópico para praticar:"
        
        # CHAMA A TELA PERSONALIZADA para a escolha de nível
        $ escolha_nivel = renpy.call_screen("escolha_nivel_pratica_screen")

        if escolha_nivel == "sair":
            return # Sai do modo de prática e volta para o menu principal

        "Você entrou na área de desafios de [escolha_nivel]!"
        
        # Cria uma cópia da lista de desafios para o nível escolhido e a embaralha
        $ desafios_para_esta_sessao = list(store.desafio_por_dificuldade[escolha_nivel])
        $ random.shuffle(desafios_para_esta_sessao)

        # Loop para enfrentar os desafios dentro do nível de dificuldade escolhido
        while desafios_para_esta_sessao and store.jogador.vida > 0:
            $ desafio_atual = desafios_para_esta_sessao.pop(0) # Pega o próximo desafio e o remove
            call batalha_de_turnos(desafio_atual) # Chama a rotina de batalha

            if store.jogador.vida <= 0:
                jump fim_de_jogo_pratica # Se o jogador morrer, o jogo acaba
        
        # Após completar todos os desafios de um nível ou morrer
        if store.jogador.vida > 0:
            "Você superou todos os desafios de [escolha_nivel]!"
            "Sua pontuação atual: [store.jogador.pontuacao_pratica]"
            "O que você gostaria de fazer agora?"
        else:
            jump fim_de_jogo_pratica # Garante que o jogo termina se a vida chegar a zero

screen escolha_nivel_pratica_screen():
    frame:
        xalign 0.5
        yalign 0.5
        background "#2a2a2a"
        padding 20

        vbox:
            spacing 15

            text "Escolha um Nível de Dificuldade para Praticar:"

            for nivel in store.desafio_por_dificuldade.keys():
                textbutton nivel:
                    action Return(nivel)
            
            textbutton "Sair do Modo Prática":
                action Return("sair")