# Projeto H

Visual novel em desenvolvimento feita com **Ren'Py**.

---

## Sobre o projeto

Projeto H é uma visual novel narrativa com sistema de escolhas, múltiplas rotas e personagens com reações dinâmicas baseadas nas decisões do jogador.

> Projeto em fase inicial de desenvolvimento.

---

## O que é necessário para rodar

### 1. Ren'Py SDK
O motor do jogo. Faça o download em:

**https://www.renpy.org/latest.html**

- Baixe a versão para **Windows**
- Extraia em qualquer pasta
- Abra o **Ren'Py Launcher**
- Clique em **"Preferences"** → **"Projects Directory"** e aponte para a pasta onde este repositório foi clonado
- O projeto `Projeto H` vai aparecer na lista — clique em **"Launch Project"** para rodar

### 2. Git
Para clonar e contribuir com o repositório:

**https://git-scm.com/downloads**

---

## Extensões recomendadas para VSCode

Se for editar o código no **Visual Studio Code**, instale a extensão:

| Extensão | Autor | Função |
|---|---|---|
| **Ren'Py Language** | LuqueDaniel | Syntax highlight e suporte completo a arquivos `.rpy` |

Para instalar: `Ctrl+Shift+X` → pesquise por `Ren'Py Language`

---

## Estrutura do projeto

```
game/
├── script.rpy          # Ponto de entrada do jogo
├── personagens.rpy     # Definição dos personagens e sprites
├── imagens.rpy         # Definição dos fundos e cenários
├── variaveis.rpy       # Flags e sistema de afinidade
├── capitulo01.rpy      # Capítulo 1 — Primeiro dia
├── options.rpy         # Configurações gerais do jogo
├── screens.rpy         # Interface do usuário
├── gui.rpy             # Estilo visual da interface
└── images/
    ├── bg/             # Fundos e cenários
    └── personagens/    # Sprites dos personagens por expressão
```

---

## Como clonar o repositório

```bash
git clone https://github.com/MedusoDev/Projeto_H.git
```

---

## Tecnologias

- [Ren'Py](https://www.renpy.org/) — engine de visual novel baseada em Python
