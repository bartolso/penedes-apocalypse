import globs
import initgame
import tools
import action
import menu

import os

def parse_command(command):
    tokens = command.lower().split()
    #if len(tokens) < 2:
        #tools.display('Comando inválido')
        #raise ValueError

    cmd_action = tokens[0]
    cmd_arguments = tokens[1:]

    return cmd_action, cmd_arguments


def handle_command(command):
    try:
        if parse_command is not None:
            cmd_action, arguments = parse_command(command)
            if cmd_action == 'ir' and len(arguments) == 1:
                direction = arguments[0]
                move_action = action.Move(direction)
                move_action.execute(globs.player)
            elif cmd_action == 'examinar' and len(arguments) == 1:
                thing = arguments[0]
                examine_action = action.Examine(thing)
                examine_action.execute(globs.player)
            elif cmd_action == 'guardar' and len(arguments) == 0:
                savegame_action = action.SaveGame()
                savegame_action.execute()
            elif cmd_action == 'cargar' and len(arguments) == 0:
                loadgame_action = action.LoadGame()
                loadgame_action.execute()
            else:
                tools.display("Argumentos inválidos!")
    except ValueError as e:
        tools.display(e)


def main():
    tools.display('══════════════════')
    tools.display('PENEDÈS APOCALYPSE')
    tools.display('══════════════════')
    
    # inicializar juego
    initgame.newgame(language='es', player_name='setup')
    menu.menu()
    # ...
    game_loop()


def game_loop():
    tools.clear_terminal()
    while True:
        if globs.player: # esto solo sive para que globs.player no de error ya que es None según vscode pero no según pycharm.
            tools.display('estás en ' + globs.player.location.name)  
        else:
            pass
        user_input = input('- > ')
        tools.clear_terminal()

        
        handle_command(user_input)


if __name__ == '__main__':
    main()
