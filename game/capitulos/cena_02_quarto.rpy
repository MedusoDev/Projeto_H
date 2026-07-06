## ============================================================
## CENA 02 — QUARTO (MANHÃ)
## Background: quarto_day (room_full.png).
## ============================================================

## Estilo sem fundo, sem borda e sem indicador de foco — usado nos hotspots
style quarto_hs:
    background          None
    hover_background    None
    selected_idle_background  None
    selected_hover_background None
    insensitive_background    None
    padding (0, 0, 0, 0)
    focus_rect (0, 0, 0, 0)


## Coletáveis: somem da cena e trocam o bg quando usados.
## Adicionar um novo item aqui (+ os PNGs em coletaveis/) é o suficiente,
## a screen e o loop abaixo lidam com o resto.
define quarto_coletaveis = [
    {"nome": "fone", "hs": "hs_item_fone", "hover": "hs_item_fone_hover", "bg": "quarto_no_fone"},
    {"nome": "wand", "hs": "hs_item_wand", "hover": "hs_item_wand_hover", "bg": "quarto_no_fone_no_wand"},
    {"nome": "box", "hs": "hs_item_box", "hover": "hs_item_box_hover", "bg": "quarto_box_open"},
    {"nome": "jaleco", "hs": "hs_item_jaleco", "hover": "hs_item_jaleco_hover", "bg": "quarto_box_open_no_jaleco"},
]

## Piscada do hotspot da caixa depois do minigame, indicando onde clicar.
transform quarto_hs_pisca:
    alpha 0.15
    block:
        linear 0.6 alpha 0.75
        linear 0.6 alpha 0.15
        repeat


screen quarto_exploracao(coletados, pc_ativado, magia_feita=False, despertador_ok=False):

    ## O despertador é o primeiro gatilho da cena: sempre clicável.
    imagebutton:
        idle       Null(width=1280, height=720)
        hover      "hs_fixo_clock_hover"
        focus_mask "hs_fixo_clock"
        keyboard_focus False
        style      "quarto_hs"
        xpos 0 ypos 0
        action Return("clock")

    ## -- Fixos: só liberam depois de parar o despertador E pegar o fone --
    if coletados["fone"]:
        imagebutton:
            idle       Null(width=1280, height=720)
            hover      "hs_fixo_losa_hover"
            focus_mask "hs_fixo_losa"
            keyboard_focus False
            style      "quarto_hs"
            xpos 0 ypos 0
            action Return("losa")

        imagebutton:
            idle       Null(width=1280, height=720)
            hover      "hs_fixo_foto_hover"
            focus_mask "hs_fixo_foto"
            keyboard_focus False
            style      "quarto_hs"
            xpos 0 ypos 0
            action Return("foto")
        imagebutton:
            idle       Null(width=1280, height=720)
            hover      "hs_fixo_bed_hover"
            focus_mask "hs_fixo_bed"
            keyboard_focus False
            style      "quarto_hs"
            xpos 0 ypos 0
            action Return("bed")
        imagebutton:
            idle       Null(width=1280, height=720)
            hover      "hs_fixo_stone_hover"
            focus_mask "hs_fixo_stone"
            keyboard_focus False
            style      "quarto_hs"
            xpos 0 ypos 0
            action Return("stone")

        imagebutton:
            idle       Null(width=1280, height=720)
            hover      "hs_fixo_pc_hover"
            focus_mask "hs_fixo_pc"
            keyboard_focus False
            style      "quarto_hs"
            xpos 0 ypos 0
            action Return("pc")

    ## Caixa piscando depois do minigame, até o jogador abrir ela.
    if magia_feita and not coletados["box"]:
        add "hs_item_box_hover" at quarto_hs_pisca

    ## -- Coletáveis: somem depois de usados --
    for item in quarto_coletaveis:
        if not coletados[item["nome"]]:
            ## Ordem dos gatilhos: o fone só libera depois do despertador;
            ## a caixa, depois do minigame; o jaleco, depois dos livros;
            ## o resto, depois do fone.
            $ hs_liberado = despertador_ok if item["nome"] == "fone" else (magia_feita if item["nome"] == "box" else (coletados["box"] if item["nome"] == "jaleco" else coletados["fone"]))
            if hs_liberado:
                imagebutton:
                    idle       Null(width=1280, height=720)
                    hover      item["hover"]
                    focus_mask item["hs"]
                    keyboard_focus False
                    style      "quarto_hs"
                    xpos 0 ypos 0
                    ## A varinha só é coletada de verdade depois do gatilho do PC;
                    ## antes disso, clicar nela só mostra uma fala e não some da cena.
                    if item["nome"] == "wand" and not pc_ativado:
                        action Return("wand_pre")
                    else:
                        action Return(item["nome"])


