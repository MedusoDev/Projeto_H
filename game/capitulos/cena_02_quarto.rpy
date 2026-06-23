## ============================================================
## CENA 02 — QUARTO (MANHÃ)
## Background: quarto_day. Sem sprite de protagonista por enquanto.
## 8 objetos clicáveis em qualquer ordem.
## Gaveta 2 encerra a fase e avança para Cena 03 (ligação).
## ============================================================

## Estilo sem fundo, sem borda e sem indicador de foco — usado em todos os hotspots
style quarto_hs:
    background          None
    hover_background    None
    selected_idle_background  None
    selected_hover_background None
    insensitive_background    None
    padding (0, 0, 0, 0)
    focus_rect (0, 0, 0, 0)


screen quarto_exploracao():

    ## Gaveta 1 — contém a varinha
    imagebutton:
        idle       Null(width=1280, height=720)
        hover      "hs_gaveta1_hover"
        focus_mask "hs_gaveta1"
        keyboard_focus False
        style      "quarto_hs"
        xpos 0 ypos 0
        action Return("gaveta1")

    ## Gaveta 2 — encerra a exploração (pegar roupas)
    imagebutton:
        idle       Null(width=1280, height=720)
        hover      "hs_gaveta2_hover"
        focus_mask "hs_gaveta2"
        keyboard_focus False
        style      "quarto_hs"
        xpos 0 ypos 0
        action Return("gaveta2")

    ## Cama
    imagebutton:
        idle       Null(width=1280, height=720)
        hover      "hs_cama_hover"
        focus_mask "hs_cama"
        keyboard_focus False
        style      "quarto_hs"
        xpos 0 ypos 0
        action Return("cama")

    ## Computador — agenda do dia
    imagebutton:
        idle       Null(width=1280, height=720)
        hover      "hs_computador_hover"
        focus_mask "hs_computador"
        keyboard_focus False
        style      "quarto_hs"
        xpos 0 ypos 0
        action Return("computador")

    ## Quadro — foto com rosto riscado
    imagebutton:
        idle       Null(width=1280, height=720)
        hover      "hs_quadro_hover"
        focus_mask "hs_quadro"
        keyboard_focus False
        style      "quarto_hs"
        xpos 0 ypos 0
        action Return("quadro")

    ## Celular
    imagebutton:
        idle       Null(width=1280, height=720)
        hover      "hs_celular_hover"
        focus_mask "hs_celular"
        keyboard_focus False
        style      "quarto_hs"
        xpos 0 ypos 0
        action Return("celular")

    ## Abajur
    imagebutton:
        idle       Null(width=1280, height=720)
        hover      "hs_abajur_hover"
        focus_mask "hs_abajur"
        keyboard_focus False
        style      "quarto_hs"
        xpos 0 ypos 0
        action Return("abajur")

    ## Relógio
    imagebutton:
        idle       Null(width=1280, height=720)
        hover      "hs_relogio_hover"
        focus_mask "hs_relogio"
        keyboard_focus False
        style      "quarto_hs"
        xpos 0 ypos 0
        action Return("relogio")


## ------------------------------------------------------------
## Label principal
## ------------------------------------------------------------

label cena_02_quarto:

    scene bg quarto_day
    with fade

    ## TODO: show sprite protagonista expressão sonolenta quando disponível

    jogador "Esse maldito sonho de novo..."
    jogador "...Bom dia, ao menos espero que ele seja bom."


label .loop:
    call screen quarto_exploracao

    if _return == "gaveta1":
        jump cena_02_quarto.gaveta1
    elif _return == "gaveta2":
        jump cena_02_quarto.gaveta2
    elif _return == "cama":
        jump cena_02_quarto.cama
    elif _return == "computador":
        jump cena_02_quarto.computador
    elif _return == "quadro":
        jump cena_02_quarto.quadro
    elif _return == "celular":
        jump cena_02_quarto.celular
    elif _return == "abajur":
        jump cena_02_quarto.abajur
    elif _return == "relogio":
        jump cena_02_quarto.relogio
    else:
        jump cena_02_quarto.loop


## ------------------------------------------------------------
## Interações
## ------------------------------------------------------------

label .gaveta1:
    ## Varinha aparece saindo da gaveta — TODO: show sprite varinha
    jogador "Minha varinha. Única coisa que eu trouxe da escola que definitivamente não vai me trair."
    pensamento "...Espero."
    jump cena_02_quarto.loop

label .cama:
    jogador "Acabei de acordar, agora não."
    pensamento "Eu sei o que você tá pensando e a resposta é não."
    jump cena_02_quarto.loop

label .computador:
    ## Agenda do dia — crítico: lista as tarefas que serão rastreadas no mapa
    jogador "Certo. Só isso. Eu consigo."
    ## TODO: implementar screen de UI com lista de tarefas quando o mapa for feito
    jump cena_02_quarto.loop

label .quadro:
    ## Foto com rosto riscado — aparece de novo na Cena 10-B quando Nósfera entra
    pensamento "..."
    pensamento "Nem sei porque ainda guardo isso."
    jump cena_02_quarto.loop

label .celular:
    jogador "Nenhuma mensagem."
    jump cena_02_quarto.loop

label .abajur:
    jogador "Comprei esse abajur porque tava barato. Não combina com nada no quarto mas não vou admitir isso pra ninguém."
    jump cena_02_quarto.loop

label .relogio:
    jogador "Já fez o suficiente. Pode parar agora."
    jump cena_02_quarto.loop

label .gaveta2:
    ## Encerra a exploração — avança para Cena 03
    jogador "Roupas. Certo."
    pensamento "Pronto."
    ## jump cena_03_ligacao
    ## Cena 03 ainda não implementada — retorna ao menu por enquanto
    return
