import random

class Dice:
    
    def __init__(self, faces = 6):
        self._faces = faces
    
    def __str__(self):
        return f"{self._faces} faces for the dice"
    
    def roll(self): 
        return random.randint(1, self._faces)
    
class RiggedDice(Dice):
    
    def roll(self, rigged = False):
        if rigged :                 #pense a simplifier : rigged == True <=> rigged
            return self._faces
        else :
            return super().roll()   #utiliser la méthode super() pour récupérer la valeur de la méthode mère
        
        #return self._faces if rigged else super().roll()
    


    
if __name__ == "__main__":
    a_dice = RiggedDice(6)
    for _ in range(10):
        print(a_dice.roll(False))