label cena_02_quarto:

    scene bg quarto_day
    with fade

    show protagonista angry talk at protagonista_size, center
    with dissolve

    jogador "Esse maldito sonho de novo..."

    show protagonista neutral talk
    jogador "...Bom dia, ao menos espero que ele seja bom."

    jogador "..."

    jogador "Um pouco deprimente me dar um bom dia... enfim."

    show protagonista angry talk
    jogador "E esse despertador que não para de tocar..."

    hide protagonista
    with dissolve

    $ coletados = {item["nome"]: False for item in quarto_coletaveis}
    $ pc_ativado = False
    $ magia_feita = False
    $ despertador_parado = False

label .loop:
    call screen quarto_exploracao(coletados, pc_ativado, magia_feita, despertador_parado)

    if _return == "losa":
        jump .losa
    elif _return == "foto":
        jump .foto
    elif _return == "wand_pre":
        jump .wand_pre
    elif _return == "bed":
        jump .bed
    elif _return == "stone":
        jump .stone
    elif _return == "pc":
        jump .pc
    elif _return == "clock":
        jump .clock
    elif _return in coletados:
        jump .item_coletado
    else:
        jump .loop


label .losa:
    if pc_ativado:
        show protagonista neutral talk at protagonista_size, center
        with dissolve
        jogador "Juro que apago isso quando eu voltar."
        hide protagonista
        with dissolve
        jump .loop

    show protagonista arms_pensativo neutral talk at protagonista_size, center
    with dissolve
    jogador "Eu devia ter limpado isso... resquício do antigo inquilino."
    jogador "Enfim, depois eu limpo."
    jogador "Pera..."
    jogador "...Pet invisível?"
    hide protagonista
    with dissolve
    jump .loop

label .bed:
    show protagonista neutral talk at protagonista_size, center
    with dissolve
    jogador "Eu devia arrumar a cama minha mãe vai impli..."
    show protagonista sad talk at protagonista_size, center
    with dissolve
    jogador "..ah"
    jogador "Deixa.."
    hide protagonista
    with dissolve
    jump .loop

label .stone:
    if pc_ativado:
        show protagonista neutral talk at protagonista_size, center
        with dissolve
        jogador "Sem tempo para contemplar a pedra agora."
        hide protagonista
        with dissolve
        jump .loop

    show protagonista arms_pensativo  talk at protagonista_size, center
    with dissolve
    jogador "hum."
    jogador "hum.."
    jogador "hum..."
    jogador "Pedra"
    hide protagonista
    with dissolve
    jump .loop


label .wand_pre:
    show protagonista neutral talk at protagonista_size, center
    with dissolve
    jogador "As vezes eu esqueço que ela não gosta de lugares apertados."
    hide protagonista
    with dissolve
    jump .loop


label .clock:
    if not despertador_parado:
        ## Despertador mágico: obedece quando o dono manda. É o primeiro
        ## gatilho da cena — só depois dele o fone fica clicável.
        $ despertador_parado = True
        show protagonista neutral talk at protagonista_size, center
        with dissolve
        jogador "Já fez o suficiente. Pode parar agora."
        stop alarme fadeout 1.5
        pensamento "Silêncio. Bem melhor."
        show protagonista neutral talk
        jogador "Agora... preciso ver que horas são. Cadê meu celular?"
        hide protagonista
        with dissolve
    else:
        show protagonista neutral talk at protagonista_size, center
        with dissolve
        pensamento "Muito melhor assim."
        hide protagonista
        with dissolve
    jump .loop


