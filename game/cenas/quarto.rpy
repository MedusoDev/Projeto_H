## ============================================================
## cenas/quarto.rpy — Cena inicial: quarto do protagonista
## ============================================================

## ---------- Imagem de fundo ----------

image bg quarto = "images/bg_room/quarto_cortina_fechada_luz_ligada.jpg"


## ---------- Labels da cena ----------

label cena_quarto:

    call screen quarto

    ## Pergunta se o jogador está pronto para ir
    menu:
        "Pronto para ir?"

        "Sim, vamos lá.":
            pass

        "Ainda não.":
            jump cena_quarto

    "Bom, alguém tem que trabalhar."

    jump introducao_inicio
