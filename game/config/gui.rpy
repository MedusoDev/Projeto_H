################################################################################
## Inicialização
################################################################################

## A instrução init offset faz com que as instruções de inicialização nesse
## arquivo sejam executadas antes das instruções init em qualquer outro arquivo.
init offset = -2

## Chamar gui.init redefine os estilos para os valores padrão sensatos e define
## a largura e a altura do jogo.
init python:
    gui.init(1248, 832)

## Habilitar verificações de propriedades inválidas ou instáveis em telas ou
## transformações
define config.check_conflicting_properties = True


################################################################################
## Variáveis de configuração da GUI
################################################################################
## Todos os valores de pixel abaixo estão calculados para 1248×832
## (escala ×0.65 horizontal / ×0.77 vertical a partir de 1920×1080).
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

define gui.text_size = 25
define gui.name_text_size = 35
define gui.interface_text_size = 25
define gui.label_text_size = 28
define gui.notify_text_size = 18
define gui.title_text_size = 58


## Menus principal e de jogos ##################################################

define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Diálogo #####################################################################

define gui.textbox_height = 214

define gui.textbox_yalign = 1.0

define gui.name_xpos = 234
define gui.name_ypos = 0

define gui.name_xalign = 0.0

define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False

define gui.dialogue_xpos = 261
define gui.dialogue_ypos = 58
define gui.dialogue_width = 725
define gui.dialogue_text_xalign = 0.0


## Botões ######################################################################

define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(4, 4, 4, 4)
define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size

define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0

define gui.radio_button_borders = Borders(18, 4, 4, 4)
define gui.check_button_borders = Borders(18, 4, 4, 4)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(10, 4, 10, 4)
define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 16
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color


## Botões de escolha ###########################################################

define gui.choice_button_width = 770
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(98, 5, 98, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## Botões de slot de arquivo ###################################################

define gui.slot_button_width = 269
define gui.slot_button_height = 238
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 16
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

define config.thumbnail_width = 250
define config.thumbnail_height = 166

define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Posicionamento e espaçamento ################################################

define gui.navigation_xpos = 39
define gui.skip_ypos = 12
define gui.notify_ypos = 52
define gui.choice_spacing = 22
define gui.navigation_spacing = 4
define gui.pref_spacing = 10
define gui.pref_button_spacing = 0
define gui.page_spacing = 0
define gui.slot_spacing = 10
define gui.main_menu_text_xalign = 1.0


## Quadros #####################################################################

define gui.frame_borders = Borders(4, 4, 4, 4)
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)
define gui.skip_frame_borders = Borders(16, 5, 50, 5)
define gui.notify_frame_borders = Borders(16, 5, 40, 5)
define gui.frame_tile = False


## Barras, barras de rolagem e controles deslizantes ###########################

define gui.bar_size = 29
define gui.scrollbar_size = 14
define gui.slider_size = 29

define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

define gui.unscrollable = "hide"


## Histórico ###################################################################

define config.history_length = 250

define gui.history_height = 162
define gui.history_spacing = 0

define gui.history_name_xpos = 151
define gui.history_name_ypos = 0
define gui.history_name_width = 151
define gui.history_name_xalign = 1.0

define gui.history_text_xpos = 166
define gui.history_text_ypos = 2
define gui.history_text_width = 722
define gui.history_text_xalign = 0.0


## Modo NVL ####################################################################

define gui.nvl_borders = Borders(0, 12, 0, 23)
define gui.nvl_list_length = 6
define gui.nvl_height = 133
define gui.nvl_spacing = 12

define gui.nvl_name_xpos = 419
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 146
define gui.nvl_name_xalign = 1.0

define gui.nvl_text_xpos = 439
define gui.nvl_text_ypos = 9
define gui.nvl_text_width = 575
define gui.nvl_text_xalign = 0.0

define gui.nvl_thought_xpos = 234
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 761
define gui.nvl_thought_xalign = 0.0

define gui.nvl_button_xpos = 439
define gui.nvl_button_xalign = 0.0


## Localização #################################################################

define gui.language = "unicode"


################################################################################
## Dispositivos móveis
################################################################################

init python:

    @gui.variant
    def touch():
        gui.quick_button_borders = Borders(39, 16, 39, 0)

    @gui.variant
    def small():

        gui.text_size = 23
        gui.name_text_size = 28
        gui.notify_text_size = 19
        gui.interface_text_size = 23
        gui.button_text_size = 23
        gui.label_text_size = 26

        gui.textbox_height = 185
        gui.name_xpos = 52
        gui.dialogue_xpos = 59
        gui.dialogue_width = 715

        gui.slider_size = 28

        gui.choice_button_width = 806
        gui.choice_button_text_size = 23

        gui.navigation_spacing = 15
        gui.pref_button_spacing = 8

        gui.history_height = 146
        gui.history_text_width = 449

        gui.quick_button_text_size = 15

        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        gui.nvl_height = 131

        gui.nvl_name_width = 198
        gui.nvl_name_xpos = 211

        gui.nvl_text_width = 595
        gui.nvl_text_xpos = 224
        gui.nvl_text_ypos = 4

        gui.nvl_thought_width = 806
        gui.nvl_thought_xpos = 13

        gui.nvl_button_width = 806
        gui.nvl_button_xpos = 13
