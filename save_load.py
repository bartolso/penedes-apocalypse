from datetime import datetime
import os

import tools
import globs
import pickle

save_folder_path = 'saves' # TODO: poner en config.ini

def save_game():
    now = datetime.now()
    dt = now.strftime("%Y-%m-%d_%H-%M")
    filename = f'{save_folder_path}/{dt}.apocalypse'
    with open(filename, 'wb') as f:
        pickle.dump((globs.strings, globs.player, globs.areas, globs.maps, globs.items, globs.npcs), f)
        tools.display(globs.strings['general']['save_game_successful'].format(filename=filename))


def load_game():
    filename = str(get_latest_save())
    filename = f'{save_folder_path}/{filename}'
    with open(filename, 'rb') as file:
        globs.strings, globs.player, globs.areas, globs.maps, globs.items, globs.npcs = pickle.load(file)
        tools.display(globs.strings['general']['load_game_successful'].format(filename=filename))


def get_latest_save():
    most_recent_file = None
    most_recent_datetime = None
    files = os.listdir(save_folder_path)

    for file in files:
        if file.endswith('.apocalypse'):
            datetime_str = file.replace('.apocalypse', '')
            file_datetime = datetime.strptime(datetime_str, '%Y-%m-%d_%H-%M')

            if most_recent_datetime is None or file_datetime > most_recent_datetime:
                most_recent_datetime = file_datetime
                most_recent_file = file

    return most_recent_file