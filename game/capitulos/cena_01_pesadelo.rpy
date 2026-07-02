## ============================================================
## CENA 01 — PESADELO
## Sem sprite. Background: oceano escuro (perspectiva de afundar).
## Pensamentos do protagonista + contato de um ser desconhecido (nome
## sempre embaralhado via tag {glitch}, ver glitch.rpy) que pede o nome do
## jogador. O jogador não vai lembrar disso na Cena 02 — só do pesadelo em
## si, não do "ser".
## ============================================================

label cena_01_pesadelo:

    scene black
    with fade

    ## TODO: trocar por "scene bg oceano_escuro" quando o asset estiver pronto
    ## SFX: play sound "audio/sfx/agua_distante.ogg" loop

    pensamento "Não há mais nada a se fazer..."

    ## Tentáculos verdes surgem — efeito visual a implementar depois
    pensamento "...não há mais nada que eu possa fazer."

    ## ====================================================================
    ## Contato — um ser desconhecido tenta se comunicar. O jogador não vai
    ## se lembrar disso ao acordar (só do pesadelo em si).
    ## ====================================================================

    ser "Alô? Testando?... Sempre erro essa magia maldita..."

    ser "Ahh, agora te vejo!"

    ser "Senhor... qual é seu nome mesmo?"

    $ nome_jogador = renpy.input("Como você se chama?", length=20).strip() or "Estagiário"

    ser "Ahhh, sim... senhor [nome_jogador]."

    ser_glitch "Eu sou {glitch=10}..."

    ser_glitch "Eu preciso que..."

    ## Luz pulsa no centro e corta a cena — o contato é interrompido
    scene black
    with fade

    ## SFX: play sound "audio/sfx/despertador.ogg"

    jump cena_02_quarto
