import action
import globs
import initgame
import tools


def menu():
    tools.display(globs.strings['start']['welcome'])
    tools.display(globs.strings['start']['start_options'])

    option = input("º > ")
    if option == '1': # Cargar partida
        loadgame_action = action.LoadGame()
        loadgame_action.execute()
    elif option == '2': # Nueva partida
        tools.display(globs.strings['start']['player_name_prompt'])
        player_name = input("ª > ")
        print("test")
        initgame.newgame(language='es', player_name=player_name)
    else:
        loadgame_action = action.LoadGame()
        loadgame_action.execute()