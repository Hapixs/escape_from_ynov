from entities.npc import Npc
from factory import datafactory
import os


npcs = {}
def loadAllStoredNpc():
        folderPath = datafactory._defineFolderFromObject(Npc())
        for x in os.listdir(folderPath):
            npc = datafactory.loadJsonObject(x, Npc())
            npcs[npc.name] = npc

def saveAllCachedNpc():
    for x in npcs.values():
        datafactory.saveJsonObject(x.name+".json", x)

def createNewNpc(name, health, displayname):
    npc = Npc()
    npc.name = name
    npc.displayname = displayname
    npc.healthMax = health
    npc.health = health
    npc.displayname = displayname
    npcs[npc.name] = npc 
    return npc

def getNpcFromName(name):
    return npcs[name]