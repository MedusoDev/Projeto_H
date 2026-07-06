# -*- coding: utf-8 -*-
"""
Editor de Constelações — Projeto H
==================================
Janela onde você monta a constelação clicando, e ao salvar ele gera o
arquivo .rpy direto em game/minigames/constelacoes/, pronto pro jogo usar.

Como usar:
    - Duplo clique neste arquivo, ou: python tools/constelacao_editor.py
    - Clique no vazio ........ cria um ponto
    - Arrastar um ponto ...... move
    - Clique num ponto ....... entra/sai da ordem da constelação
                               (o 1º da ordem é o ponto de início, que brilha)
    - Shift + clique ......... num ponto já conectado: vira ponto DUPLO (verde),
                               a linha volta nele e segue pra outro ponto
    - Botão direito .......... apaga o ponto
    - Salvar ................. gera game/minigames/constelacoes/<nome>.rpy

No jogo, é só chamar:  call screen constelacao_minigame(<nome>)
"""

import os
import re
import random
import tkinter as tk
from tkinter import filedialog, messagebox

LARGURA, ALTURA = 1280, 720
RAIO = 9           # raio visual do ponto
RAIO_CLIQUE = 16   # área de acerto do clique

PASTA_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_SAIDA = os.path.join(PASTA_PROJETO, "game", "minigames", "constelacoes")


