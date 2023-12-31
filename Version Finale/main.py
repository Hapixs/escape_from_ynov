import os
from character import Character
from etage import EtageRDC
from prompting import prompting
from level import B1
from colorama import *
from rich.pretty import pprint


if __name__ == "__main__":
    
    clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
    clear()
    with open("./Version Finale/sprites/GAME_NAME.txt", 'r') as f:
        print(Fore.BLUE + Style.BRIGHT +f.read())
        print(Style.RESET_ALL)

    mon_etage = EtageRDC()
    prompting("\nBienvenue dans Ynov Campus, une nouvelle aventure pour vous ")
    prompting("\nPour commencer cette première année il faut d'abord choisir son nom :")
    name = input()
    joueur = Character(name, level= B1())
    joueur.initiali()
    prompting('''L'année va pouvoir commencer, ne pas oublier l'objectif, progresser pour vaincre le boss de Python\n''')
    mon_etage.possible_move(mon_etage, joueur)



