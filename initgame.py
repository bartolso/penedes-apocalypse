import globs
from area import Area
from map import Map
from player import Player

import json


def load_strings(language='es'):
    if language == 'es':
        with open('strings_es.json', 'r', encoding='utf-8') as file:
            globs.strings = json.load(file)


def initialize_maps_and_areas():
    # Area.map primero es un string con el nombre del mapa. luego en link_areas_maps() se cambia a su
    # correspondiente objeto.
    globs.areas = {
        'bonaterra': Area(name='Bonaterra', description=globs.strings['area']['desc']['bonaterra'], coordinates={"x": 0, "y": 0},
                          items=None, gmap='baix_penedes'),
        'la_cometa': Area(name='La Cometa', description=globs.strings['area']['desc']['la_cometa'], coordinates={"x": 0, "y": 1},
                          items=None, gmap='baix_penedes'),
        'el_vendrell': Area(name='El Vendrell', description=globs.strings['area']['desc']['el_vendrell'], coordinates={"x": 0, "y": 2},
                            items=None, gmap='baix_penedes'),
        'les_pedreres': Area(name='Les Pedreres', description=globs.strings['area']['desc']['les_pedreres'], coordinates={"x": 1, "y": 0},
                             items=None, gmap='baix_penedes'),
        'bellvei': Area(name='Bellvei', description=globs.strings['area']['desc']['bellvei'], coordinates={"x": 1, "y": 1},
                        items=None, gmap='baix_penedes'),
        'cantera': Area(name='Cantera', description=globs.strings['area']['desc']['cantera'], coordinates={"x": 1, "y": 2},
                        items=None, gmap='baix_penedes')
    }

    globs.maps = {
        'baix_penedes': Map(name='Baix Penedès', areas=[], dimensions=(3, 3))
    }


def create_player(name='Default'):
    globs.player = Player(name=name, inventory=[], location=globs.areas['bonaterra'], health=20)


def link_maps_and_areas():
    # enlazar areas
    for area_key, area_obj in globs.areas.items():
        map_to_link = globs.maps[area_obj.gmap]
        area_obj.gmap = map_to_link

    # enlazar mapas
    for area_key, area_obj in globs.areas.items():
        for map_key, map_obj in globs.maps.items():
            if area_obj.gmap.name == map_obj.name:
                map_obj.areas.append(area_obj)

def newgame(language, player_name):
    load_strings(language=language)
    initialize_maps_and_areas()
    link_maps_and_areas()
    create_player(name=player_name)