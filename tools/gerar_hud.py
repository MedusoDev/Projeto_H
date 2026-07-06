# -*- coding: utf-8 -*-
"""Gera a HUD "clean" do jogo: painéis escuros translúcidos com cantos
arredondados e borda sutil, no lugar da arte preto+dourado do template.

Gera (sobrescreve) em game/gui/:
    textbox.png                       1280x185 — caixa de diálogo
    namebox.png                       300x36   — pílula do nome
    frame.png                         96x96    — frame genérico (confirm etc.)
    button/choice_idle_background.png 240x48   — opção de menu
    button/choice_hover_background.png

Rodar de novo pra ajustar cores/medidas. Os originais do template ficam no
histórico do git."""

import math
import os
import struct
import zlib

GUI = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "game", "gui")

## Paleta (mesma família do céu do minigame: noite + acento periwinkle)
PAINEL = (13, 16, 26, 216)          # fundo do painel
PAINEL_SOLIDO = (13, 16, 26, 240)
BORDA_SUTIL = (255, 255, 255, 26)   # contorno quase invisível
ACENTO = (143, 180, 255, 110)       # periwinkle
NAME_FILL = (28, 36, 60, 235)
CHOICE_IDLE = (17, 21, 36, 205)
CHOICE_HOVER = (26, 32, 54, 228)


def salvar_png(caminho, w, h, linhas):
    def chunk(tipo, dados):
        return (struct.pack(">I", len(dados)) + tipo + dados
                + struct.pack(">I", zlib.crc32(tipo + dados) & 0xffffffff))

    raw = b"".join(b"\x00" + bytes(l) for l in linhas)
    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(raw))
           + chunk(b"IEND", b""))
    with open(caminho, "wb") as f:
        f.write(png)
    print("ok:", os.path.relpath(caminho, GUI))


def _clamp01(v):
    return 0.0 if v < 0.0 else (1.0 if v > 1.0 else v)


def painel(caminho, w, h, raio, fill, borda, esp=1.5, margem=(0, 0, 0, 0), externo=None):
    """Retângulo arredondado anti-serrilhado (SDF) com borda, centrado na
    área do canvas descontadas as margens (esq, topo, dir, baixo). Se
    "externo" for dado, a área fora do painel recebe essa cor (senão fica
    transparente)."""
    ml, mt, mr, mb = margem
    cx = (ml + w - mr) / 2.0
    cy = (mt + h - mb) / 2.0
    bx = (w - ml - mr) / 2.0 - raio
    by = (h - mt - mb) / 2.0 - raio

    linhas = []
    for y in range(h):
        row = bytearray()
        for x in range(w):
            px = abs(x + 0.5 - cx) - bx
            py = abs(y + 0.5 - cy) - by
            qx = px if px > 0 else 0.0
            qy = py if py > 0 else 0.0
            d = math.hypot(qx, qy) + min(max(px, py), 0.0) - raio

            forma = _clamp01(0.5 - d)             # cobertura total da forma
            interior = _clamp01(0.5 - (d + esp))  # cobertura sem a borda
            af = fill[3] / 255.0 * interior
            ab = borda[3] / 255.0 * (forma - interior)
            ae = (externo[3] / 255.0 * (1.0 - forma)) if externo else 0.0
            a = af + ab + ae
            if a <= 0.0:
                row += b"\x00\x00\x00\x00"
                continue
            er, eg, eb = (externo[0], externo[1], externo[2]) if externo else (0, 0, 0)
            r = int((fill[0] * af + borda[0] * ab + er * ae) / a)
            g = int((fill[1] * af + borda[1] * ab + eg * ae) / a)
            b = int((fill[2] * af + borda[2] * ab + eb * ae) / a)
            row += bytes((r, g, b, int(a * 255)))
        linhas.append(row)
    salvar_png(caminho, w, h, linhas)


def chapado(caminho, w, h, cor):
    """Canvas inteiro numa cor só (RGBA)."""
    row = bytes(cor) * w
    salvar_png(caminho, w, h, [row] * h)


def fundo_estrelado(caminho, w=1280, h=720, qtd=150, seed=7, estrelas=True,
                    topo=(5, 8, 17), base=(13, 19, 34)):
    """Gradiente vertical noturno com (opcionalmente) estrelas estáticas."""
    import random
    pontos = {}
    if estrelas:
        rng = random.Random(seed)
        cores = [(255, 255, 255), (255, 255, 255), (200, 215, 255),
                 (143, 180, 255), (255, 233, 200)]
        for _ in range(qtd):
            x = rng.randint(0, w - 2)
            y = rng.randint(0, h - 2)
            t = rng.choice([1, 1, 1, 2, 2])
            cor = rng.choice(cores)
            a = rng.randint(70, 210) / 255.0
            for dx in range(t):
                for dy in range(t):
                    pontos[(x + dx, y + dy)] = (cor, a)

    linhas = []
    for y in range(h):
        f = y / float(h - 1)
        rb = topo[0] + (base[0] - topo[0]) * f
        gb = topo[1] + (base[1] - topo[1]) * f
        bb = topo[2] + (base[2] - topo[2]) * f
        row = bytearray()
        for x in range(w):
            p = pontos.get((x, y))
            if p:
                (cr, cg, cb), a = p
                row += bytes((int(cr * a + rb * (1 - a)),
                              int(cg * a + gb * (1 - a)),
                              int(cb * a + bb * (1 - a)), 255))
            else:
                row += bytes((int(rb), int(gb), int(bb), 255))
        linhas.append(row)
    salvar_png(caminho, w, h, linhas)


def linha_decorativa(caminho, w, h, x0, x1, y0, esp, cor):
    """Canvas transparente com uma linha horizontal que esvanece nas pontas."""
    fade = (x1 - x0) * 0.25
    linhas = []
    for y in range(h):
        row = bytearray()
        for x in range(w):
            if y0 <= y < y0 + esp and x0 <= x < x1:
                t = min(x - x0, x1 - 1 - x) / fade
                a = int(cor[3] * _clamp01(t))
                row += bytes((cor[0], cor[1], cor[2], a))
            else:
                row += b"\x00\x00\x00\x00"
        linhas.append(row)
    salvar_png(caminho, w, h, linhas)


if __name__ == "__main__":
    ## Caixa de diálogo: painel com respiro nas laterais e embaixo
    painel(os.path.join(GUI, "textbox.png"), 1280, 185, 18,
           PAINEL, BORDA_SUTIL, margem=(120, 8, 120, 10))

    ## Pílula do nome
    painel(os.path.join(GUI, "namebox.png"), 300, 36, 17,
           NAME_FILL, ACENTO)

    ## Frame genérico (confirm, etc.)
    painel(os.path.join(GUI, "frame.png"), 96, 96, 18,
           PAINEL_SOLIDO, BORDA_SUTIL)

    ## Botões de escolha
    pasta_botao = os.path.join(GUI, "button")
    painel(os.path.join(pasta_botao, "choice_idle_background.png"), 240, 48, 14,
           CHOICE_IDLE, BORDA_SUTIL)
    painel(os.path.join(pasta_botao, "choice_hover_background.png"), 240, 48, 14,
           CHOICE_HOVER, (143, 180, 255, 140))
