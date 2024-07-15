from player import Player
import save_load
import globs
import tools


class Action:
    def __init__(self, name, hotkey, **kwargs):
        self.name = name
        self.hotkey = hotkey
        self.kwargs = kwargs

    def execute(self, **kwargs):
        all_kwargs = self.kwargs.copy()
        all_kwargs.update(kwargs)
        #  self.method(**all_kwargs)


class SaveGame(Action):
    def __init__(self):
        name = f'save'
        super().__init__(name=name, hotkey=None)

    def execute(self):
        save_load.save_game()


class LoadGame(Action):
    def __init__(self):
        name = f'save'
        super().__init__(name=name, hotkey=None)

    def execute(self):
        save_load.load_game()


class Move(Action):
    def __init__(self, direction):
        self.direction = direction
        name = f'move_{direction}'
        hotkey = direction[0]
        super().__init__(name=name, hotkey=hotkey, direction=direction)

    def execute(self, player):
        player.move(self.direction)


class Examine(Action):
    def __init__(self, thing):
        self.thing = thing
        name = f'examine_{thing}'
        hotkey = thing[0]
        super().__init__(name=name, hotkey=hotkey, thing=thing)

    def execute(self, player):
        player.examine(self.thing)
