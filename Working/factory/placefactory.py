from entities.place import Place
from factory import datafactory
import os


places = {}
def loadAllStoredPlace():
        folderPath = datafactory._defineFolderFromObject(Place())
        for x in os.listdir(folderPath):
            place = datafactory.loadJsonObject(x, Place())
            places[place.name] = place

def saveAllCachedPlace():
    for x in places.values():
        datafactory.saveJsonObject(x.name+".json", x)

def createNewPlace(name, npcs, connected_places):
    place = Place()
    place.name = name
    place.npcs = npcs
    place.connected_places = connected_places
    places[place.name] = place 
    return place

def getPlaceFromName(name):
    return places[name]