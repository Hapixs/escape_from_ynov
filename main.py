import os
from entities.player import *
from entities.inventory import *
from entities.place import *
from entities.item import *
from entities.npc import *
from entities.capacity import *
from entities.level import *

from factory import datafactory
from factory import placefactory
from factory import npcfactory

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
npcfactory.loadAllStoredNpc()

npcfactory.createNewNpc('Alred le gonz', 100, "oué")

npcfactory.saveAllCachedNpc()

print(npcfactory.getNpcFromName('Alred le gonz'))

level = Level()
level.name = "B1"
level.option = "RIEN DU TOUT"

capacity1 = Capacity()
capacity1.name = "Hello world"
capacity1.damage = 100

datafactory.saveJsonObject(level.name+".json", level)