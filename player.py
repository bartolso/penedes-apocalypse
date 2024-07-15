import tools
import globs

import copy


class Player:
    def __init__(self, name, inventory, location, health):
        self.name = name
        self.inventory = inventory if inventory else []
        self.location = location
        self.health = health

    def move(self, direction):
        coordinates = copy.copy(self.location.coordinates)
        if direction == 'norte' or direction == 'n':
            coordinates['y'] -= 1
        elif direction == 'sur' or direction == 's':
            coordinates['y'] += 1
        elif direction == 'este' or direction == 'e':
            coordinates['x'] += 1
        elif direction == 'oeste' or direction == 'o':
            coordinates['x'] -= 1
        else:
            tools.display(f"¡Dirección inválida!: {direction}")

        for key, value in globs.areas.items():
            if value.coordinates == coordinates:
                self.location = value

    def examine(self, thing):
        if thing == 'área' or thing == 'area':
            tools.display(self.location.description)
        else:
            tools.display('No sé qué es eso')
