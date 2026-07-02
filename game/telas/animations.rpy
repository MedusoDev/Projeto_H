## ---------- Animações da GUI (GUITEMPLATE) ----------
## Transforms usados pela tela main_menu (botões deslizando ao aparecer)
## e pelos botões de página das telas de salvar/carregar.

transform page_button_left():
    subpixel True
    yalign 0.5
    xpos 40
    linear 1.0 xpos 30
    linear 1.0 xpos 40
    repeat

transform page_button_right():
    subpixel True
    yalign 0.5
    xpos 1217
    linear 1.0 xpos 1227
    linear 1.0 xpos 1217
    repeat

transform button1():
    subpixel True
    alpha 0.0
    xpos -33
    linear 0.5 xpos 0 alpha 1.0

transform button2():
    subpixel True
    alpha 0.0
    xpos -33
    pause 0.2
    linear 0.5 xpos 0 alpha 1.0

transform button3():
    subpixel True
    alpha 0.0
    xpos -33
    pause 0.4
    linear 0.5 xpos 0 alpha 1.0

transform button4():
    subpixel True
    alpha 0.0
    xpos -33
    pause 0.6
    linear 0.5 xpos 0 alpha 1.0

transform button5():
    subpixel True
    alpha 0.0
    xpos -33
    pause 0.8
    linear 0.5 xpos 0 alpha 1.0

transform button6():
    subpixel True
    alpha 0.0
    xpos -33
    pause 1.0
    linear 0.5 xpos 0 alpha 1.0
