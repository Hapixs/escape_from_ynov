import os
import character

class Combat:
    
    def __init__(self, character: character, target : character, room):
        self.character = character
        self.target = target
        self.room = room
        
    def attack(self, target : character):
        if not self.is_alive :
            return 
        roll = self._dice.roll()
        damages = self._attack_value + roll
        print(f"{self._name} attack with {damages} damages (attack: {self._attack_value} + roll: {roll})")
        target.defense(damages)
    
    def defense(self, damages):
        roll = self._dice.roll()
        wounds = damages - self._defense_value - roll
        print(f"{self._name} take {wounds} wounds (damages: {damages} - defense: {self._defense_value} - roll: {roll})")
        self.decrease_health(wounds)