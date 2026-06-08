## ---------- Capitulo 1 — Primeiro dia ----------

label capitulo01_abertura:

    scene bg sala_de_aula
    with fade

    "O primeiro dia. A sala de aula parecia maior do que o esperado."
    "Carteiras enfileiradas, janelas abertas, o cheiro de livros novos no ar."
    "Você entra devagar, olhando ao redor — e então a vê."

    show gwendolyn animada at center
    with dissolve

    gwendolyn "Oh! Um rosto novo!"
    gwendolyn "Que bom que chegou. Eu sou a Professora Gwendolyn."

    show gwendolyn neutra
    gwendolyn "E você? Como você se chama?"

    $ nome_jogador = renpy.input("Como você se chama?", length=20).strip() or "Sem nome"

    show gwendolyn animada
    gwendolyn "Que nome bonito! [nome_jogador], seja bem-vindo!"
    gwendolyn "Espero que goste das minhas aulas."

    show gwendolyn neutra
    gwendolyn "O que acha de começarmos hoje mesmo?"

    menu:
        "Mal posso esperar! Adoro aprender.":
            $ afinidade_gwendolyn += 2
            show gwendolyn animada
            gwendolyn "Haha! Que entusiasmo maravilhoso!"
            gwendolyn "Com esse ânimo, vai longe, [nome_jogador]!"

        "Vamos ver como vai ser...":
            show gwendolyn neutra
            gwendolyn "Hm... reservado, hein?"
            gwendolyn "Tudo bem. As coisas falam por si mesmas."

        "Honestamente? Não gosto muito de aulas.":
            $ afinidade_gwendolyn -= 1
            show gwendolyn triste
            gwendolyn "..."
            gwendolyn "Bom... espero mudar sua opinião com o tempo."

    jump capitulo01_fim


label capitulo01_fim:

    show gwendolyn neutra
    "A aula está prestes a começar."
    "O que esse dia vai reservar?"

    return
