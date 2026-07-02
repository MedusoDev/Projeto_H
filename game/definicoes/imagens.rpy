## ---------- Fundos ----------

image bg sala_de_aula   = im.Scale("images/bg_sala_de_aula_vazia.png", 1280, 720)
image bg quarto_day     = im.Scale("images/background/room_full.png", 1280, 720)
image bg quarto_no_fone = im.Scale("images/background/room_no_fone.png", 1280, 720)

## TODO: adicionar bg oceano_escuro para a Cena 01 (Pesadelo)


## ---------- Hotspots — Quarto (Cena 02) ----------
## fixos/     -> permanecem clicáveis em qualquer variante do bg, sem trocar a cena
## coletaveis/ -> somem ao serem usados e trocam o bg permanentemente


## -------- Fixos

image hs_fixo_losa        = im.Scale("images/hotspots/room/fixos/room_full_losa.png",        1280, 720)
image hs_fixo_losa_hover  = im.Scale("images/hotspots/room/fixos/room_full_losa_hover.png",  1280, 720)

image hs_fixo_foto        = im.Scale("images/hotspots/room/fixos/room_full_picture.png",        1280, 720)
image hs_fixo_foto_hover  = im.Scale("images/hotspots/room/fixos/room_full_picture_hover.png",  1280, 720)

image hs_fixo_bed         = im.Scale("images/hotspots/room/fixos/room_full_bed.png",        1280, 720)
image hs_fixo_bed_hover   = im.Scale("images/hotspots/room/fixos/room_full_bed_hover.png",  1280, 720)

image hs_fixo_clock       = im.Scale("images/hotspots/room/fixos/room_full_clock.png",     1280,720)
image hs_fixo_clock_hover = im.Scale("images/hotspots/room/fixos/room_full_clock_hover.png",   1280,720)

image hs_fixo_stone       = im.Scale("images/hotspots/room/fixos/room_full_stone.png",     1280,720)
image hs_fixo_stone_hover = im.Scale("images/hotspots/room/fixos/room_full_stone_hover.png",     1280,720)
## ------- Coletaveis

image hs_item_wand        = im.Scale("images/hotspots/room/coletaveis/room_full_wand.png",       1280, 720)
image hs_item_wand_hover  = im.Scale("images/hotspots/room/coletaveis/room_full_wand_hover.png", 1280, 720)

image hs_item_fone        = im.Scale("images/hotspots/room/coletaveis/room_full_fone.png",       1280, 720)
image hs_item_fone_hover  = im.Scale("images/hotspots/room/coletaveis/room_full_fone_hover.png", 1280, 720)

image hs_item_jaleco      = im.Scale("images/hotspots/room/coletaveis/room_full_jaleco.png", 1280, 720)
image hs_item_jaleco_hover= im.Scale("images/hotspots/room/coletaveis/room_full_jaleco_hover.png", 1280, 720)

image hs_item_box      = im.Scale("images/hotspots/room/coletaveis/room_full_box.png", 1280, 720)
image hs_item_box_hover= im.Scale("images/hotspots/room/coletaveis/room_full_box_hover.png", 1280, 720)
