## ---------- Personagens ----------

## Jogador — nome inserido pelo jogador na tela de nome
## image="protagonista" liga este Character ao layeredimage abaixo, permitindo
## a forma curta `jogador neutral talk "Frase."` para trocar a expressão e
## falar na mesma linha (mostra o sprite automaticamente se ainda não estiver em cena).
define jogador     = Character("[nome_jogador]", color="#e0e0ff", image="protagonista")
define pensamento  = Character(None, what_italic=True, what_color="#b0b0c8")

## Pai do protagonista — só voz (ligação na Cena 03).
define pai = Character("Pai", color="#d8b060")

## Ser misterioso — contato na Cena 01 (Pesadelo). Sem sprite, só voz.
## Nome = bloco glitch de 7 chars animado (tag {glitch=N}, ver glitch.rpy).
## Falas em vermelho (what_color).
define ser        = Character("{glitch=7}", what_color="#e02020")

## Igual, mas usado nas linhas em que a fala do ser também é corrompida
## (embaralhada com a tag {glitch=N} dentro do próprio texto).
define ser_glitch = Character("{glitch=7}", what_color="#e02020")

## -----------------------------------------------------------------------
## Protagonista — sprite em camadas (pose + expressões avulsas)
## Sprites: images/personagens/protagonista/
## arms_free.png é a pose padrão (rosto em branco); arms_pensativo.png para
## momentos de reflexão (ex: mexendo no computador/checklist).
## eyebrows_*/mouth_*/sweat.png encaixam por cima, todos no mesmo canvas
## (sem necessidade de offset).
## -----------------------------------------------------------------------

layeredimage protagonista:
    group pose:
        attribute arms_free default:
            "images/personagens/protagonista/arms_free.png"
        attribute arms_pensativo:
            "images/personagens/protagonista/arms_pensativo.png"

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
## Close-up — mão com o celular (Cena 02, ao pegar o telefone)
## Composto: a arte da mão (373x669) + o horário centralizado por cima da
## tela do celular (bbox da tela em pixels da arte original: x 132-260,
## y 154-438 -> centro em 196,296).
## -----------------------------------------------------------------------
image protagonista_celular_hora = Fixed(
    Image("images/personagens/protagonista/protagonista_celular_wand.png"),
    Text("7:12", xpos=196, ypos=296, xanchor=0.5, yanchor=0.5, size=48, bold=True, color="#1a1a1a", font="gui/font/Jost-Light.ttf"),
    xysize=(373, 669),
)

transform celular_hora_size:
    ysize 650
    align (0.5, 0.62)

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