class EditorConstelacao:
    def __init__(self, raiz):
        self.raiz = raiz
        raiz.title("Editor de Constelações — Projeto H (1280x720)")
        raiz.configure(bg="#0d0f1a")
        raiz.resizable(False, False)

        self.pontos = {}      # id -> (x, y)
        self.ordem = []       # [id, ...] — o 1º é o ponto de início
        self.proximo_id = 1
        self.arrastando = None
        self.moveu = False
        self.tick = 0

        # ---- barra de controles ----
        barra = tk.Frame(raiz, bg="#0d0f1a")
        barra.pack(fill="x", padx=10, pady=8)

        def rotulo(texto):
            return tk.Label(barra, text=texto, bg="#0d0f1a", fg="#aab", font=("Segoe UI", 9))

        rotulo("Nome:").pack(side="left")
        self.ent_nome = tk.Entry(barra, width=22, bg="#1a1d2e", fg="#fff",
                                 insertbackground="#fff", relief="flat")
        self.ent_nome.insert(0, "constelacao_nova")
        self.ent_nome.pack(side="left", padx=(4, 12), ipady=3)

        rotulo("Limite (vazio = auto):").pack(side="left")
        self.ent_limite = tk.Entry(barra, width=5, bg="#1a1d2e", fg="#fff",
                                   insertbackground="#fff", relief="flat")
        self.ent_limite.pack(side="left", padx=(4, 12), ipady=3)

        rotulo("Falsos (sorteados no jogo):").pack(side="left")
        self.ent_fakes = tk.Entry(barra, width=5, bg="#1a1d2e", fg="#fff",
                                  insertbackground="#fff", relief="flat")
        self.ent_fakes.insert(0, "7")
        self.ent_fakes.pack(side="left", padx=(4, 12), ipady=3)

        def botao(texto, comando, cor="#2a3050"):
            b = tk.Button(barra, text=texto, command=comando, bg=cor, fg="#fff",
                          relief="flat", padx=10, pady=3, font=("Segoe UI", 9),
                          activebackground="#3a4270", activeforeground="#fff")
            b.pack(side="left", padx=3)
            return b

        botao("💾 Salvar .rpy", self.salvar)
        botao("📂 Abrir .rpy", self.abrir)
        botao("Limpar ordem", self.limpar_ordem)
        botao("Limpar tudo", self.limpar_tudo, cor="#502a2a")

        # ---- canvas ----
        self.cv = tk.Canvas(raiz, width=LARGURA, height=ALTURA, bg="#05060f",
                            highlightthickness=1, highlightbackground="#333850")
        self.cv.pack(padx=10, pady=(0, 4))
        self.cv.bind("<ButtonPress-1>", self.ao_pressionar)
        self.cv.bind("<B1-Motion>", self.ao_arrastar)
        self.cv.bind("<ButtonRelease-1>", self.ao_soltar)
        self.cv.bind("<ButtonPress-3>", self.ao_botao_direito)

        # ---- status ----
        self.status = tk.Label(raiz, text="Clique no vazio = criar ponto. Clique em ponto = ordem. "
                               "Shift+clique em ponto conectado = ponto duplo (verde).",
                               bg="#0d0f1a", fg="#7f8", font=("Segoe UI", 9), anchor="w")
        self.status.pack(fill="x", padx=10, pady=(0, 8))

        # estrelinhas decorativas fixas do fundo (só visual do editor)
        rng = random.Random(42)
        self.fundo = [(rng.randint(0, LARGURA), rng.randint(0, ALTURA),
                       rng.choice((1, 1, 2)), rng.choice(("#556", "#778", "#99a")))
                      for _ in range(90)]

        self.animar()

    # ------------------------------------------------------------------
    # interação
    # ------------------------------------------------------------------
    def achar_ponto(self, x, y):
        for pid, (px, py) in self.pontos.items():
            if (px - x) ** 2 + (py - y) ** 2 <= RAIO_CLIQUE ** 2:
                return pid
        return None

    def ao_pressionar(self, ev):
        self.arrastando = self.achar_ponto(ev.x, ev.y)
        self.moveu = False
        self.origem = (ev.x, ev.y)

    def ao_arrastar(self, ev):
        if self.arrastando is None:
            return
        ox, oy = self.origem
        if abs(ev.x - ox) > 3 or abs(ev.y - oy) > 3:
            self.moveu = True
        if self.moveu:
            x = min(max(ev.x, 0), LARGURA)
            y = min(max(ev.y, 0), ALTURA)
            self.pontos[self.arrastando] = (x, y)

    def ao_soltar(self, ev):
        shift = bool(ev.state & 0x0001)
        if self.arrastando is not None and not self.moveu:
            pid = self.arrastando
            if shift and pid in self.ordem:
                # Shift+clique em ponto conectado: ligação dupla (verde) —
                # a linha volta nele e segue pro próximo ponto clicado.
                if self.ordem[-1] == pid:
                    self.status.config(text="Esse ponto é o último da ordem — "
                                       "ligue outro antes de voltar nele.")
                else:
                    self.ordem.append(pid)
                    self.status.config(text="Ponto #%d virou ponto duplo (verde): "
                                       "a linha volta nele." % pid)
            elif pid in self.ordem:
                # clique normal: remove a última passagem desse ponto
                for i in range(len(self.ordem) - 1, -1, -1):
                    if self.ordem[i] == pid:
                        del self.ordem[i]
                        break
            else:
                self.ordem.append(pid)
        elif self.arrastando is None and not self.moveu:
            self.pontos[self.proximo_id] = (ev.x, ev.y)
            self.proximo_id += 1
        self.arrastando = None

    def ao_botao_direito(self, ev):
        pid = self.achar_ponto(ev.x, ev.y)
        if pid is not None:
            del self.pontos[pid]
            if pid in self.ordem:
                self.ordem.remove(pid)

    def limpar_ordem(self):
        self.ordem = []

    def limpar_tudo(self):
        if messagebox.askyesno("Limpar tudo", "Apagar todos os pontos?"):
            self.pontos = {}
            self.ordem = []
            self.proximo_id = 1

    # ------------------------------------------------------------------
    # desenho
    # ------------------------------------------------------------------
    def animar(self):
        self.desenhar()
        self.tick += 1
        self.raiz.after(60, self.animar)

    def desenhar(self):
        cv = self.cv
        cv.delete("all")

        for x, y, t, cor in self.fundo:
            cv.create_rectangle(x, y, x + t, y + t, fill=cor, outline="")

        # zona da caixa de referência do jogo (x>1000, y<260)
        cv.create_rectangle(1000, 0, 1280, 260, outline="#553333", dash=(5, 5))
        cv.create_text(1140, 130, text="caixa de\nreferência", fill="#775555",
                       font=("Segoe UI", 10), justify="center")

        # linhas da constelação
        for a, b in zip(self.ordem, self.ordem[1:]):
            x1, y1 = self.pontos[a]
            x2, y2 = self.pontos[b]
            cv.create_line(x1, y1, x2, y2, fill="#ffffff", width=3)

        # pontos
        import math
        for pid, (x, y) in self.pontos.items():
            passagens = [i + 1 for i, v in enumerate(self.ordem) if v == pid]
            if self.ordem and pid == self.ordem[0]:
                # halo pulsante do ponto de início
                r = 18 + 4 * math.sin(self.tick / 5.0)
                cv.create_oval(x - r, y - r, x + r, y + r, outline="#ffe98c", width=2)
            if len(passagens) >= 2:
                cor = "#66dd66"   # ponto duplo: a linha passa nele mais de uma vez
            elif passagens:
                cor = "#ffcc33"
            else:
                cor = "#8899ff"
            cv.create_oval(x - RAIO, y - RAIO, x + RAIO, y + RAIO, fill=cor, outline="")
            cv.create_text(x + 14, y - 12, text="#%d" % pid, fill="#889", font=("Segoe UI", 8))
            if passagens:
                cv.create_text(x + 14, y + 12, text=",".join(map(str, passagens)),
                               fill=cor, font=("Segoe UI", 10, "bold"))

        # contadores
        cv.create_text(12, 12, anchor="nw", fill="#aab", font=("Segoe UI", 10),
                       text="Pontos: %d   |   Na ordem: %d   |   Ligações do desenho: %d"
                            % (len(self.pontos), len(self.ordem), max(0, len(self.ordem) - 1)))

    # ------------------------------------------------------------------
    # salvar / abrir
    # ------------------------------------------------------------------
    def gerar_codigo(self, nome, limite, fakes):
        linhas = ["## Constelação gerada pelo editor (tools/constelacao_editor.py).",
                  "## No jogo: chamar constelacao_preparar(%s) e passar pra tela." % nome,
                  "define %s = {" % nome,
                  '    "pontos": {']
        for pid in sorted(self.pontos):
            x, y = self.pontos[pid]
            linhas.append("        %d: (%d, %d)," % (pid, x, y))
        linhas.append("    },")
        linhas.append('    "ordem": [%s],' % ", ".join(str(i) for i in self.ordem))
        linhas.append('    "limite": %d,' % limite)
        linhas.append('    "fakes": %d,' % fakes)
        linhas.append("}")
        return "\n".join(linhas) + "\n"

    def salvar(self):
        nome = self.ent_nome.get().strip()
        if not re.match(r"^[a-zA-Z_]\w*$", nome):
            messagebox.showerror("Nome inválido",
                                 "O nome precisa ser um identificador válido\n"
                                 "(letras, números e _, sem começar com número).")
            return
        if len(self.ordem) < 2:
            messagebox.showerror("Ordem incompleta",
                                 "Marque pelo menos 2 pontos na ordem da constelação\n"
                                 "(clique nos pontos na sequência do desenho).")
            return
        txt_limite = self.ent_limite.get().strip()
        limite = int(txt_limite) if txt_limite.isdigit() else len(self.ordem) - 1
        txt_fakes = self.ent_fakes.get().strip()
        fakes = int(txt_fakes) if txt_fakes.isdigit() else 0

        os.makedirs(PASTA_SAIDA, exist_ok=True)
        caminho = os.path.join(PASTA_SAIDA, nome + ".rpy")
        if os.path.exists(caminho):
            if not messagebox.askyesno("Sobrescrever?",
                                       "%s.rpy já existe. Sobrescrever?" % nome):
                return

        with open(caminho, "w", encoding="utf-8") as f:
            f.write(self.gerar_codigo(nome, limite, fakes))
        self.status.config(text="Salvo em: %s  —  no jogo: call screen "
                           "constelacao_minigame(%s)" % (caminho, nome))

    def abrir(self):
        os.makedirs(PASTA_SAIDA, exist_ok=True)
        caminho = filedialog.askopenfilename(initialdir=PASTA_SAIDA,
                                             filetypes=[("Ren'Py", "*.rpy")])
        if not caminho:
            return
        with open(caminho, "r", encoding="utf-8") as f:
            txt = f.read()

        pts = re.findall(r"(\d+)\s*:\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)", txt)
        if not pts:
            messagebox.showerror("Erro", "Não achei pontos nesse arquivo.")
            return
        self.pontos = {int(i): (int(x), int(y)) for i, x, y in pts}
        self.proximo_id = max(self.pontos) + 1

        m = re.search(r'"ordem"\s*:\s*\[([^\]]*)\]', txt)
        self.ordem = [int(s) for s in m.group(1).split(",") if s.strip().isdigit()] if m else []

        m = re.search(r'"limite"\s*:\s*(\d+)', txt)
        self.ent_limite.delete(0, "end")
        if m:
            self.ent_limite.insert(0, m.group(1))

        m = re.search(r'"fakes"\s*:\s*(\d+)', txt)
        self.ent_fakes.delete(0, "end")
        self.ent_fakes.insert(0, m.group(1) if m else "0")

        m = re.search(r"define\s+(\w+)\s*=", txt)
        if m:
            self.ent_nome.delete(0, "end")
            self.ent_nome.insert(0, m.group(1))

        self.status.config(text="Carregado: %d pontos, %d na ordem."
                           % (len(self.pontos), len(self.ordem)))


if __name__ == "__main__":
    raiz = tk.Tk()
    EditorConstelacao(raiz)
    raiz.mainloop()
