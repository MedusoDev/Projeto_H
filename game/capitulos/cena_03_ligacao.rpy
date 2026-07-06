## ============================================================
## CENA 03 — A LIGAÇÃO
## Tela preta. O telefone toca (phone_ring.wav, placeholder sintético
## gerado por tools/gerar_toque.py — trocar o arquivo mantendo o nome
## quando tiver o toque final). Depois de alguns toques aparecem as
## opções Atender / Ignorar.
##
## Diálogo sem sprite, só texto, e IMSKIPPÁVEL — mesma receita da Cena 01
## (keymap dismiss vazio + clear_keymap_cache; ritmo dentro do texto com
## {w=3.0}{nw}; nunca screen modal). O menu de escolha não é afetado pela
## trava: botão de choice não usa o evento "dismiss".
## ============================================================

label cena_03_ligacao:

    python:
        ## Mata clique/Enter/Espaço (dismiss), rollback e right-click.
        _cena03_keymap_bkp = {k: config.keymap[k] for k in ("dismiss", "rollback", "hide_windows")}
        config.keymap["dismiss"] = []
        config.keymap["rollback"] = []
        config.keymap["hide_windows"] = []
        renpy.clear_keymap_cache()

        _cena03_skip_bkp = config.allow_skipping
        config.allow_skipping = False

        ## Cena 03 digita mais rápido que a 01 (24 cps vs 16).
        _cena03_cps_bkp = preferences.text_cps
        preferences.text_cps = 24

        _cena03_menu_bkp = _game_menu_screen
        _game_menu_screen = None
        _cena03_qmenu_bkp = quick_menu
        quick_menu = False

    $ renpy.block_rollback()

    ## Se o jogador nunca mandou o despertador calar, cala aqui.
    stop alarme fadeout 1.0

    scene black
    with fade

    ## O telefone toca em loop até o jogador decidir o que fazer.
    play sound "audio/phone_ring.wav" loop
    window show

    "...{w=1.5}{nw}" (slow_abortable=False, cps=24)

    "Você recebe uma ligação antes de sair. Na tela está escrito: PAI.{w=2.5}{nw}" (slow_abortable=False, cps=24)

    menu:
        "Atender":
            jump .atender
        "Ignorar":
            jump .ignorar


label .atender:
    stop sound
    window show

    pai "Filho! Que bom que atendeu. Tava com saudade da sua voz.{w=3.0}{nw}" (slow_abortable=False, cps=24)

    jogador "Oi, pai. Tudo bem?{w=3.0}{nw}" (slow_abortable=False, cps=24)

    pai "Tudo, tudo. Bom, mais ou menos. Você sabe como é.{w=3.0}{nw}" (slow_abortable=False, cps=24)

    pai "Tava ligando pra saber como você tá se saindo por aí. Ainda... nessa escola.{w=3.0}{nw}" (slow_abortable=False, cps=24)

    pai "Não vou mentir, filho. Ainda não entendo essa escolha sua. Magia não é caminho pra ninguém da nossa família.{w=3.0}{nw}" (slow_abortable=False, cps=24)

    pensamento "E lá vamos nós.{w=3.0}{nw}" (slow_abortable=False, cps=24)

    pai "Mas enfim... fiz o que tinha que fazer. Deixei você ir. Só quero que saiba que... me preocupo.{w=3.0}{nw}" (slow_abortable=False, cps=24)

    pai "Ah, e por falar nisso — vi sua mãe na praça outro dia. Tá lindíssima, como sempre.{w=3.0}{nw}" (slow_abortable=False, cps=24)

    jogador "Pai...{w=3.0}{nw}" (slow_abortable=False, cps=24)

    pai "Não é nada. Se cuida, tá?{w=3.0}{nw}" (slow_abortable=False, cps=24)

    jogador "Certo. Tchau, pai.{w=3.0}{nw}" (slow_abortable=False, cps=24)

    pensamento "Ele nunca vai entender. Mas pelo menos ainda liga.{w=3.0}{nw}" (slow_abortable=False, cps=24)

    jump .fim


label .ignorar:
    stop sound fadeout 0.8
    window show

    "O telefone para de tocar.{w=3.0}{nw}" (slow_abortable=False, cps=24)

    pensamento "Hoje não, pai. Hoje não.{w=3.0}{nw}" (slow_abortable=False, cps=24)

    "Ele pega as coisas e sai.{w=3.0}{nw}" (slow_abortable=False, cps=24)

    jump .fim


label .fim:
    window hide
    window auto

    scene black
    with fade

    python:
        ## Restaura tudo que a cena travou
        for _k, _v in _cena03_keymap_bkp.items():
            config.keymap[_k] = _v
        renpy.clear_keymap_cache()
        config.allow_skipping = _cena03_skip_bkp
        preferences.text_cps = _cena03_cps_bkp
        _game_menu_screen = _cena03_menu_bkp
        quick_menu = _cena03_qmenu_bkp

    ## TODO: emendar na Cena 04 quando ela existir.
    return
