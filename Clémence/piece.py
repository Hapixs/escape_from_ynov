import os
import sys
import time
#import combat
#from histoire import Histoire

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
            self.print_letter_by_letter(self._histoire.__str__)
        else:
            print(f"Aucune histoire disponible pour la salle {self._name}.")
    
    def print_letter_by_letter(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)  # Ajoutez une pause de 50 millisecondes entre chaque lettre
        print()  # Nouvelle ligne après l'affichage complet du texte

    def enter_room(self):
        os.system("clear||cls")
        self.show_histoire()
        # self.start_combat()
        
