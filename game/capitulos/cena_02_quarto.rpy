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
]


screen quarto_exploracao(coletados):

    ## -- Fixos: sempre clicáveis, não alteram o bg --
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

    ## -- Coletáveis: somem depois de usados --
    for item in quarto_coletaveis:
        if not coletados[item["nome"]]:
            imagebutton:
                idle       Null(width=1280, height=720)
                hover      item["hover"]
                focus_mask item["hs"]
                keyboard_focus False
                style      "quarto_hs"
                xpos 0 ypos 0
                action Return(item["nome"])


label cena_02_quarto:

    scene bg quarto_day
    with fade

    show protagonista angry talk at protagonista_size, center
    with dissolve

    jogador "Esse maldito sonho de novo..."

    show protagonista neutral talk
    jogador "...Bom dia, ao menos espero que ele seja bom."

    jogador "Preciso ver que horas são... cadê meu celular?"

    hide protagonista
    with dissolve

    $ coletados = {item["nome"]: False for item in quarto_coletaveis}

label .loop:
    call screen quarto_exploracao(coletados)

    if _return == "losa":
        jump .losa
    elif _return == "foto":
        jump .foto
    elif _return in coletados:
        jump .item_coletado
    else:
        jump .loop


label .losa:
    show protagonista arms_pensativo neutral talk at protagonista_size, center
    with dissolve
    jogador "Eu devia ter limpado isso... resquício do antigo inquilino."
    jogador "Enfim, depois eu limpo."
    jogador "Pera... isso aqui parece pelo de bicho. Eu não tenho bicho."
    jogador "...Pet invisível?"
    hide protagonista
    with dissolve
    jump .loop


label .foto:
    show protagonista sad talk at protagonista_size, center
    with dissolve
    jogador "Essa foto é de outra pessoa que morava aqui antes..."
    jogador "Não sei o que aconteceu, mas... entendo o sentimento."
    hide protagonista
    with dissolve
    jump .loop


label .item_coletado:
    ## Aplica o item que acabou de ser usado: marca como coletado e troca o bg
    python:
        for item in quarto_coletaveis:
            if item["nome"] == _return:
                coletados[_return] = True
                renpy.scene()
                renpy.show("bg " + item["bg"])

    with dissolve

    jump .loop
