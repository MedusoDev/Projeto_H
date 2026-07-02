## ---------- Efeito de texto glitch ----------
## Tag de texto {glitch=N} — insere um bloco de N caracteres embaralhados que
## se redesenha continuamente (efeito de nome/fala corrompida). Pode ser usado
## dentro do nome de um Character ou dentro de qualquer fala.

init python:
    import random

    ## Caracteres usados no embaralhamento — mexe à vontade
    _glitch_chars = "*&^%#@$!?/\\|<>~=+()0123456789ABCDEFabcdef"

    def _scramble(n):
        return "".join(random.choice(_glitch_chars) for _ in range(n))

    ## Função do DynamicDisplayable: redesenha um texto embaralhado a cada tick.
    ## n = quantos caracteres. O 0.06 no fim = velocidade do glitch (menor = mais rápido).
    ## Não passar size=None pro Text() — isso trava a resolução de estilo (o
    ## Text não consegue herdar um tamanho e quebra com AttributeError). Só
    ## inclui "size" nas propriedades quando um valor concreto for passado.
    def _glitch_render(st, at, n=7, color="#e02020", size=None):
        properties = {"color": color, "bold": True}
        if size is not None:
            properties["size"] = size
        d = Text(_scramble(n), **properties)
        return d, 0.06

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
