## ---------- Efeito de texto glitch ----------
## Tag de texto {glitch=N} — insere um bloco de N caracteres embaralhados que
## se redesenha continuamente (efeito de nome/fala corrompida). Pode ser usado
## dentro do nome de um Character ou dentro de qualquer fala.

init python:
    import random

    ## Visual "nome censurado com interferência": na maior parte do tempo o
    ## nome é um bloco estável (▓▓▓▓ = redigido/selado); a cada ~2.2s vem uma
    ## rajada curta em que os blocos se corrompem em símbolos e a cor acende.
    ## Os glifos são todos do DejaVuSans (que vem com o Ren'Py) — a fonte é
    ## forçada abaixo pra não depender da fonte da GUI ter esses caracteres.
    _glitch_simbolos = "▚▞▛▜▙▟░▒█╳╬┼∆∇∴≠"

    ## Não passar size=None pro Text() — isso trava a resolução de estilo (o
    ## Text não consegue herdar um tamanho e quebra com AttributeError). Só
    ## inclui "size" nas propriedades quando um valor concreto for passado.
    def _glitch_render(st, at, n=7, color="#e02020", size=None):
        ciclo = 2.2      # duração de um ciclo calmo+rajada
        rajada_dur = 0.35
        rajada = (st % ciclo) > (ciclo - rajada_dur)
        tique = 0.05 if rajada else 0.18

        ## Random determinístico por frame do efeito: mesmo st = mesmo
        ## desenho (estável em rollback/redraw).
        rng = random.Random(int(st / tique) * 9973 + n)

        chars = []
        for _ in range(n):
            if rajada and rng.random() < 0.55:
                chars.append(rng.choice(_glitch_simbolos))
            elif rng.random() < 0.08:
                chars.append(rng.choice("▒█"))
            else:
                chars.append("▓")

        properties = {
            "color": ("#ff4040" if rajada else color),
            "bold": True,
            "font": "DejaVuSans.ttf",
        }
        if size is not None:
            properties["size"] = size
        return Text("".join(chars), **properties), tique

    ## Tag de texto {glitch=N} — insere um bloco glitch animado dentro de qualquer texto,
    ## inclusive dentro do NOME do personagem.
    def glitch_tag(tag, argument):
        try:
            n = int(argument)
        except (ValueError, TypeError):
            n = 7
        return [ (renpy.TEXT_DISPLAYABLE, DynamicDisplayable(_glitch_render, n=n)) ]

    ## Self-closing: {glitch=7} é usada sozinha, sem tag de fechamento
    ## {/glitch}, então precisa ser registrada aqui (não em custom_text_tags,
    ## que espera um par abre/fecha com assinatura func(tag, value, contents)).
    config.self_closing_custom_text_tags["glitch"] = glitch_tag
