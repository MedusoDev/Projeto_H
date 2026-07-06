## ============================================================
## MINIGAME — CONSTELAÇÃO (placeholder genérico)
## Ligar os pontos na ordem certa pra formar a constelação de
## referência mostrada no canto da tela. Sem arte final ainda:
## pontos e linhas são formas sólidas (Solid) só pra validar a
## mecânica antes de entrar com os assets.
## ============================================================

## Arte final (opcional): se estes arquivos existirem, o minigame usa eles
## no lugar das formas sólidas de placeholder.
define CONSTELACAO_IMG_PONTO_OFF = "images/minigames/constelacao/ponto_off.png"
define CONSTELACAO_IMG_PONTO_ON = "images/minigames/constelacao/ponto_on.png"
define CONSTELACAO_IMG_LINHA = "images/minigames/constelacao/linha.png"
define CONSTELACAO_IMG_FUNDO = "images/minigames/constelacao/fundo.png"

init python:
    import math

    ## Círculos perfeitos: PNGs brancos pré-gerados (tools/gerar_circulos.py)
    ## tingidos da cor desejada. "caixa" é o tamanho total do displayable
    ## (área de clique), "diametro" é o tamanho visual do círculo, centrado.
    def _constelacao_forma(img, cor, caixa, diametro):
        if renpy.loadable(img):
            base = Transform(img, xysize=(diametro, diametro), matrixcolor=TintMatrix(cor))
        else:
            base = Solid(cor, xsize=diametro, ysize=diametro)
        return Fixed(Transform(base, align=(0.5, 0.5)), xysize=(caixa, caixa))

    def _constelacao_circulo(cor, caixa, diametro):
        return _constelacao_forma("images/minigames/constelacao/circulo.png", cor, caixa, diametro)

    def _constelacao_anel(cor, caixa, diametro):
        return _constelacao_forma("images/minigames/constelacao/anel.png", cor, caixa, diametro)

    def _constelacao_linha(p1, p2, largura=3, cor="#ffffff"):
        x1, y1 = p1
        x2, y2 = p2
        dx = x2 - x1
        dy = y2 - y1
        comprimento = max(1, int(math.hypot(dx, dy)))
        angulo = math.degrees(math.atan2(dy, dx))
        if renpy.loadable(CONSTELACAO_IMG_LINHA):
            base = Transform(CONSTELACAO_IMG_LINHA, xysize=(comprimento, largura))
        else:
            base = Solid(cor, xsize=comprimento, ysize=largura)
        ## A rotação do Ren'Py preserva o centro do displayable, então a única
        ## ancoragem exata é centro da linha no ponto médio entre p1 e p2.
        return Transform(
            base,
            xpos=int((x1 + x2) / 2.0), ypos=int((y1 + y2) / 2.0),
            xanchor=0.5, yanchor=0.5,
            rotate=angulo, rotate_pad=False,
        )

    def _constelacao_ref(dados, largura, altura, margem=14):
        """Reprojeta os pontos da constelação (só os da ordem — os falsos
        ficam de fora) pra caberem centralizados na caixinha de referência,
        mantendo a proporção do desenho."""
        reais = {pid: dados["pontos"][pid] for pid in dados["ordem"]}
        xs = [p[0] for p in reais.values()]
        ys = [p[1] for p in reais.values()]
        dx = max(xs) - min(xs) or 1
        dy = max(ys) - min(ys) or 1
        escala = min((largura - 2 * margem) / float(dx), (altura - 2 * margem) / float(dy))
        off_x = (largura - dx * escala) / 2.0
        off_y = (altura - dy * escala) / 2.0
        return {
            pid: (off_x + (x - min(xs)) * escala, off_y + (y - min(ys)) * escala)
            for pid, (x, y) in reais.items()
        }

    def constelacao_preparar(dados):
        """Monta a versão jogável da constelação: os pontos reais ficam no
        lugar exato salvo no editor, e os falsos (campo "fakes") são
        sorteados a cada partida — longe dos reais, das bordas e da caixa
        de referência."""
        pontos = dict(dados["pontos"])
        restam = dados.get("fakes", 0)
        prox = max(pontos) + 1
        tentativas = 0
        while restam > 0 and tentativas < 400:
            tentativas += 1
            x = renpy.random.randint(70, 1210)
            y = renpy.random.randint(70, 640)
            if x > 980 and y < 280:
                continue  # área da caixa de referência
            if all(math.hypot(x - px, y - py) >= 70 for px, py in pontos.values()):
                pontos[prox] = (x, y)
                prox += 1
                restam -= 1
        novo = dict(dados)
        novo["pontos"] = pontos
        return novo

    def constelacao_clicar(dados, pid):
        store.mg_erro = False
        if store.mg_progresso and pid == store.mg_progresso[-1]:
            ## Clicou no último ponto ligado: linha de comprimento zero, ignora.
            ## (Revisitar pontos mais antigos é permitido — pontos duplos.)
            return
        if not store.mg_progresso:
            ## Primeiro clique: só o ponto de início (que brilha) responde.
            ## Clicar em outro não dá feedback nenhum, pra não entregar dica.
            if pid == dados["ordem"][0]:
                store.mg_progresso = [pid]
                renpy.restart_interaction()
            return
        ## Ligações livres, sem validar no meio do caminho.
        store.mg_progresso = store.mg_progresso + [pid]
        limite = dados.get("limite", len(dados["ordem"]) - 1)
        if len(store.mg_progresso) - 1 >= limite:
            ## Gastou todas as ligações: só agora confere com a referência.
            if store.mg_progresso == list(dados["ordem"]):
                return "vitoria"
            store.mg_erro = True
            store.mg_progresso = []
        renpy.restart_interaction()


