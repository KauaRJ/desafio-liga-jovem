################################################################################
## Inicialização
################################################################################

## A instrução init offset faz com que as instruções de inicialização nesse
## arquivo sejam executadas antes das instruções init em qualquer outro arquivo.
init offset = -2

## Chamar gui.init redefine os estilos para os valores padrão sensatos e define
## a largura e a altura do jogo.
init python:
    gui.init(1920, 1080)

## Habilitar verificações de propriedades inválidas ou instáveis em telas ou
## transformações
define config.check_conflicting_properties = True


################################################################################
## Variáveis de configuração da GUI
################################################################################


## Cores #######################################################################
##
## As cores do texto na interface.

## Uma cor de destaque usada em toda a interface para rotular e destacar o
## texto.
define gui.accent_color = '#0099cc'

## A cor usada para um botão de texto quando ele não está selecionado nem passa
## o mouse.
define gui.idle_color = '#888888'

## A cor pequena é usada para texto pequeno, que precisa ser mais claro/escuro
## para obter o mesmo efeito.
define gui.idle_small_color = '#aaaaaa'

## A cor que é usada para botões e barras que passam pelo mouse.
define gui.hover_color = '#66c1e0'

## A cor usada em um botão de texto quando ele está selecionado, mas não
## focalizado. Um botão estará selecionado se for a tela atual ou o valor de
## preferência.
define gui.selected_color = '#ffffff'

## A cor usada para um botão de texto quando ele não pode ser selecionado.
define gui.insensitive_color = '#8888887f'

## Cores usadas para as partes das barras que não estão preenchidas. Elas não
## são usadas diretamente, mas são usadas ao gerar novamente os arquivos de
## imagem de barra.
define gui.muted_color = '#003d51'
define gui.hover_muted_color = '#005b7a'

## As cores usadas para o diálogo e o texto da opção de menu.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Fontes e tamanhos de fonte ##################################################

## A fonte usada para o texto do jogo.
define gui.text_font = "DejaVuSans.ttf"

## A fonte usada para os nomes dos caracteres.
define gui.name_text_font = "DejaVuSans.ttf"

## A fonte usada para o texto fora do jogo.
define gui.interface_text_font = "DejaVuSans.ttf"

## O tamanho do texto normal do diálogo.
define gui.text_size = 33

## O tamanho dos nomes dos caracteres.
define gui.name_text_size = 45

## O tamanho do texto na interface de usuário do jogo.
define gui.interface_text_size = 33

## O tamanho dos rótulos na interface de usuário do jogo.
define gui.label_text_size = 36

## O tamanho do texto na tela de notificação.
define gui.notify_text_size = 24

## O tamanho do título do jogo.
define gui.title_text_size = 75


## Menus principal e de jogos ##################################################

## As imagens usadas nos menus principal e de jogo.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Diálogo #####################################################################
##
## Essas variáveis controlam como o diálogo é exibido na tela, uma linha por
## vez.

## A altura da caixa de texto que contém o diálogo.
define gui.textbox_height = 278

## O posicionamento da caixa de texto verticalmente na tela. 0,0 é a parte
## superior, 0,5 é o centro e 1,0 é a parte inferior.
define gui.textbox_yalign = 1.0


## O posicionamento do nome do personagem que fala, em relação à caixa de texto.
## Pode ser um número inteiro de pixels a partir da esquerda ou do topo, ou 0,5
## para o centro.
define gui.name_xpos = 360
define gui.name_ypos = 0

## O alinhamento horizontal do nome do personagem. Pode ser 0,0 para alinhado à
## esquerda, 0,5 para centralizado e 1,0 para alinhado à direita.
define gui.name_xalign = 0.0

## A largura, a altura e as bordas da caixa que contém o nome do caractere ou
## Nenhum para dimensioná-la automaticamente.
define gui.namebox_width = None
define gui.namebox_height = None

