from __future__ import annotations
import keyboard 
from action import *
from message import *
from Rez_de_chausse import *

def RDC(Floor : str, whereIAm : str) :
    abc = True
    while abc:
        if keyboard.is_pressed('h'):
            OpenMessageRoom(Floor, 'hub')
            HUB(Floor, whereIAm)
            abc = False
        elif keyboard.is_pressed('e'):
            OpenMessageRoom(Floor, 'ascenceur')
            ASCENCEUR(Floor, whereIAm)
            abc = False
        elif keyboard.is_pressed('a'):
            OpenMessageRoom(Floor, 'accueil')
            ACCUEIL(Floor, whereIAm)
            abc = False
        elif keyboard.is_pressed('p'):
            OpenMessageRoom(Floor, 'portique')
            PORTIQUE(Floor, whereIAm)
            abc = False