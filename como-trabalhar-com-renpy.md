# Como trabalhar com Ren'Py — Mini Tutorial

Referência rápida para as tarefas mais comuns do projeto.

---

## 1. Adicionar um novo personagem

Todo personagem precisa de dois passos: **declarar** e **declarar os sprites**.

### 1.1 Declarar o personagem

Abra `game/definicoes/personagens.rpy` e adicione:

```renpy
define nome_variavel = Character("Nome na caixa de diálogo", color="#HEXCOR")
```

Exemplos do projeto:

```renpy
define kimiko = Character("Kimiko", color="#6abf6a")
define moria  = Character("Moria",  color="#e05a30")
```

- `nome_variavel` é o que você vai usar no script para falar (`kimiko "Olá!"`)
- `color` é a cor do nome na caixa de texto (formato hex)

---

### 1.2 Declarar os sprites

Ainda em `personagens.rpy`, adicione uma linha `image` para cada expressão:

```renpy
image tag expressao = Transform("images/personagens/pasta/arquivo.png", ysize=600)
```

- **tag** → identificador do personagem nos comandos `show`/`hide` (ex: `anqian`, `lindan`)
- **expressao** → nome da expressão (ex: `neutral`, `happytalk`, `sad`)
- **ysize=600** → altura padrão em pixels (largura escala automaticamente)

Exemplo completo:

```renpy
image anqian neutral    = Transform("images/personagens/kimiko/anqian_neutral.png",    ysize=600)
image anqian happytalk  = Transform("images/personagens/kimiko/anqian_happytalk.png",  ysize=600)
image anqian sad        = Transform("images/personagens/kimiko/anqian_sad.png",        ysize=600)
```

Depois no script você usa:

```renpy
show anqian neutral at center
with dissolve

kimiko "Olá!"

show anqian happytalk
kimiko "Estou feliz!"
```

---

## 2. Ajustar o tamanho de um sprite

O tamanho é controlado pelo `ysize` no `Transform`. Altere o valor para deixar o personagem maior ou menor:

```renpy
## Personagem menor (ex: criança ou silhueta de fundo)
image anqian neutral = Transform("images/...", ysize=400)

## Personagem padrão
image anqian neutral = Transform("images/...", ysize=600)

## Personagem maior (ocupa a tela inteira)
image anqian neutral = Transform("images/...", ysize=720)
```

> A largura sempre acompanha a proporção original da imagem. Nunca distorce.

Se quiser mudar o tamanho de **todos os sprites de um personagem de uma vez**, basta fazer busca e substituição do valor nos `Transform` daquele personagem em `personagens.rpy`.

---

## 3. Ir para o próximo capítulo

### 3.1 Criar o arquivo do novo capítulo

Crie um novo arquivo `.rpy` dentro de `game/capitulos/`, por exemplo `capitulo01.rpy`:

```renpy
## ---------- Capítulo 1 — Título ----------

label capitulo01_inicio:

    scene bg sala_de_aula
    with fade

    "Texto da cena..."

    jump capitulo01_fim


label capitulo01_fim:

    scene black
    with fade

    "Fim do capítulo 1."

    return
```

### 3.2 Conectar ao capítulo anterior

No final do capítulo anterior, troque o `return` ou adicione um `jump` apontando para o label do novo capítulo:

```renpy
## Em introducao.rpy — label introducao_fim:
label introducao_fim:

    scene black
    with fade

    "Fim da introdução."

    jump capitulo01_inicio  ## ← aponta para o próximo capítulo
```

### 3.3 Regra geral de navegação

| Comando | Quando usar |
|---|---|
| `jump label` | Ir para outro ponto do script (sem retorno) |
| `call label` | Chamar uma cena e voltar depois |
| `return` | Encerrar o jogo ou retornar de um `call` |

> Ren'Py carrega automaticamente todos os `.rpy` dentro de `game/` e subpastas.
> Não é preciso importar arquivos — basta criar e nomear os labels corretamente.

---

## Estrutura atual do projeto

```
game/
├── script.rpy              ← entry point (jump para o primeiro label)
├── capitulos/
│   └── introducao.rpy      ← cena de introdução
├── config/
│   ├── gui.rpy             ← estilo visual da interface
│   └── options.rpy         ← configurações do jogo
├── definicoes/
│   ├── imagens.rpy         ← fundos (bg_*)
│   ├── personagens.rpy     ← define + image de todos os personagens
│   └── variaveis.rpy       ← variáveis globais (afinidade, nome, etc.)
├── telas/
│   └── screens.rpy         ← menus, histórico, saves
└── images/
    ├── bg_sala_de_aula_vazia.png
    └── personagens/
        ├── kimiko/         ← anqian_*.png (14 expressões)
        └── moria/          ← lindan_*.png (22 expressões)
```
