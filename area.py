class Area:
    def __init__(self, name, coordinates, description, items, gmap):
        self.name = name
        self.coordinates = coordinates
        self.description = description
        self.items = items if items else []
        self.gmap = gmap
