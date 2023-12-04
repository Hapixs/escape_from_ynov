import os
from combat import Combat
from character import Character
from prompting import prompting

class Piece: 

    def __init__(self, name : str, histoire : str = None, event : str = None, combat =False, enemy : Character = None):
         self._name = name
         self._histoire = histoire
         self._enemy = enemy
         self._combat = combat
         self.event = event

<<<<<<< HEAD

=======
>>>>>>> ab849ed4afc0a8bfb05d39ad4c6873ad54c1594b
    def __str__(self) -> str:
        return self._name
    
    def show_histoire(self):
        if self._name == "Esc1":
            prompting(self._histoire)
            self.enter_room()
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
        
