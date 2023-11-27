import json , random
from charactere import *
from message import *
from etg import *
import keyboard

def Portique():
    if ( Personne._accueil ) :
        result = random.randrange(1, 6)
        if (result == 5) :
            f = open("./Samy/Message/Room/RDC/espace_echange.json", "r")
            content = json.load(f)
            print(content)
        else :
            f = open("./Samy/Message/Action/Portique.json", "r")
            content = json.load(f)
            print(content)
            if ( input() == "entre") :
                OpenMessageRoom('RDC', 'entre')
            else :
                Portique()
    else :    
        result = random.randrange(1, 26)
        if (result == 5) :
            f = open("./Samy/Message/Room/RDC/espace_echange.json", "r")
            content = json.load(f)
            print(content)
            ESPACE_ECHANGE("RDC", "RDC")
        else :
            f = open("./Samy/Message/Action/Portique.json", "r")
            content = json.load(f)
            print(content)
            abc = True
            while abc:
                if keyboard.is_pressed('d'):
                    OpenMessageRoom('RDC', 'RDC')
                    RDC("RDC", 'RDC')
                    abc = False
                elif keyboard.is_pressed('r'):
                    Portique()
                    abc = False

def Ascenseur() :
    if (Personne._proviseur) :
        f = open("./Samy/Message/Room/4eme/4eme.json", "r")
        content = json.load(f)
        print(content)
    else :
        f = open("./Samy/Message/Action/Ascenceur.json", "r")
        content = json.load(f)
        print(content)
        RDC('RDC', 'RDC')

def Hub() :
    f = open("./Samy/Message/Action/Hub.json", "r")
    content = json.load(f)
    print(content)
    RDC('RDC', 'RDC')

def Archi() :
    pass

def Escalier(seedetg : int):
    random.seed = seedetg
    result = random.randrange(1, 5)
    f = open("./Samy/Message/Room/Escalier/escalier_"+str(result)+".json", "r")
    content = json.load(f)
    print(content)

def Premier() :
    f = open("./Samy/Message/Room/1er/1er.json", "r")
    content = json.load(f)
    print(content)
    return "1er"

def Deuxieme(etage : str) -> str :
    if (Personne._mentor) :
        f = open("./Samy/Message/Room/2eme/2eme.json", "r")
        content = json.load(f)
        print(content)
        etage = "2eme"
        return etage
    else :
        f = open("./Samy/Message/Room/Escalier/erreur.json", "r")
        content = json.load(f)
        print(content)
        f = open("./Samy/Message/Room/"+etage+"/"+etage+".json", "r")
        content = json.load(f)
        print(content)

def Troisieme() :
    if (Personne._piscine) :
        f = open("./Samy/Message/Room/3eme/3eme.json", "r")
        content = json.load(f)
        print(content)
        etage = "2eme"
        return etage
    else :
        f = open("./Samy/Message/Room/Escalier/erreur.json", "r")
        content = json.load(f)
        print(content)
        f = open("./Samy/Message/Room/"+etage+"/"+etage+".json", "r")
        content = json.load(f)
        print(content)

def Quatrieme() :
        f = open("./Samy/Message/Room/Escalier/4eme.json", "r")
        content = json.load(f)
        print(content)