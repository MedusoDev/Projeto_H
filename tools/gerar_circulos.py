# -*- coding: utf-8 -*-
"""Gera os PNGs de círculo e anel (brancos, com anti-aliasing) usados pelo
minigame da constelação. O jogo tinge eles da cor necessária via TintMatrix.
Rodar de novo só se quiser mudar tamanho/espessura."""

import math
import os
import struct
import zlib

PASTA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     "game", "images", "minigames", "constelacao")


def salvar_png(caminho, tam, linhas):
    def chunk(tipo, dados):
        return (struct.pack(">I", len(dados)) + tipo + dados
                + struct.pack(">I", zlib.crc32(tipo + dados) & 0xffffffff))

    raw = b"".join(b"\x00" + linha for linha in linhas)
    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", tam, tam, 8, 6, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(raw))
           + chunk(b"IEND", b""))
    with open(caminho, "wb") as f:
        f.write(png)


def desenhar(tam, raio, raio_interno=None):
    """Disco branco (ou anel, se raio_interno) com borda suavizada de 1px."""
    linhas = []
    for y in range(tam):
        linha = bytearray()
        for x in range(tam):
            d = math.hypot(x + 0.5 - tam / 2.0, y + 0.5 - tam / 2.0)
            a = max(0.0, min(1.0, raio - d + 0.5))
            if raio_interno is not None:
                a *= max(0.0, min(1.0, d - raio_interno + 0.5))
            linha += bytes((255, 255, 255, int(a * 255)))
        linhas.append(bytes(linha))
    return linhas


if __name__ == "__main__":
    os.makedirs(PASTA, exist_ok=True)
    salvar_png(os.path.join(PASTA, "circulo.png"), 64, desenhar(64, 30.0))
    salvar_png(os.path.join(PASTA, "anel.png"), 64, desenhar(64, 30.0, 24.0))
    print("Gerados em", PASTA)
