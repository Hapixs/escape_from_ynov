import os
from combat import Combat
from character import Character
from prompting import prompting
from level import B1

class Piece: 

    def __init__(self, name : str, histoire : str = None, event : str = None, combat =False, enemy : Character = None):
         self._name = name
         self._histoire = histoire
         self._enemy = enemy
         self._combat = combat
         self.event = event

    def __str__(self) -> str:
        return self._name
    
    def show_histoire(self):
        if self._name == "Esc1":
            prompting(self._histoire)
            self.enter_room()
        if self._histoire != None:
            prompting(self._histoire)
            if self._combat != None:
                perso = Character("salim", level=B1())
                Combat(character=perso,target=self._enemy, room= self._name).start_attack()
        else:
            prompting(f"Aucune histoire disponible pour la salle {self._name}.")
            
    def enter_room(self):
        os.system("clear||cls")
        self.show_histoire()