## ---- Céu estrelado do fundo: cópia exata do editor (tkinter) ----
## Mesma seed (42), mesmas cores e posições estáticas do editor.

## Anel pulsante do ponto de início (igual ao editor: cresce e encolhe).
transform mg_ponto_inicio_brilho:
    subpixel True
    alpha 0.9 zoom 0.85
    block:
        linear 0.55 zoom 1.2 alpha 0.55
        linear 0.55 zoom 0.85 alpha 0.9
        repeat

init python:
    import random as _random

    def _constelacao_gerar_estrelas(qtd=90, seed=42):
        rng = _random.Random(seed)
        cores = ["#555566", "#777788", "#9999aa"]
        estrelas = []
        for _ in range(qtd):
            x = rng.randint(0, 1280)
            y = rng.randint(0, 720)
            tamanho = rng.choice([1, 1, 2])
            cor = rng.choice(cores)
            estrelas.append((x, y, tamanho, cor))
        return estrelas

define constelacao_estrelas_fundo = _constelacao_gerar_estrelas()

screen constelacao_fundo():
    add Solid("#05060f")
    for (ex, ey, es, cor) in constelacao_estrelas_fundo:
        add Solid(cor, xsize=es, ysize=es) xpos ex ypos ey


default mg_progresso = []
default mg_erro = False

## Dado de exemplo: 12 pontos espalhados de forma irregular pelo céu.
## Só 5 formam o "M" torto (constelação real não é simétrica) — o resto
## é ponto falso. "ordem" define o desenho e o ponto de início (primeiro
## da lista). "limite" é quantas ligações o jogador pode fazer.
## (Evitar pontos em x>1000/y<260, que é onde fica a caixa de referência.)
define constelacao_teste = {
    "pontos": {
        1: (390, 250),    # M — pico esquerdo
        2: (540, 170),
        3: (800, 230),    # M — pico direito
        4: (980, 350),
        5: (210, 380),
        6: (610, 420),    # M — vale do meio
        7: (740, 350),
        8: (450, 490),
        9: (330, 560),    # M — início (base esquerda)
        10: (640, 615),
        11: (890, 545),   # M — base direita
        12: (150, 180),
    },
    "ordem": [9, 1, 6, 3, 11],
    "limite": 4,
}


