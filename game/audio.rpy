init -1 python:
    renpy.music.register_channel("ambience", mixer="sfx", loop=True)
    renpy.music.register_channel("ambience2", mixer="sfx", loop=True)
    renpy.music.register_channel("tictac", mixer="sfx", loop=True)
    renpy.music.register_channel("typing", mixer="sfx", loop=True)

    ## Blip de digitação — toca em loop enquanto o texto está digitando
    ## (letra por letra) e para quando a fala termina de aparecer.
    ## text_blip.wav é um placeholder sintético (~7 ticks/s); pra trocar o
    ## som, basta substituir o arquivo mantendo o nome.
    ## Registrado como callback global (config.character_callback), então
    ## vale pra TODOS os personagens sem precisar mexer nos defines.
    def blip_callback(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.music.play("audio/text_blip.wav", channel="typing", loop=True)
        elif event in ("slow_done", "end"):
            renpy.music.stop(channel="typing")

    config.character_callback = blip_callback