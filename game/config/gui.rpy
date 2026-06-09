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
## Todos os valores de pixel abaixo foram escalonados x1.5 em relação ao
## padrão gerado para 1280x720 (1920/1280 = 1080/720 = 1.5).
################################################################################


## Cores #######################################################################

define gui.accent_color = '#0066cc'
define gui.idle_color = '#888888'
define gui.idle_small_color = '#aaaaaa'
define gui.hover_color = '#66a3e0'
define gui.selected_color = '#ffffff'
define gui.insensitive_color = '#8888887f'
define gui.muted_color = '#002851'
define gui.hover_muted_color = '#003d7a'
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Fontes e tamanhos de fonte ##################################################

define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"

define gui.text_size = 33               ## era 22
define gui.name_text_size = 45          ## era 30
define gui.interface_text_size = 33     ## era 22
define gui.label_text_size = 36         ## era 24
define gui.notify_text_size = 24        ## era 16
define gui.title_text_size = 75         ## era 50


## Menus principal e de jogos ##################################################

define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Diálogo #####################################################################

define gui.textbox_height = 278         ## era 185

define gui.textbox_yalign = 1.0

define gui.name_xpos = 360              ## era 240
define gui.name_ypos = 0

define gui.name_xalign = 0.0

define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(8, 8, 8, 8)   ## era Borders(5, 5, 5, 5)
define gui.namebox_tile = False

define gui.dialogue_xpos = 402          ## era 268
define gui.dialogue_ypos = 75           ## era 50
define gui.dialogue_width = 1116        ## era 744
define gui.dialogue_text_xalign = 0.0


## Botões ######################################################################

define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(6, 6, 6, 6)    ## era Borders(4, 4, 4, 4)
define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size

define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0

define gui.radio_button_borders = Borders(27, 6, 6, 6)     ## era Borders(18, 4, 4, 4)
define gui.check_button_borders = Borders(27, 6, 6, 6)     ## era Borders(18, 4, 4, 4)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(15, 6, 15, 6)     ## era Borders(10, 4, 10, 4)
define gui.quick_button_borders = Borders(15, 6, 15, 0)    ## era Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 21                      ## era 14
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color


## Botões de escolha ###########################################################

define gui.choice_button_width = 1185                               ## era 790
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)         ## era Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## Botões de slot de arquivo ###################################################

define gui.slot_button_width = 414                                  ## era 276
define gui.slot_button_height = 309                                 ## era 206
define gui.slot_button_borders = Borders(15, 15, 15, 15)           ## era Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 21                               ## era 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

define config.thumbnail_width = 384                                 ## era 256
define config.thumbnail_height = 216                                ## era 144

define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Posicionamento e espaçamento ################################################

define gui.navigation_xpos = 60        ## era 40
define gui.skip_ypos = 15              ## era 10
define gui.notify_ypos = 68            ## era 45
define gui.choice_spacing = 33         ## era 22
define gui.navigation_spacing = 6      ## era 4
define gui.pref_spacing = 15           ## era 10
define gui.pref_button_spacing = 0
define gui.page_spacing = 0
define gui.slot_spacing = 15           ## era 10
define gui.main_menu_text_xalign = 1.0


## Quadros #####################################################################

define gui.frame_borders = Borders(6, 6, 6, 6)             ## era Borders(4, 4, 4, 4)
define gui.confirm_frame_borders = Borders(60, 60, 60, 60) ## era Borders(40, 40, 40, 40)
define gui.skip_frame_borders = Borders(24, 8, 75, 8)      ## era Borders(16, 5, 50, 5)
define gui.notify_frame_borders = Borders(24, 8, 60, 8)    ## era Borders(16, 5, 40, 5)
define gui.frame_tile = False


## Barras, barras de rolagem e controles deslizantes ###########################

define gui.bar_size = 38               ## era 25
define gui.scrollbar_size = 18         ## era 12
define gui.slider_size = 38            ## era 25

define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

define gui.bar_borders = Borders(6, 6, 6, 6)           ## era Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)     ## era Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(6, 6, 6, 6)        ## era Borders(4, 4, 4, 4)

define gui.vbar_borders = Borders(6, 6, 6, 6)          ## era Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)    ## era Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(6, 6, 6, 6)       ## era Borders(4, 4, 4, 4)

define gui.unscrollable = "hide"


## Histórico ###################################################################

define config.history_length = 250

define gui.history_height = 210        ## era 140
define gui.history_spacing = 0

define gui.history_name_xpos = 233     ## era 155
define gui.history_name_ypos = 0
define gui.history_name_width = 233    ## era 155
define gui.history_name_xalign = 1.0

define gui.history_text_xpos = 255     ## era 170
define gui.history_text_ypos = 3       ## era 2
define gui.history_text_width = 1110   ## era 740
define gui.history_text_xalign = 0.0


## Modo NVL ####################################################################

define gui.nvl_borders = Borders(0, 15, 0, 30)     ## era Borders(0, 10, 0, 20)
define gui.nvl_list_length = 6
define gui.nvl_height = 173                         ## era 115
define gui.nvl_spacing = 15                         ## era 10

define gui.nvl_name_xpos = 645                      ## era 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225                     ## era 150
define gui.nvl_name_xalign = 1.0

define gui.nvl_text_xpos = 675                      ## era 450
define gui.nvl_text_ypos = 12                       ## era 8
define gui.nvl_text_width = 885                     ## era 590
define gui.nvl_text_xalign = 0.0

define gui.nvl_thought_xpos = 360                   ## era 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170                 ## era 780
define gui.nvl_thought_xalign = 0.0

define gui.nvl_button_xpos = 675                    ## era 450
define gui.nvl_button_xalign = 0.0


## Localização #################################################################

define gui.language = "unicode"


################################################################################
## Dispositivos móveis
################################################################################

init python:

    @gui.variant
    def touch():
        gui.quick_button_borders = Borders(60, 21, 60, 0)  ## era Borders(40, 14, 40, 0)

    @gui.variant
    def small():

        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 30
        gui.button_text_size = 30
        gui.label_text_size = 34

        gui.textbox_height = 240
        gui.name_xpos = 80
        gui.dialogue_xpos = 90
        gui.dialogue_width = 1100

        gui.slider_size = 36

        gui.choice_button_width = 1240
        gui.choice_button_text_size = 30

        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10

        gui.history_height = 190
        gui.history_text_width = 690

        gui.quick_button_text_size = 20

        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        gui.nvl_height = 170

        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325

        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5

        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20

        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20
