import os
from action import Action
from attack import Attack
from character import Character
from combat import Combat
from dice import Dice
from etage import EtageRDC, Etage1, Etage2, Etage3, Etage4
from histoire import Histoire
from level import Level
from piece import Piece
from prompting import prompting

from rich.pretty import pprint

if __name__ == "__main__":
    
    clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
    clear()
    with open("./sprites/GAME_NAME.txt", 'r') as f:
        print(f.read())

    mon_etage = EtageRDC()
    prompting("\nBienvenue dans Ynov Campus, une nouvelle aventure pour vous ")
    prompting("\nPour commencer cette première année il faut d'abord choisir son nom :")
    name = input()
    joueur = Character(name)
    joueur.initiali()
    prompting('''L'année va pouvoir commencer, ne pas oublier l'objectif, progresser pour vaincre le boss de Python\n\n''')
    mon_etage.possible_move()
    while (joueur.is_alive):
        if mon_etage.get_nbr() == 0:
            pass

