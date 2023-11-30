from dice import Dice

class Commandes: 
    
    def __init__(self, dice : Dice):
        self._dice = dice
        self._gift = string["argent", "nourriture", "xp"]
    
    def ben(self):
        roll = self._dice.roll()
        if roll ==1:
            return self._gifts[0]
        else if roll == 2:
            return self._gifts[1]
        else if roll == 3:
            return self._gifts[2]
        
    
        