import os
import platform

def display(text, category=None, log=False):
    print(text)


def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")