from __future__ import annotations
import keyboard 
from action import *
from npc import *
from etg import *


def HUB(Floor : str, whereIAm : str) :
    abc = True
    while abc:
        if keyboard.is_pressed('s'):
            Hub()
            abc = False
        elif keyboard.is_pressed('d'):
            OpenMessageRoom(Floor, whereIAm)
            RDC(Floor, whereIAm)
            abc = False

def ASCENCEUR(Floor : str, whereIAm : str) :
    abc = True
    while abc:
        if keyboard.is_pressed('s'):
            Ascenseur()
            abc = False
        elif keyboard.is_pressed('d'):
            OpenMessageRoom(Floor, whereIAm)
            RDC(Floor, whereIAm)
            abc = False

def ACCUEIL(Floor : str, whereIAm : str) :
    abc = True
    while abc:
        if keyboard.is_pressed('q'):
            Accueil()
        elif keyboard.is_pressed('d'):
            OpenMessageRoom(Floor, whereIAm)
            RDC(Floor, whereIAm)
            abc = False

def PORTIQUE(Floor : str, whereIAm : str) :
    abc = True
    while abc:
        if keyboard.is_pressed('s'):
            Portique()
        elif keyboard.is_pressed('d'):
            OpenMessageRoom(Floor, whereIAm)
            RDC(Floor, whereIAm)
            abc = False

def ESPACE_ECHANGE(Floor : str, whereIAm : str) :
        abc = True
        while abc:
            if keyboard.is_pressed('u'):
                Ascenseur()
                abc = False
            elif keyboard.is_pressed('e'):
                OpenMessageRoom(Floor, whereIAm)
                RDC(Floor, whereIAm)
                abc = False