class NPC:
    def __init__(self, name, location, inventory, health, dialogues):
        self.name = name
        self.location = location
        self.inventory = inventory if inventory else []
        self.health = health
        self.dialogues = dialogues