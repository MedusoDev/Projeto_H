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

## ---- Visual provisório do fundo do mar (até ter o bg de verdade) ----
## Oceano = cor chapada escura; bolhas = os PNGs de círculo/anel do
## minigame, tingidos de azul, subindo em loop; sombra = silhueta escura
## difusa que surge quando o "ser" começa a falar.

image pesadelo_oceano = Solid("#04121e")

image pesadelo_sombra = Transform(
    "images/minigames/constelacao/circulo.png",
    xysize=(420, 640), matrixcolor=TintMatrix("#000408"), alpha=0.85,
)

## Respiração lenta da sombra (o fade-in fica no próprio ATL).
transform pesadelo_sombra_pose:
    subpixel True
    xalign 0.5 yalign 0.7 alpha 0.0
    linear 5.0 alpha 1.0
    block:
        easein 3.5 zoom 1.06
        easeout 3.5 zoom 1.0
        repeat

## Uma bolha: espera o atraso, sobe do rodapé até sair da tela balançando
## de leve, some e recomeça.
transform pesadelo_bolha(x0, dur, atraso, desvio):
    subpixel True
    xpos x0 ypos 770 xanchor 0.5 yanchor 0.5 alpha 0.0
    pause atraso
    block:
        ypos 770 xoffset 0 alpha 0.0
        parallel:
            linear dur ypos -60
        parallel:
            linear 0.8 alpha 1.0
            pause (dur - 1.6)
            linear 0.8 alpha 0.0
        parallel:
            linear (dur / 4) xoffset desvio
            linear (dur / 4) xoffset -desvio
            linear (dur / 4) xoffset desvio
            linear (dur / 4) xoffset 0
        repeat

init python:
    import random as _random_c01

    def _pesadelo_gerar_bolhas(qtd=16, seed=11):
        rng = _random_c01.Random(seed)
        bolhas = []
        for _ in range(qtd):
            x = rng.randint(30, 1250)
            tamanho = rng.choice([6, 8, 10, 14, 18, 24])
            duracao = round(rng.uniform(7.0, 16.0), 1)
            atraso = round(rng.uniform(0.0, 10.0), 1)
            desvio = rng.randint(10, 40)
            bolhas.append((x, tamanho, duracao, atraso, desvio))
        return bolhas

define pesadelo_bolhas_lista = _pesadelo_gerar_bolhas()

screen pesadelo_bolhas():
    for (bx, tam, dur, atraso, desvio) in pesadelo_bolhas_lista:
        ## Bolhas maiores são só o contorno (anel), as pequenas são cheias.
        $ img_bolha = "images/minigames/constelacao/anel.png" if tam >= 12 else "images/minigames/constelacao/circulo.png"
        add Transform(img_bolha, xysize=(tam, tam), matrixcolor=TintMatrix("#9fc8e8"), alpha=0.3) at pesadelo_bolha(bx, dur, atraso, desvio)


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
        ## (cada fala traz o próprio cps), então o slider de "Velocidade do
        ## texto" não interfere de nenhum jeito. Afogamento digita a 24,
        ## o ser a 30 — o ritmo diferente é caracterização.
        _cena01_cps_bkp = preferences.text_cps
        preferences.text_cps = 28

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
    pensamento "...{w=3.0}{nw}" (slow_abortable=False, cps=24)

    ## "Aos poucos surge um oceano profundo" — cor + bolhas subindo
    ## (placeholder até ter a arte do bg).
    scene pesadelo_oceano
    with Dissolve(3.0)
    show screen pesadelo_bolhas

    ## Sensações físicas primeiro: o jogador sente o afogamento antes do
    ## pensamento existencial.
    pensamento "Frio.{w=2.5}{nw}" (slow_abortable=False, cps=24)

    pensamento "Já não sei mais onde é pra cima.{w=2.5}{nw}" (slow_abortable=False, cps=24)

    pensamento "Não há mais nada a se fazer...{w=3.0}{nw}" (slow_abortable=False, cps=24)

    ## Tentáculos verdes surgem — efeito visual a implementar depois
    pensamento "...não há mais nada que eu possa fazer.{w=3.0}{nw}" (slow_abortable=False, cps=24)

    ## ====================================================================
    ## Contato — um ser desconhecido tenta se comunicar. O jogador não vai
    ## se lembrar disso ao acordar (só do pesadelo em si).
    ## ====================================================================

    ## A sombra surge ANTES da voz: primeiro se percebe, depois se ouve.
    show pesadelo_sombra at pesadelo_sombra_pose

    pensamento "...?{w=2.0}{nw}" (slow_abortable=False, cps=24)

    ## Primeiro contato falha: chega quebrado, em fragmentos.
    ser_glitch "{glitch=3}...ndo? Está me... {glitch=5}{w=2.2}{nw}" (slow_abortable=False, cps=30)

    ser "...Alô? Testando? Sempre erro essa magia maldita...{w=2.2}{nw}" (slow_abortable=False, cps=30)

    ser "Ahh! Agora te vejo.{w=2.2}{nw}" (slow_abortable=False, cps=30)

    ser "Que fundo você foi parar, hein...{w=2.2}{nw}" (slow_abortable=False, cps=30)

    ser "Senhor... qual é o seu nome mesmo?{w=2.5}{nw}" (slow_abortable=False, cps=30)

    ## Digitar o nome continua funcionando: o input confirma com Enter
    ## (evento "input_enter", não "dismiss"), então a trava não afeta.
    $ nome_jogador = renpy.input("Como você se chama?", length=20).strip() or "Estagiário"

    ser "Ahhh, sim. Senhor [nome_jogador].{w=2.2}{nw}" (slow_abortable=False, cps=30)

    ## Reação levemente errada ao nome — ele sabe mais do que diz.
    ser "É. Combina com você.{w=2.5}{nw}" (slow_abortable=False, cps=30)

    ## Tic-tac por baixo da fala — para quando ela termina
    play tictac "audio/clock_tictac.wav"

    ser_glitch "Escute bem, porque o tempo aqui é curto. Eu sou {glitch=10}{w=3.0}{nw}" (slow_abortable=False, cps=30)

    stop tictac fadeout 0.2
    ## Em loop: o alarme atravessa a transição e continua na Cena 02 até o
    ## jogador mandar o despertador parar (hotspot do relógio).
    play alarme "audio/clock_alarm_only.wav"

    ## O toque de verdade começa 2.8s dentro do áudio do alarme. O ambiente
    ## da cena corta exatamente nesse instante — a Cena 02 (por enquanto)
    ## não tem som ambiente próprio, então daqui pra frente é só o alarme.
    $ renpy.pause(2.8, hard=True)
    stop ambience fadeout 0.6
    stop ambience2 fadeout 0.6

    ## Luz pulsa no centro e corta a cena — o contato é interrompido antes
    ## de terminar a frase. O alarme continua tocando por cima da
    ## transição (emenda com o acordar na cena 02).
    window hide
    window auto

    hide screen pesadelo_bolhas

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
