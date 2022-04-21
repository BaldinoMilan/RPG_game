import Characters as crt
import weapons as wp
import equipment as plt
import map 
from random import randint

def create_character(name_, class_):
    if class_ == "paladin":
        return crt.Paladin(name_)
    elif class_ == "fighter":
        return crt.Fighter(name_)
    elif class_ == "assasin":
        return crt.Assasin(name_)
    elif class_ == "archerer":
        return crt.Archerer(name_)
    else:
        raise TypeError("your chracter must have a class, check the list of all classes: paladin, fighter, assasin, archerer")

def saving(character):
    file = open("save_1.txt", "w")
    if isinstance(character, crt.CharacterLike):
        for i in character.base_stats:
            file.write(f"{i}")
            file.write('\n')
    file.close()

def open_save():
    file = open("save_1.txt", "r")
    save = [i for i in file]
    file.close()
    new_game = [i.split("\n") for i in save]
    new_game = [i[0] for i in new_game]
    return new_game

""" SCRIPT """
