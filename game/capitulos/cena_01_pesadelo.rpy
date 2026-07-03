## ============================================================
## CENA 01 — PESADELO
## Sem sprite. Background: oceano escuro (perspectiva de afundar).
## Pensamentos do protagonista + contato de um ser desconhecido (nome
## sempre embaralhado via tag {glitch}, ver glitch.rpy) que pede o nome do
## jogador. O jogador não vai lembrar disso na Cena 02 — só do pesadelo em
## si, não do "ser".
##
## CENA TOTALMENTE SCRIPTADA — o jogador não controla o ritmo:
##   texto digita a cps fixo -> fica 3s na tela -> avança sozinho.
##
## Como a trava funciona (e por que as tentativas anteriores falharam):
## - slow_abortable=False sozinho NÃO segura o clique: como o clique não
##   pode completar o texto, ele cai no comportamento padrão seguinte e
##   DISPENSA A FALA INTEIRA (era isso que fazia a fala "pular").
## - A solução é matar o evento "dismiss" na raiz: config.keymap com
##   lista vazia. MAS o Ren'Py cacheia o keymap — mudança em runtime só
##   vale depois de renpy.clear_keymap_cache().
## - Screen modal para bloquear input NÃO serve: engole os timers do
##   {nw}/pause e trava a cena.
## - O ritmo de cada fala fica DENTRO do texto: "fala{w=3.0}{nw}". O {nw}
##   sozinho + renpy.pause depois NÃO funciona porque o {nw} encerra o
##   statement na hora, sem esperar a digitação — a pausa rodava em
##   paralelo com o texto ainda digitando e vencia junto com a última
##   letra (a fala "mal terminava e já pulava"). Já a tag {w=3.0} só é
##   processada quando a digitação CHEGA nela (depois da última letra), e
##   com o dismiss morto ninguém encurta a espera: digita -> segura 3s
##   com o texto completo -> {nw} avança sozinho.
## ============================================================

label cena_01_pesadelo:

    python:
        ## Mata clique/Enter/Espaço (dismiss), scroll de rollback e o
        ## right-click de esconder janela. Backup pra restaurar no fim.
        _cena01_keymap_bkp = {k: config.keymap[k] for k in ("dismiss", "rollback", "hide_windows")}
        config.keymap["dismiss"] = []
        config.keymap["rollback"] = []
        config.keymap["hide_windows"] = []
        renpy.clear_keymap_cache()   ## sem isso a mudança de keymap é ignorada

        ## Sem Ctrl-skip / botão de skip
        _cena01_skip_bkp = config.allow_skipping
        config.allow_skipping = False

        ## Velocidade fixa da cena: a preferência do player é neutralizada
        ## pro mesmo valor do cps por fala (16), então o slider de
        ## "Velocidade do texto" não interfere de nenhum jeito.
        _cena01_cps_bkp = preferences.text_cps
        preferences.text_cps = 16

        ## Sem menu (Esc) e sem quick menu — impede save/load e mudança de
        ## preferências no meio da cena
        _cena01_menu_bkp = _game_menu_screen
        _game_menu_screen = None
        _cena01_qmenu_bkp = quick_menu
        quick_menu = False

    $ renpy.block_rollback()

    scene black
    with fade

    play ambience "audio/504641__fission9__underwater-ambience.wav" fadein 2.0
    play ambience2 "audio/859447__coghezzi__alien-spaceship-interior-atmosphere-coghezzi-files.wav" fadein 2.0 volume 0.4

    ## Mantém a caixa de diálogo na tela o tempo todo (sem piscar entre
    ## falas).
    window show

    ## O ambiente começa a rolar e só aparece "..."
    pensamento "...{w=3.0}{nw}" (slow_abortable=False, cps=16)

    pensamento "Não há mais nada a se fazer...{w=3.0}{nw}" (slow_abortable=False, cps=16)

    ## Tentáculos verdes surgem — efeito visual a implementar depois
    pensamento "...não há mais nada que eu possa fazer.{w=3.0}{nw}" (slow_abortable=False, cps=16)

    ## ====================================================================
    ## Contato — um ser desconhecido tenta se comunicar. O jogador não vai
    ## se lembrar disso ao acordar (só do pesadelo em si).
    ## ====================================================================

    ser "Alô? Testando?... Sempre erro essa magia maldita...{w=3.0}{nw}" (slow_abortable=False, cps=16)

    ser "Ahh, agora te vejo!{w=3.0}{nw}" (slow_abortable=False, cps=16)

    ser "Senhor... qual é seu nome mesmo?{w=3.0}{nw}" (slow_abortable=False, cps=16)

    ## Digitar o nome continua funcionando: o input confirma com Enter
    ## (evento "input_enter", não "dismiss"), então a trava não afeta.
    $ nome_jogador = renpy.input("Como você se chama?", length=20).strip() or "Estagiário"

    ser "Ahhh, sim... senhor [nome_jogador].{w=3.0}{nw}" (slow_abortable=False, cps=16)

    ## Tic-tac por baixo da fala — para quando ela termina
    play tictac "audio/clock_tictac.wav"

    ser_glitch "Eu sou {glitch=10}...{w=3.0}{nw}" (slow_abortable=False, cps=16)

    stop tictac fadeout 0.2
    play sound "audio/clock_alarm_only.wav"

    ## Luz pulsa no centro e corta a cena — o contato é interrompido antes
    ## de terminar a frase. O alarme continua tocando por cima da
    ## transição (emenda com o acordar na cena 02).
    window hide
    window auto

    scene black
    with fade

    python:
        ## Restaura tudo que a cena travou
        for _k, _v in _cena01_keymap_bkp.items():
            config.keymap[_k] = _v
        renpy.clear_keymap_cache()
        config.allow_skipping = _cena01_skip_bkp
        preferences.text_cps = _cena01_cps_bkp
        _game_menu_screen = _cena01_menu_bkp
        quick_menu = _cena01_qmenu_bkp

    jump cena_02_quarto