screen constelacao_minigame(dados):
    modal True

    if renpy.loadable(CONSTELACAO_IMG_FUNDO):
        add Transform(CONSTELACAO_IMG_FUNDO, xysize=(config.screen_width, config.screen_height))
    else:
        use constelacao_fundo

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
                $ ref = _constelacao_ref(dados, 220, 165)
                for i in range(len(dados["ordem"]) - 1):
                    add _constelacao_linha(ref[dados["ordem"][i]], ref[dados["ordem"][i + 1]], largura=2, cor="#88ccffcc")
                for pid, pos in ref.items():
                    ## Sem legenda: a cor fala por si — amarelo é o início,
                    ## verde é ponto duplo (se só houver verde, ele é os dois).
                    $ eh_duplo_ref = dados["ordem"].count(pid) >= 2
                    $ eh_inicio_ref = pid == dados["ordem"][0]
                    $ cor_ref = "#66dd66" if eh_duplo_ref else ("#ffcc33" if eh_inicio_ref else "#ffffff")
                    add _constelacao_circulo(cor_ref, 12, 8) xpos int(pos[0]) ypos int(pos[1]) xanchor 0.5 yanchor 0.5

    ## -- Linhas já ligadas pelo jogador --
    fixed:
        for i in range(len(mg_progresso) - 1):
            $ p1 = dados["pontos"][mg_progresso[i]]
            $ p2 = dados["pontos"][mg_progresso[i + 1]]
            add _constelacao_linha(p1, p2)

    ## -- Pontos clicáveis (reais e falsos, sem distinção visual) --
    for pid, pos in dados["pontos"].items():
        $ conectado = pid in mg_progresso
        $ duplo = mg_progresso.count(pid) >= 2
        $ img_ponto = CONSTELACAO_IMG_PONTO_ON if conectado else CONSTELACAO_IMG_PONTO_OFF
        ## Cores iguais às do editor: azul solto, amarelo ligado, verde duplo.
        $ cor_ponto = "#66dd66" if duplo else ("#ffcc33" if conectado else "#8899ff")
        $ cor_hover = "#88ee88" if duplo else ("#ffdd66" if conectado else "#b8c4ff")
        ## Anel pulsante marcando o ponto de início, enquanto não foi clicado.
        if pid == dados["ordem"][0] and not mg_progresso:
            add _constelacao_anel("#ffe98c", 48, 38) xpos pos[0] ypos pos[1] xanchor 0.5 yanchor 0.5 at mg_ponto_inicio_brilho
        button:
            xpos pos[0] ypos pos[1] xanchor 0.5 yanchor 0.5
            xysize (30, 30)
            if renpy.loadable(img_ponto):
                background Transform(img_ponto, xysize=(30, 30))
                hover_background Transform(img_ponto, xysize=(30, 30), matrixcolor=BrightnessMatrix(0.15))
            else:
                background _constelacao_circulo(cor_ponto, 30, 18)
                hover_background _constelacao_circulo(cor_hover, 30, 18)
            action Function(constelacao_clicar, dados, pid)

    ## -- HUD: contador de ligações e mensagens --
    $ mg_limite = dados.get("limite", len(dados["ordem"]) - 1)
    $ mg_usadas = max(0, len(mg_progresso) - 1)
    text "Ligações: [mg_usadas]/[mg_limite]" xalign 0.03 yalign 0.05 size 26 color "#ffffff"

    if mg_erro:
        text "Não era a constelação da referência. De volta ao começo." xalign 0.5 yalign 0.92 size 28 color "#ff5555"
    elif not mg_progresso:
        text "Comece pelo ponto que brilha." xalign 0.5 yalign 0.92 size 24 color "#ffe98c"

    textbutton "Cancelar":
        xalign 0.02 yalign 0.95
        action Return("cancelado")


## Label de teste isolado — chamar via "jump constelacao_demo" (ex: pelo
## console de desenvolvedor, shift+O) pra validar a mecânica sem depender
## do fluxo da Cena 02, que ainda não está integrado a este minigame.
label constelacao_demo:
    $ mg_progresso = []
    $ mg_erro = False
    ## Preparar fora do call screen: sorteia os fakes UMA vez por partida
    ## (dentro do call screen, re-sortearia a cada clique).
    $ mg_dados = constelacao_preparar(constelacao_dupla)
    call screen constelacao_minigame(mg_dados)

    if _return == "vitoria":
        "Constelação completa!"
    else:
        "Minigame cancelado."

    return
