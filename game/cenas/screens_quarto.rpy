## ============================================================
## cenas/screens_quarto.rpy — Screen interativa do quarto
## ============================================================

screen quarto():

    default mensagem = ""
    default luz_ligada = True

    ## ---- Fundo ----
    ## Dinâmico: alterna entre luz ligada e luz do dia
    if luz_ligada:
        add "quarto_cortina_fechada_luz_ligada"
    else:
        add "quarto_cortina_fechada_luz_do_dia"

    ## ---- Cama (sprite permanente por cima do fundo) ----
    ##
    ## idle é a cama limpa (sem contorno), sempre visível.
    ## hover troca para a versão com contorno dourado.
    ## Fica aqui logo após o bg para o livros (que vem depois) ficar acima
    ## visualmente, caso as áreas se sobreponham.
    imagebutton:
        idle       "images/bg_room/cama_idle.png"
        hover      "images/bg_room/cama_hover_dourado.png"
        focus_mask "images/bg_room/cama_mask_dourado.png"
        action SetScreenVariable("mensagem",
            "Não agora. Tem trabalho pela frente.")

    ## ---- Botão invisível de fundo (limpa mensagem ao clicar fora) ----
    ##
    ## Definido ANTES do imagebutton dos livros: nos pixels cobertos pela
    ## mask dos livros o imagebutton tem prioridade; fora deles esse botão
    ## captura o clique e apaga a mensagem.

    if mensagem:
        button:
            xpos 0  ypos 0  xsize 1248  ysize 832
            background       None
            action SetScreenVariable("mensagem", "")

    ## ---- Hotspot: interruptor ----
    imagebutton:
        idle       "images/bg_room/interruptor_idle.png"
        hover      "images/bg_room/interruptor_hover.png"
        focus_mask "images/bg_room/interruptor_mask.png"
        action ToggleScreenVariable("luz_ligada")

    ## ---- Hotspot: livros ----
    imagebutton:
        idle       "images/bg_room/quarto_idle_transparente.png"
        hover      "images/bg_room/livros_hover.png"
        focus_mask "images/bg_room/livros_mask.png"
        action SetScreenVariable("mensagem",
            "Livros de pedagogia, alguns de história... e um de culinária que você jura não ter comprado.")

    ## ---- Caixa de mensagem ----
    if mensagem:
        frame:
            xalign  0.5
            ypos    690
            xsize   1050
            padding (35, 22)
            background Solid("#111111dd")
            text mensagem:
                color  "#e8e8e8"
                size   24
                italic True
                layout "subtitle"
