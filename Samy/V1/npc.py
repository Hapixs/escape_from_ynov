import json
from charactere import *
from message import *
from etg import *
import keyboard

def Accueil():
        f = open("./Samy/Message/NPC/accueil/question.json", "r")
        content = json.load(f)
        print(content)
        abc = True
        while abc:
            if keyboard.is_pressed('c') :
                Personne._accueil = True
                f = open("./Samy/Message/NPC/accueil/reponce.json", "r")
                content = json.load(f)
                print(content)
                OpenMessageRoom('RDC', 'RDC')
                RDC('RDC', 'RDC')
                abc = False
            elif keyboard.is_pressed('u') | keyboard.is_pressed('t') | keyboard.is_pressed('s') :
                f = open("./Samy/Message/NPC/accueil/erreur.json", "r")
                content = json.load(f)
                print(content)
                Accueil()
                abc = False