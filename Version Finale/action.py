import os
from typing import Any 
from dice import Dice
from prompting import prompting

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

    def action(self, perso , mon_etage) :
        if perso._accueil == False :
            lance = Dice(25)
            if lance == 5 :
                prompting("Bravo ton scan est passer, tu passe le portique\n")
                mon_etage.possible_move(perso, mon_etage)
            else :
                prompting("Malheuresement, ton scan n'a pas fonctionner, du devrais peut-etre aller voir le Mec de l'accueil\n")
                perso.position = [1,2]
                mon_etage.possible_move(perso, mon_etage)
        elif perso._accueil == True :
            lance = Dice(5)
            if lance == 5 :
                prompting("Bravo ton scan est passer, tu passe le portique\n")
                mon_etage.possible_move(perso, mon_etage)
            else :
                prompting("Désole ton scan n'a pas fonctionner, tu devrais réessayer\n")
                perso.position = [1,2]
                mon_etage.possible_move(perso, mon_etage)