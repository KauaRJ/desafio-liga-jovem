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
            self.nome = nome                                                 # Nome do "inimigo" (ex: "Bug de Sintaxe", "Erro de Laço Infinito")
            self.vida = vida                                                 # "Vida" do desafio, que diminui com acertos
            self.tipo_desafio = tipo_desafio                                 # Tópico de lógica (ex: "If/Else", "Loop", "Vetor")
            self.pontos = pontos                                             # Pontos ganhos ao vencer o desafio
            self.ataque_base = 15                                            # Dano que o desafio causa ao jogador se ele errar ou passar a vez
            self.problema = problema                                         # Enunciado do problema em texto (ex: "Qual a saída do código?")
            self.codigo = codigo                                             # Trecho de código a ser exibido (lista de strings, uma linha por item)
            self.opcoes = opcoes                                             # Lista de strings com as opções de múltipla escolha
            self.resposta_correta = resposta_correta                         # A string exata que corresponde à resposta correta
            self.nivel_dificuldade = nivel_dificuldade                       # Ex: "FAC_Basico", "FAC_Avancado", "FPR_Basico"

    # Cria uma instância do jogador
    store.Jogador = Jogador("Heroi")

    # Dicionário de desafios, agrupados por nível de dificuldade/tópico.
    # Esta é a lista MESTRA de todos os desafios disponíveis.
    store.desafio_por_dificuldade= {
        "FAC_Basico": [
            Desafio(
                nome="Calculadora de IMC",
                vida=50,
                tipo_desafio="If/Else",
                pontos=100,
                problema="Segundo o código a seguir, em que condições o IMC está ideal?",
                codigo=["float imc = peso / (altura * altura);", 
                        ],
                opcoes=["Abaixo do peso", "Peso ideal", "Sobrepeso"],
                resposta_correta="Peso ideal",
                nivel_dificuldade="FAC_Basico"
            ),
            Desafio(
                nome="Completando a Condição",
                vida=50,
                tipo_desafio="If/Else",
                pontos=100,
                problema="Complete a linha em branco para que o código imprima 'Aprovado' se a nota for maior ou igual a 7.",
                codigo=["int nota = 8;", "if (__________) {", "  printf('Aprovado');", "}"],
                opcoes=["A. nota > 7", "B. nota >= 7", "C. nota == 7"],
                resposta_correta="B. nota >= 7",
                nivel_dificuldade="FAC_Basico"
            ),
            # Adicione mais desafios FAC_Basico aqui
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
                codigo=["int arr[] = {5, 2, 8, 1};", "for (int i = 0; i < 4; i++) {", "  // Código de ordenação faltando", "}"],
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

