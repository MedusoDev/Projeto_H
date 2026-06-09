## ============================================================
## cenas/quarto.rpy — Cena inicial: quarto do protagonista
## ============================================================
## O jogador explora o quarto antes de sair para trabalhar.
## Pode clicar em objetos para ver pensamentos do personagem
## e no interruptor para alternar a iluminação.
## Ao clicar na área inferior, avança para a próxima cena.
## ============================================================


## ---------- Imagens de fundo ----------

image bg quarto_dia = "images/bg_room/pra_a1_day1.png"
image bg quarto_luz = "images/bg_room/pra_a1_day2.png"


## ---------- Variáveis de estado ----------
##
## quarto_iluminacao: qual versão do fundo está visível
## quarto_mensagem:   texto flutuante exibido ao clicar em objetos

default quarto_iluminacao = "dia"
default quarto_mensagem   = ""


## ---------- Screen do quarto ----------
##
## Usamos "call screen" no label, então a screen PAUSA o script
## enquanto o jogador explora. Só avança quando ele clicar na
## área de sair (botão inferior), que executa Return().
##
## SetVariable("quarto_mensagem", "...") troca o texto flutuante.
## ToggleVariable alterna entre dois valores a cada clique.
## O Ren'Py re-renderiza a screen automaticamente ao mudar variáveis.

screen tela_quarto():

    ## ---- Fundo dinâmico ----
    if quarto_iluminacao == "dia":
        add "bg quarto_dia"
    else:
        add "bg quarto_luz"

    ## ---- Caixa de mensagem flutuante ----
    ##
    ## Aparece no rodapé sempre que quarto_mensagem não estiver vazia.
    ## Clicar em outro objeto substitui a mensagem automaticamente.

    if quarto_mensagem:
        frame:
            xalign  0.5
            ypos    860
            xsize   1700
            padding (50, 25)
            background Solid("#000000bb")
            text quarto_mensagem:
                xalign 0.5
                color  "#ffffff"
                size   38

    ## ---- Interruptor de luz ----
    ##
    ## ToggleVariable alterna entre "dia" e "luz" a cada clique.
    ## Isso troca o fundo acima instantaneamente.

    button:
        xpos 1849  ypos 513  xsize 38  ysize 78
        background       None
        hover_background Solid("#ffff0044")
        action ToggleVariable("quarto_iluminacao", "dia", "luz")

    ## ---- Livros ----

    button:
        xpos 1470  ypos 502  xsize 137  ysize 71
        background       None
        hover_background Solid("#ffffff33")
        action SetVariable("quarto_mensagem",
            "Estudou bastante para finalmente poder dar aula.")

    ## ---- Janela principal ----

    button:
        xpos 997  ypos 257  xsize 269  ysize 304
        background       None
        hover_background Solid("#ffffff33")
        action SetVariable("quarto_mensagem",
            "Está um bom dia para ficar em casa... mas precisa trabalhar.")

    ## ---- Segunda janela ----

    button:
        xpos 1490  ypos 147  xsize 268  ysize 327
        background       None
        hover_background Solid("#ffffff33")
        action SetVariable("quarto_mensagem",
            "Melhor deixar fechada para a fada não pegar o doce.")

    ## ---- Cama ----

    button:
        xpos 184  ypos 533  xsize 721  ysize 350
        background       None
        hover_background Solid("#ffffff33")
        action SetVariable("quarto_mensagem",
            "Vou arrumar quando chegar.")

    ## ---- Área de saída (parte inferior) ----
    ##
    ## Return() encerra o "call screen" e devolve o controle ao label.
    ## O hover mais visível serve de dica visual para o jogador.

    button:
        xpos 568  ypos 911  xsize 879  ysize 88
        background       None
        hover_background Solid("#ffffff22")
        action Return()


## ---------- Label da cena ----------

label cena_quarto:

    ## Reinicia o estado a cada vez que a cena é carregada
    $ quarto_iluminacao = "dia"
    $ quarto_mensagem   = ""

    ## "call screen" pausa o script e mostra a tela interativa.
    ## O jogador explora livremente até clicar na área de saída.
    call screen tela_quarto

    ## Diálogo exibido após o jogador decidir sair
    "Já vai?"
    "Bom, alguém tem que trabalhar."

    jump introducao_inicio