label .pc:
    $ pc_ativado = True
    show protagonista arms_pensativo neutral talk at protagonista_size, center
    with dissolve
    jogador "Ok, se eu bobar mais vou me atrasar para o primeiro dia de trabalho."
    jogador "E sinceramente, to precisando muito desse emprego..."
    jogador "Mas antes preciso pegar algumas coisas..."
    jogador "Primeiro minha varinha."
    hide protagonista
    with dissolve
    jump .loop


label .foto:
    if pc_ativado:
        show protagonista neutral talk at protagonista_size, center
        with dissolve
        jogador "Sem tempo pra isso agora."
        hide protagonista
        with dissolve
        jump .loop

    show protagonista sad talk at protagonista_size, center
    with dissolve
    jogador "Essa foto é de outra pessoa que morava aqui antes..."
    jogador "Não sei o que aconteceu, mas... entendo o sentimento."
    hide protagonista
    with dissolve
    jump .loop


label .item_coletado:
    ## Aplica o item que acabou de ser usado: marca como coletado e troca o bg
    $ item_atual = _return
    python:
        for item in quarto_coletaveis:
            if item["nome"] == item_atual:
                coletados[item_atual] = True
                renpy.scene()
                renpy.show("bg " + item["bg"])

    with dissolve

    if item_atual == "fone":
        jump .fone_hora
    elif item_atual == "wand":
        jump .wand_pega
    elif item_atual == "box":
        jump .box_pega
    elif item_atual == "jaleco":
        jump .jaleco_pega

    jump .loop


label .wand_pega:
    show protagonista neutral talk at protagonista_size, center
    with dissolve
    jogador "Minha varinha. Única coisa que eu trouxe da escola que definitivamente não vai me trair."
    pensamento "...Espero."
    jogador "Ok, agora preciso dos livros..."
    jogador "Mas eles estão em uma dessas caixas... vai dar trabalho achar."
    jogador "A menos que..."
    show protagonista arms_pensativo neutral talk
    jogador "...eu use um feitiço de localização."
    hide protagonista
    with dissolve

label .magia:
    ## Minigame da constelação: repete até acertar (cancelar só faz o
    ## protagonista se reconcentrar e tentar de novo).
    $ mg_progresso = []
    $ mg_erro = False
    $ mg_dados = constelacao_preparar(constelacao_oreo)
    call screen constelacao_minigame(mg_dados)

    if _return == "vitoria":
        $ magia_feita = True
        show protagonista neutral talk at protagonista_size, center
        with dissolve
        jogador "Achei! Os livros estão naquela caixa."
        hide protagonista
        with dissolve
        jump .loop
    else:
        show protagonista huh talk at protagonista_size, center
        with dissolve
        pensamento "Não consigo me concentrar... de novo."
        hide protagonista
        with dissolve
        jump .magia


label .box_pega:
    show protagonista neutral talk at protagonista_size, center
    with dissolve
    jogador "Peguei os livros. Pesados como eu lembrava..."
    jogador "Agora só falta o jaleco e posso ir."
    hide protagonista
    with dissolve
    jump .loop


label .jaleco_pega:
    show protagonista neutral talk at protagonista_size, center
    with dissolve
    jogador "Jaleco... pronto."
    jogador "É isso. Hora de ir."
    hide protagonista
    with dissolve
    jump cena_03_ligacao


label .fone_hora:
    ## Close-up da mão com o celular mostrando a hora
    show protagonista_celular_hora at celular_hora_size
    with dissolve

    pause 1.5

    hide protagonista_celular_hora
    with dissolve

    show protagonista neutral talk at protagonista_size, center
    with dissolve
    jogador "7h12... ainda dá pra relaxar um pouco antes de precisar me arrumar de verdade."
    hide protagonista
    with dissolve

    jump .loop
