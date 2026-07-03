## ============================================================
## MINIGAME — CONSTELAÇÃO (placeholder genérico)
## Ligar os pontos na ordem certa pra formar a constelação de
## referência mostrada no canto da tela. Sem arte final ainda:
## pontos e linhas são formas sólidas (Solid) só pra validar a
## mecânica antes de entrar com os assets.
## ============================================================

init python:
    import math

    def _constelacao_linha(p1, p2, largura=4, cor="#ffffffcc"):
        x1, y1 = p1
        x2, y2 = p2
        dx = x2 - x1
        dy = y2 - y1
        comprimento = max(1, int(math.hypot(dx, dy)))
        angulo = math.degrees(math.atan2(dy, dx))
        return Transform(
            Solid(cor, xsize=comprimento, ysize=largura),
            xpos=x1, ypos=y1, xanchor=0.0, yanchor=0.5,
            rotate=angulo, rotate_pad=False,
        )

    def constelacao_clicar(dados, pid):
        store.mg_erro = False
        esperado = dados["ordem"][len(store.mg_progresso)]
        if pid == esperado:
            store.mg_progresso.append(pid)
            if len(store.mg_progresso) == len(dados["ordem"]):
                return "vitoria"
        else:
            store.mg_erro = True
            store.mg_progresso = []
        renpy.restart_interaction()


## Dado de exemplo só pra testar a mecânica (5 pontos formando um "M").
define constelacao_teste = {
    "pontos": {
        1: (360, 460),
        2: (460, 260),
        3: (560, 400),
        4: (660, 260),
        5: (760, 460),
    },
    "ordem": [1, 2, 3, 4, 5],
}


screen constelacao_minigame(dados):
    modal True

    add Solid("#000000cc")

    ## -- Referência (miniatura reduzida do desenho correto) --
    frame:
        xalign 1.0 yalign 0.0
        xmargin 30 ymargin 30
        padding (14, 14)
        background "#101018e0"
        vbox:
            spacing 6
            text "Referência" size 22 color "#ffffff"
            fixed:
                xsize 220 ysize 165
                for i in range(len(dados["ordem"]) - 1):
                    $ p1 = dados["pontos"][dados["ordem"][i]]
                    $ p2 = dados["pontos"][dados["ordem"][i + 1]]
                    add _constelacao_linha((p1[0] / 5.0, p1[1] / 5.0), (p2[0] / 5.0, p2[1] / 5.0), largura=2, cor="#88ccffcc")
                for pid, pos in dados["pontos"].items():
                    add Transform(Solid("#ffffff"), xsize=6, ysize=6, xpos=pos[0] / 5.0, ypos=pos[1] / 5.0, xanchor=0.5, yanchor=0.5)

    ## -- Linhas já ligadas pelo jogador --
    fixed:
        for i in range(len(mg_progresso) - 1):
            $ p1 = dados["pontos"][mg_progresso[i]]
            $ p2 = dados["pontos"][mg_progresso[i + 1]]
            add _constelacao_linha(p1, p2)

    ## -- Pontos clicáveis --
    for pid, pos in dados["pontos"].items():
        button:
            xpos pos[0] ypos pos[1] xanchor 0.5 yanchor 0.5
            xysize (36, 36)
            background (Solid("#ffcc33") if pid in mg_progresso else Solid("#4466ffcc"))
            hover_background (Solid("#ffcc33") if pid in mg_progresso else Solid("#6688ffee"))
            action Function(constelacao_clicar, dados, pid)

    if mg_erro:
        text "Ordem errada, tente de novo." xalign 0.5 yalign 0.92 size 28 color "#ff5555"

    textbutton "Cancelar":
        xalign 0.02 yalign 0.95
        action Return("cancelado")


## Label de teste isolado — chamar via "jump constelacao_demo" (ex: pelo
## console de desenvolvedor, shift+O) pra validar a mecânica sem depender
## do fluxo da Cena 02, que ainda não está integrado a este minigame.
label constelacao_demo:
    $ mg_progresso = []
    $ mg_erro = False
    call screen constelacao_minigame(constelacao_teste)

    if _return == "vitoria":
        "Constelação completa!"
    else:
        "Minigame cancelado."

    return
