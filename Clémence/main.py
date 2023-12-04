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

from rich.pretty import pprint

if __name__ == "__main__":
    
    clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
    clear()
    with open("./sprites/GAME_NAME.txt", 'r') as f:
        print(f.read())
    joueur = Character()
    mon_etage = EtageRDC()
    print('''Bienvenue dans Ynov Campus, 
          pour commencer cette première année il faut d'abord choisir son nom :'''
    )
    joueur._name = input("pour commencer cette première année il faut d'abord choisir son nom :")
    joueur.__str__()
    print('''L'année va pouvoir commencer, ne pas oublier l'objectif, progresser pour vaincre le boss de Python''')
    mon_etage.possible_move()
    while (joueur.is_alive):
        if mon_etage.get_nbr() == 0:
            pass

