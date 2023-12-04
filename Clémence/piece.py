import os
from combat import Combat
from character import Character
from prompting import prompting

class Piece: 

    def __init__(self, name : str, histoire = None, event = None, combat : Combat = None, enemy : Character = None):
         self._name = name
         self._histoire = histoire
         self._enemy = enemy
         self._combat = combat
         self.event = event


    def get_name(self):
        return self._name
    
    def show_histoire(self):
        if self._histoire != None:
            prompting(self._histoire)
            if self._combat != None:
                self._combat.start_attack()
        else:
            prompting(f"Aucune histoire disponible pour la salle {self._name}.")
        

    

    def enter_room(self):
        os.system("clear||cls")
        self.show_histoire()
        # self.start_combat()
        