## As bordas da caixa que contém o nome do personagem, na ordem esquerda,
## superior, direita e inferior.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Se for True, o plano de fundo da caixa de nome será lado a lado; se for
## False, o plano de fundo da caixa de nome será dimensionado.
define gui.namebox_tile = False


## O posicionamento do diálogo em relação à caixa de texto. Esse pode ser um
## número inteiro de pixels em relação ao lado esquerdo ou superior da caixa de
## texto, ou 0,5 em relação ao centro.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## A largura máxima do texto da caixa de diálogo, em pixels.
define gui.dialogue_width = 1116

## O alinhamento horizontal do texto da caixa de diálogo. Pode ser 0,0 para
## alinhado à esquerda, 0,5 para centralizado e 1,0 para alinhado à direita.
define gui.dialogue_text_xalign = 0.0


## Botões ######################################################################
##
## Essas variáveis, juntamente com os arquivos de imagem em gui/button,
## controlam aspectos de como os botões são exibidos.

## A largura e a altura de um botão, em pixels. Se nenhum, Ren'Py calcula um
## tamanho.
define gui.button_width = None
define gui.button_height = None

## As bordas em cada lado do botão, na ordem esquerda, superior, direita e
## inferior.
define gui.button_borders = Borders(6, 6, 6, 6)

## Se for True, a imagem de fundo será lado a lado. Se for False, a imagem de
## fundo será dimensionada linearmente.
define gui.button_tile = False

## A fonte usada pelo botão.
define gui.button_text_font = gui.interface_text_font

## O tamanho do texto usado pelo botão.
define gui.button_text_size = gui.interface_text_size

## A cor do texto do botão em vários estados.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## O alinhamento horizontal do texto do botão. (0,0 é à esquerda, 0,5 é ao
## centro, 1,0 é à direita).
define gui.button_text_xalign = 0.0


## Essas variáveis substituem as configurações de diferentes tipos de botões.
## Consulte a documentação do gui para saber os tipos de botões disponíveis e
## para que cada um é usado.
##
## Essas personalizações são usadas pela interface padrão:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Você também pode adicionar suas próprias personalizações, acrescentando
## variáveis com nomes adequados. Por exemplo, você pode descomentar a seguinte
## linha para definir a largura de um botão de navegação.

# define gui.navigation_button_width = 250


## Botões de escolha ###########################################################
##
## Os botões de escolha são usados nos menus do jogo.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## Botões de slot de arquivo ###################################################
##
## Um botão de slot de arquivo é um tipo especial de botão. Ele contém uma
## imagem em miniatura e um texto que descreve o conteúdo do slot de salvamento.
## Um slot para salvar usa arquivos de imagem em gui/button, como os outros
## tipos de botões.

## O botão salvar slot.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## A largura e a altura das miniaturas usadas pelos slots de salvamento.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## O número de colunas e linhas na grade de slots de salvamento.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Posicionamento e espaçamento ################################################
##
## Essas variáveis controlam o posicionamento e o espaçamento de vários
## elementos da interface do usuário.

## A posição do lado esquerdo dos botões de navegação, em relação ao lado
## esquerdo da tela.
define gui.navigation_xpos = 60

## A posição vertical do indicador de salto.
define gui.skip_ypos = 15

## A posição vertical da tela de notificação.
define gui.notify_ypos = 68

## O espaçamento entre as opções de menu.
define gui.choice_spacing = 33

## Botões na seção de navegação dos menus principal e de jogo.
define gui.navigation_spacing = 6

## Controla a quantidade de espaçamento entre as preferências.
define gui.pref_spacing = 15

## Controla a quantidade de espaçamento entre os botões de preferência.
define gui.pref_button_spacing = 0

## O espaçamento entre os botões de página de arquivo.
define gui.page_spacing = 0

## O espaçamento entre os slots de arquivo.
define gui.slot_spacing = 15

