import os
from entities.player import *
from entities.inventory import *
from entities.place import *
from entities.item import *
from entities.npc import *

from factory import datafactory
from factory import placefactory

from rich.pretty import pprint

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
clear()
with open("./sprites/GAME_NAME.txt", 'r') as f:
        print(f.read())


def showMainBoard():
    print('(1)  Nouvelle partie')
    print('(2)  Continuer')
    selection = input('Choisis une action: ')

#showMainBoard()
placefactory.loadAllStoredPlace()

placefactory.createNewPlace("hub", [], ["Escalier1", "Escalier2", "Salle Ytrack"])
placefactory.createNewPlace("Escalier1", [], [])
placefactory.createNewPlace("Escalier2", [], [])
placefactory.createNewPlace("Salle Ytrack", [], [])

placefactory.saveAllCachedPlace()

print(placefactory.getPlaceFromName("acceuil"))