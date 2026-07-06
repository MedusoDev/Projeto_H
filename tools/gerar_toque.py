# -*- coding: utf-8 -*-
"""Gera game/audio/phone_ring.wav — toque de telefone sintético (placeholder).
Padrão clássico: dois tons somados (440 + 480 Hz) com tremolo, 1.2s tocando
e 2.3s de silêncio por ciclo (o jogo toca em loop). Pra trocar por um toque
real depois, basta substituir o arquivo mantendo o nome."""

import math
import os
import struct
import wave

TAXA = 44100
DESTINO = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "game", "audio", "phone_ring.wav")


def gerar():
    amostras = []

    def tom(duracao):
        n = int(TAXA * duracao)
        borda = int(TAXA * 0.012)  # rampa anti-clique
        for i in range(n):
            t = i / float(TAXA)
            v = 0.5 * (math.sin(2 * math.pi * 440 * t) + math.sin(2 * math.pi * 480 * t))
            v *= 0.75 + 0.25 * math.sin(2 * math.pi * 20 * t)  # tremolo de campainha
            if i < borda:
                v *= i / float(borda)
            elif i > n - borda:
                v *= (n - i) / float(borda)
            amostras.append(int(v * 0.42 * 32767))

    def silencio(duracao):
        amostras.extend([0] * int(TAXA * duracao))

    tom(1.2)
    silencio(2.3)

    with wave.open(DESTINO, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(TAXA)
        w.writeframes(struct.pack("<%dh" % len(amostras), *amostras))
    print("Gerado:", DESTINO, "(%.1fs)" % (len(amostras) / float(TAXA)))


if __name__ == "__main__":
    gerar()
