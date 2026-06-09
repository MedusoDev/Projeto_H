## ---------- Introdução — Primeiro Contato ----------
## Convenção de sprites:
##   - variante "talk"  → personagem está falando a linha
##   - variante estática → reação silenciosa / escutando

label introducao_inicio:

    scene bg sala_de_aula
    with fade

    ## ====================================================================
    ## Bloco 1 — O professor chega na sala vazia
    ## ====================================================================

    "O sol da manhã jorra pelas janelas entreabertas da sala 7-B."
    "A diretora foi direta: 'Chegue cedo e organize antes das alunas chegarem.'"
    "Uma olhada rápida ao redor explica o que ela quis dizer."

    menu:
        "Carteiras reviradas, quadro riscado, papéis no chão. Um caos completo.":
            "Você empurra uma carteira com o pé e suspira fundo."
            "— Organizar. Claro. Só isso."
        "Já vi pior. Muito pior.":
            "Você começa a arrumar com uma calma quase perturbadora."
            "Trabalhou em lugares difíceis. Isso aqui é domável."
        "A diretora chamou isso de sala de aula. Parece mais um depósito abandonado.":
            "Você murmura baixinho enquanto recolhe papéis do chão."
            "Uma ordem é uma ordem, afinal."

    "Quinze minutos depois, a sala está em condições aceitáveis."
    "Você se encosta na mesa da frente, braços cruzados."
    "— Pelo menos fiz algo útil antes do primeiro dia começar de verdade."

    ## ====================================================================
    ## Bloco 2 — Kimiko entra
    ## ====================================================================

    "A porta se abre com um rangido agudo."

    show anqian happytalk at center
    with dissolve

    kimiko "Ei! Oi! Alguém aí?"

    show anqian neutraltalk
    kimiko "Você deve ser o novo estagiário que a diretora mencionou, né?"

    menu:
        "Sim. Cheguei cedo pra organizar um pouco.":
            show anqian happysmile
            kimiko "Caramba, dedicado já no primeiro dia!"
            show anqian happytalk
            kimiko "Isso é raro por aqui, saiba."
        "Prefiro 'professor substituto', mas tudo bem...":
            show anqian sweatdrop
            kimiko "O-oh! Desculpa! A diretora falou 'estagiário' e eu assumi que..."
            show anqian nervouslaugh
            kimiko "Não quis ofender, juro."

    show anqian smile
    kimiko "Mas espera — eu nem perguntei o seu nome! Qual é?"

    $ nome_jogador = renpy.input("Como você se chama?", length=20).strip() or "Estagiário"

    show anqian happytalk
    kimiko "[nome_jogador]! Que nome legal!"

    show anqian happysmile
    kimiko "Eu sou a Kimiko. Centopeia mágica — muito prazer!"

    jogador "Centopeia? Nunca trabalhei com uma antes."

    show anqian neutraltalk
    kimiko "Sério? E com que tipo de criatura você trabalhou antes de vir pra cá?"

    menu:
        "Nunca trabalhei com criaturas mágicas. Essa é minha primeira escola assim.":
            show anqian sweatdrop
            kimiko "Nossa! De verdade?"
            show anqian happytalk
            kimiko "Então prepare-se — aqui é bem intenso. No bom sentido!"
        "Trabalhei com fadas uma vez. Panda vermelho e centopeia são novidade.":
            show anqian happytalk
            kimiko "Fadas! Elas são terríveis com pontualidade, não são?"
            show anqian smile
            kimiko "A gente aqui é mais confiável. Na maioria das vezes."
        "Trabalhei em escolas convencionais. Criaturas mágicas são novidade total.":
            show anqian neutraltalk
            kimiko "Escola convencional... então você deve estranhar bastante coisa aqui."
            show anqian happysmile
            kimiko "Mas não precisa se preocupar! A gente te ajuda a se acostumar."

    show anqian neutraltalk
    kimiko "E você, [nome_jogador]? Usa algum tipo de magia?"

    menu:
        "Uso magia de suporte — reforço e escudos principalmente.":
            $ afinidade_kimiko += 1
            show anqian happytalk
            kimiko "Magia de suporte! Sempre subestimada, mas absolutamente indispensável."
            show anqian happysmile
            kimiko "Aqui vão valorizar muito isso. Pode ter certeza."
        "Tenho afinidade elemental. Fogo, principalmente.":
            show anqian sweatdrop
            kimiko "Fogo? Cuidado com as cortinas, então."
            show anqian happytalkclosed
            kimiko "Brincadeira! Mais ou menos."
        "Honestamente? Minha área forte é pedagogia, não magia.":
            show anqian sweatdrop
            kimiko "Um professor sem magia forte numa escola mágica?"
            show anqian happytalk
            kimiko "Corajoso. Respeito muito isso."

    ## ====================================================================
    ## Bloco 3 — Moria entra
    ## ====================================================================

    "A porta volta a ranger."

    show anqian happytalk at right
    with move

    show lindan neutral at left
    with dissolve

    show lindan neutraltalk
    moria "..."

    show anqian happytalk
    kimiko "Moria! Chegou bem na hora."

    show lindan neutral
    moria "Cheguei no horário."

    show anqian happytalk
    kimiko "Exatamente o que eu disse!"

    show lindan serious
    moria "..."

    show lindan neutraltalk
    moria "Quem é esse?"

    show anqian happytalk
    kimiko "Ah! Esse é o [nome_jogador]. Professor novo da turma."

    show lindan neutraltalk
    moria "[nome_jogador]..."

    show lindan surprised
    moria "Parece jovem demais pra ser professor."

    menu:
        "Estagiário, tecnicamente. Mas pretendo me provar.":
            $ afinidade_moria += 1
            show lindan serious
            moria "Hm."
            show lindan smile
            moria "...Honesto. Gosto disso."
        "As aparências enganam. Tenho mais experiência do que pareço ter.":
            show lindan neutraltalk
            moria "Quanto mais?"
            show anqian worried
            kimiko "Moria! Não é educado perguntar isso!"
            show lindan nervoussmile
            moria "...Verdade. Desculpe."
        "Eu também não esperava que a aluna fosse um panda vermelho, então estamos quites.":
            $ afinidade_moria += 1
            show lindan surprisedtalk
            moria "..."
            show lindan challengingsmile
            moria "...Justo."

    show anqian happytalk
    kimiko "Moria é panda vermelho. Não deixa a carinha séria te enganar — ela é incrivelmente inteligente."

    show lindan serioustalk
    moria "Você faz isso parecer difícil de admitir."

    show anqian sweatdrop
    kimiko "Não é nada disso!"

    show lindan neutraltalk
    moria "..."

    show lindan nervoussmile
    moria "...Era mesmo um elogio?"

    show anqian happytalk
    kimiko "Claro que era, Moria!"

    jogador "Vocês duas se conhecem há muito tempo?"

    show lindan neutraltalk
    moria "Dois anos."

    show anqian happytalk
    kimiko "Dois anos e ela ainda não sabe quando estou sendo séria ou brincando."

    show lindan serioustalk
    moria "...Você quase nunca parece séria."

    show anqian sadtalk
    kimiko "Isso machuca, Moria."

    show lindan sad
    moria "..."

    show lindan nervousgrin
    moria "...Um pouco machuca, sim. Me desculpe."

    show anqian happytalkclosed
    kimiko "Estou brincando! Metade do tempo."

    jogador "É bom ver que vocês se entendem bem."

    show lindan neutraltalk
    moria "Nos toleramos bem."

    show anqian worried
    kimiko "TOLERAMOS?!"

    show lindan laugh
    moria "..."

    "Você nota que o canto da boca de Moria se curva por um segundo."

    show lindan resignedsmile
    moria "...Nos entendemos bem. É o que eu quis dizer."

    ## ====================================================================
    ## Bloco 4 — O sinal toca
    ## ====================================================================

    "Um longo sinal ecoa pelos corredores."
    "O início das aulas."

    show anqian happytalk
    kimiko "Já?! Nem vi o tempo passar!"

    show lindan serious
    moria "Vamos sentar."

    show anqian neutral
    kimiko "Boa sorte hoje, professor [nome_jogador]!"

    show lindan neutral
    moria "..."

    show lindan smile
    moria "...Boa sorte."

    hide anqian
    hide lindan
    with dissolve

    "Você olha para as carteiras agora ocupadas."
    "É assim que começa."
    "Seu primeiro dia de verdade."

    jump introducao_fim


label introducao_fim:

    scene black
    with fade

    "Fim da introdução."

    return