## A posição do texto do menu principal.
define gui.main_menu_text_xalign = 1.0


## Quadros #####################################################################
##
## Essas variáveis controlam a aparência dos quadros que podem conter
## componentes da interface do usuário quando uma sobreposição ou janela não
## está presente.

## Quadros genéricos.
define gui.frame_borders = Borders(6, 6, 6, 6)

## O quadro que é usado como parte da tela de confirmação.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## O quadro que é usado como parte da tela de salto.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## O quadro que é usado como parte da tela de notificação.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Os planos de fundo dos quadros devem ser lado a lado?
define gui.frame_tile = False


## Barras, barras de rolagem e controles deslizantes ###########################
##
## Controlam a aparência e o tamanho das barras, barras de rolagem e controles
## deslizantes.
##
## A GUI padrão usa apenas controles deslizantes e barras de rolagem verticais.
## Todas as outras barras são usadas somente em telas escritas pelo criador.

## A altura das barras horizontais, barras de rolagem e controles deslizantes. A
## largura das barras verticais, barras de rolagem e controles deslizantes.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## True (verdadeiro) se as imagens da barra devem ser lado a lado. False se elas
## devem ser escalonadas linearmente.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Bordas horizontais.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Bordas verticais.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## What to do with unscrollable scrollbars in the game menu. "hide" hides them,
## while None shows them.
define gui.unscrollable = "hide"


## Histórico ###################################################################
##
## A tela de histórico exibe o diálogo que o jogador já dispensou.

## O número de blocos de histórico de diálogo que Ren'Py manterá.
define config.history_length = 250

## A altura de uma entrada de tela de histórico ou Nenhum para tornar a altura
## variável ao custo do desempenho.
define gui.history_height = 210

## Additional space to add between history screen entries.
define gui.history_spacing = 0

## A posição, a largura e o alinhamento do rótulo que fornece o nome do
## caractere falante.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## A posição, a largura e o alinhamento do texto da caixa de diálogo.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## Modo NVL ####################################################################
##
## A tela do modo NVL exibe o diálogo falado pelos personagens do modo NVL.

## As bordas do plano de fundo da janela de plano de fundo do modo NVL.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## O número máximo de entradas do modo NVL que o Ren'Py exibirá. Quando mais
## entradas do que isso forem exibidas, a entrada mais antiga será removida.
define gui.nvl_list_length = 6

## A altura de uma entrada no modo NVL. Defina como None para que as entradas
## ajustem a altura dinamicamente.
define gui.nvl_height = 173

## O espaçamento entre as entradas do modo NVL quando gui.nvl_height é Nenhum e
## entre as entradas do modo NVL e um menu do modo NVL.
define gui.nvl_spacing = 15

## A posição, a largura e o alinhamento do rótulo que fornece o nome do
## caractere falante.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## A posição, a largura e o alinhamento do texto da caixa de diálogo.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## A posição, a largura e o alinhamento do texto nvl_thought (o texto dito pelo
## caractere nvl_narrator).
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## A posição dos botões de menu nvl.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Localização #################################################################

## Isso controla onde é permitida uma quebra de linha. O padrão é adequado para
## a maioria dos idiomas. Uma lista de valores disponíveis pode ser encontrada
## em https://www.renpy.org/doc/html/style_properties.html#style-property-
## language

define gui.language = "unicode"


################################################################################
## Dispositivos móveis
################################################################################

init python:

    ## Isso aumenta o tamanho dos botões rápidos para torná-los mais fáceis de
    ## tocar em tablets e telefones.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## Isso altera o tamanho e o espaçamento de vários elementos da GUI para
    ## garantir que eles sejam facilmente visíveis nos telefones.
    @gui.variant
    def small():

        ## Tamanhos de fonte.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Ajustar o local da caixa de texto.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Altere o tamanho e o espaçamento de vários itens.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## Layout do botão Arquivo.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## Modo NVL.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
