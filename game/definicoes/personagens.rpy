## ---------- Personagens ----------

## Jogador — nome inserido pelo jogador na tela de nome
## image="protagonista" liga este Character ao layeredimage abaixo, permitindo
## a forma curta `jogador neutral talk "Frase."` para trocar a expressão e
## falar na mesma linha (mostra o sprite automaticamente se ainda não estiver em cena).
define jogador     = Character("[nome_jogador]", color="#e0e0ff", image="protagonista")
define pensamento  = Character(None, what_italic=True, what_color="#b0b0c8")

## -----------------------------------------------------------------------
## Protagonista — sprite em camadas (base + expressões avulsas)
## Sprites: images/personagens/protagonista/
## base.png tem o rosto em branco; eyebrows_*/mouth_*/sweat.png encaixam por cima,
## todos no mesmo canvas (sem necessidade de offset).
## -----------------------------------------------------------------------

layeredimage protagonista:
    always:
        "images/personagens/protagonista/base.png"

    group eyebrows:
        attribute neutral default:
            "images/personagens/protagonista/eyebrows_neutral.png"
        attribute sad:
            "images/personagens/protagonista/eyebrows_sad.png"
        attribute angry:
            "images/personagens/protagonista/eyebrows_angry.png"
        attribute huh:
            "images/personagens/protagonista/eyebrows_huh.png"

    group mouth:
        attribute talk default:
            "images/personagens/protagonista/mouth_talk.png"
        attribute frown:
            "images/personagens/protagonista/mouth_frown.png"

    ## Acessório opcional — sem "default", só aparece se for pedido (ex: "show protagonista sweat")
    group sweat:
        attribute sweat:
            "images/personagens/protagonista/sweat.png"

## Mesmo padrão de tamanho usado em kimiko/moria (ysize=600).
## Usar com "at protagonista_size, <posicao>".
transform protagonista_size:
    ysize 600

## -----------------------------------------------------------------------
## Kimiko — centopeia mágica
## Sprites: images/personagens/kimiko/ | Pack: Wuxia Beastman – Centipede
## -----------------------------------------------------------------------
define kimiko = Character("Kimiko", color="#6abf6a")

image anqian neutral           = Transform("images/personagens/kimiko/anqian_neutral.png",           ysize=600)
image anqian neutraltalk       = Transform("images/personagens/kimiko/anqian_neutraltalk.png",       ysize=600)
image anqian happysmile        = Transform("images/personagens/kimiko/anqian_happysmile.png",        ysize=600)
image anqian happytalk         = Transform("images/personagens/kimiko/anqian_happytalk.png",         ysize=600)
image anqian happytalkclosed   = Transform("images/personagens/kimiko/anqian_happytalkclosed.png",   ysize=600)
image anqian smile             = Transform("images/personagens/kimiko/anqian_smile.png",             ysize=600)
image anqian nervouslaugh      = Transform("images/personagens/kimiko/anqian_nervouslaugh.png",      ysize=600)
image anqian nervouslaughclosed= Transform("images/personagens/kimiko/anqian_nervouslaughclosed.png",ysize=600)
image anqian sweatdrop         = Transform("images/personagens/kimiko/anqian_sweatdrop.png",         ysize=600)
image anqian worried           = Transform("images/personagens/kimiko/anqian_worried.png",           ysize=600)
image anqian sad               = Transform("images/personagens/kimiko/anqian_sad.png",               ysize=600)
image anqian sadtalk           = Transform("images/personagens/kimiko/anqian_sadtalk.png",           ysize=600)
image anqian resigned          = Transform("images/personagens/kimiko/anqian_resigned.png",          ysize=600)
image anqian resignedtalk      = Transform("images/personagens/kimiko/anqian_resignedtalk.png",      ysize=600)

## -----------------------------------------------------------------------
## Moria — panda vermelho
## Sprites: images/personagens/moria/ | Pack: Wuxia Beastman – Red Panda
## -----------------------------------------------------------------------
define moria = Character("Moria", color="#e05a30")

image lindan neutral           = Transform("images/personagens/moria/lindan_neutral.png",           ysize=600)
image lindan neutraltalk       = Transform("images/personagens/moria/lindan_neutraltalk.png",       ysize=600)
image lindan serious           = Transform("images/personagens/moria/lindan_serious.png",           ysize=600)
image lindan serioustalk       = Transform("images/personagens/moria/lindan_serioustalk.png",       ysize=600)
image lindan smile             = Transform("images/personagens/moria/lindan_smile.png",             ysize=600)
image lindan happysmile        = Transform("images/personagens/moria/lindan_happysmile.png",        ysize=600)
image lindan happytalk         = Transform("images/personagens/moria/lindan_happytalk.png",         ysize=600)
image lindan laugh             = Transform("images/personagens/moria/lindan_laugh.png",             ysize=600)
image lindan nervoussmile      = Transform("images/personagens/moria/lindan_nervoussmile.png",      ysize=600)
image lindan nervousgrin       = Transform("images/personagens/moria/lindan_nervousgrin.png",       ysize=600)
image lindan nervouslaugh      = Transform("images/personagens/moria/lindan_nervouslaugh.png",      ysize=600)
image lindan challengingsmile  = Transform("images/personagens/moria/lindan_challengingsmile.png",  ysize=600)
image lindan challenginglaugh  = Transform("images/personagens/moria/lindan_challenginglaugh.png",  ysize=600)
image lindan surprised         = Transform("images/personagens/moria/lindan_surprised.png",         ysize=600)
image lindan surprisedtalk     = Transform("images/personagens/moria/lindan_surprisedtalk.png",     ysize=600)
image lindan sad               = Transform("images/personagens/moria/lindan_sad.png",               ysize=600)
image lindan sadtalk           = Transform("images/personagens/moria/lindan_sadtalk.png",           ysize=600)
image lindan worried           = Transform("images/personagens/moria/lindan_worried.png",           ysize=600)
image lindan worriedtalk       = Transform("images/personagens/moria/lindan_worriedtalk.png",       ysize=600)
image lindan resignedsmile     = Transform("images/personagens/moria/lindan_resignedsmile.png",     ysize=600)
image lindan resignedlaugh     = Transform("images/personagens/moria/lindan_resignedlaugh.png",     ysize=600)
image lindan sweatdrop         = Transform("images/personagens/moria/lindan_sweatdrop.png",         ysize=600)
