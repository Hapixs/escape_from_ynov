import os
from combat import Combat
from character import Character
from prompting import prompting
from level import B1
from etage import *

class Piece: 

    def __init__(self, name : str, histoire : str = None, event : str = None, combat = None, enemy : Character = None, esca = None, asce = None, action = None):
         self._name = name
         self._histoire = histoire
         self._enemy = enemy
         self._combat = combat
         self.event = event
         self._esca = esca
         self._asce = asce
         self._action = action

    def __str__(self) -> str:
        return self._name
    
    def show_histoire(self, mon_etage : str, perso : Character):
        if self._esca != None :
            mon_etage.monter_etage(self, perso)
        if self._histoire != None:
            prompting(self._histoire)
        else:
            prompting(f"Aucune histoire disponible pour la salle {self._name}.")
        if self._asce != None :
            self._action.action(perso=perso, mon_etage=mon_etage)
        if self._action != None :
            self._action.action(perso=perso,mon_etage=mon_etage)
        if self._combat != None:
            result = Combat(character=perso,target=self._enemy, room= self._name).start_attack()
            if result :
               mon_etage.possible_move(mon_etage=mon_etage, perso= perso)
        if self._combat == None :
            mon_etage.possible_move(mon_etage=mon_etage, perso=perso)
            
    def enter_room(self, mon_etage :str, perso : Character):
        os.system("clear||cls")
        self.show_histoire(mon_etage, perso)


