from entities.place import Place
from factory import datafactory
import os


places = {}
def loadAllStoredPlace():
        for x in os.listdir("./places"):
            place = datafactory.loadJsonObject(x, "./places", Place())
            places[place.name] = place

def saveAllCachedPlace():
    for x in places.values():
        datafactory.saveJsonObject(x.name+".json", "./places", x)

def createNewPlace(name, npcs, connected_places):
    place = Place()
    place.name = name
    place.npcs = npcs
    place.connected_places = connected_places
    places[place.name] = place 
    return place

def getPlaceFromName(name):
    return places[name]