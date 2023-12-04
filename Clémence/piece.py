import os
import sys
import time
#import combat
#from histoire import Histoire
from prompting import prompting

class Piece: 

    def __init__(self, name, histoire = None, combat = None) -> None:
         self._name = name
         self._histoire = histoire
         self._combat = combat
    
    def __str__(self) -> str:
        return f"{self._name}".upper() 
    
    def __repr__(self) -> str: 
        return self.__str__() 
    
    def show_histoire(self):
        if self._histoire != None:
            prompting(self._histoire)
        else:
            prompting(f"Aucune histoire disponible pour la salle {self._name}.")
        
    

    def enter_room(self):
        os.system("clear||cls")
        self.show_histoire()
        # self.start_combat()
        
