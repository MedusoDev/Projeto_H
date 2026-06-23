## ============================================================
## CENA 01 — PESADELO
## Sem sprite. Background: oceano escuro (perspectiva de afundar).
## Só narração, pensamentos e SFX.
## ============================================================

label cena_01_pesadelo:

    scene black
    with fade

    ## TODO: trocar por "scene bg oceano_escuro" quando o asset estiver pronto
    ## SFX: play sound "audio/sfx/agua_distante.ogg" loop

    pensamento "Não há mais nada a se fazer..."

    ## Tentáculos verdes surgem — efeito visual a implementar depois
    pensamento "...não há mais nada que eu possa fazer."

    ## Luz pulsa no centro e corta a cena
    scene black
    with fade

    ## SFX: play sound "audio/sfx/despertador.ogg"

    jump cena_02_quarto
