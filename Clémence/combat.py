from character import Character

class Combat:
    
    def __init__(self, character: Character, target : Character, room):
        self.character = character
        self.target = target
        self.room = room    
        
    def attack(self, target : Character):
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
        
if __name__ == "__main__":
    character1 = Character("clem", 10, 10,  )
    character2 = Character()
    print(character1)
    print(character2)
    
    while character1.is_alive() and character2.is_alive():
        Combat.attack(character2)        
        Combat.attack(character1)
