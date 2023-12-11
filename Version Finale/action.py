import os
from typing import Any 
from dice import Dice
from prompting import prompting
from etage import *

class Action:
    
    def __init__(self) -> None:
        pass
    


    def pick(self, item : str):
        if "$" in item:
            for i in range(item, 1):
                money = int(item[i])
            self._money += money
            self.getmoney(money)
        else :
            self._inventory.append(item)
            print(f"{self._name} a ramasse {item}.")

class Portiques(Action) :

    def __init__(self) -> None:
        super().__init__()     

    def action(perso , mon_etage) :
        if perso._accueil == False :
            lance = Dice(25).roll()
            if lance == 1 :
                prompting("Bravo ton scan est passer, tu passe le portique\n")
                mon_etage.possible_move(perso=perso, mon_etage=mon_etage)
            else :
                prompting("Malheuresement, ton scan n'a pas fonctionner, du devrais peut-etre aller voir le Mec de l'accueil\n")
                mon_etage._position= (1,2)
                mon_etage.possible_move(perso=perso, mon_etage=mon_etage)
        elif perso._accueil == True :
            lance = Dice(3).roll()
            if lance == 1:
                prompting("Bravo ton scan est passer, tu passe le portique\n")
                mon_etage.possible_move(perso=perso, mon_etage=mon_etage)
            else :
                prompting("Désole ton scan n'a pas fonctionner, tu devrais réessayer\n")
                mon_etage._position= (1,2)
                mon_etage.possible_move(perso=perso, mon_etage=mon_etage)

class Ascenceur(Action):
    def __init__(self) -> None:
        super().__init__()
    
    def action(perso, mon_etage):
        if perso._asce == True :
            prompting("Bravo tu a trouver le badge d'acces ! tu peux maintenant acceder au 4eme etage !")
            mon_etage.acse(perso)
        else :
            prompting("Tu n'a toujours pas trouver le badge ! Essaye de fouiller ailleurs")
            mon_etage.possible_move(perso=perso, mon_etage=mon_etage)