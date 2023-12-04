from character import Character
from prompting import prompting


class Combat:
    
    def __init__(self, character: Character, target : Character):
        self.character = character
        self.target = target 
    
    def start_attack(self, character: Character, target: Character):
        prompting(f'''Vous etez dans {self.room}, face a vous {self.target._name}, avec {self.target._current_hp},
un combat va pouvoir commencer :''')
        possible_choice = character._level._attack
        possible_choice_name = character._level._attack._name
        possible_choice_pts = character._level._attack._pts
        for i in range(0, possible_choice):
            prompting(f'1: {possible_choice_name[i]} {possible_choice_pts[i]}')
            prompting(f'Choisis une action: ')
        sel = int(input())
        if sel == 1:
            prompting(f''''Vous avez choisi pour attaquer {possible_choice_name[sel-1]} avec {possible_choice_pts[sel-1] } points.
Le combat va pouvoir commencer, a votre disposition il y a un dé''') 
        while character.is_alive() and target.is_alive():
            character.attack(target, possible_choice_pts[sel-1])        
            target.attack(character, )

    def decrease_health(self, amount):
        self._current_hp -= amount
        if self._current_hp < 0:
            self._current_hp = 0
        
    def attack(self, player : Character, possible_choice_pts):
        if not self.is_alive :
            return 
        roll = self._dice.roll()
        attack_value = roll + possible_choice_pts
        prompting(f"La puissance de l'attaque sera de {roll} +{possible_choice_pts} soit {attack_value} points ") 
        self.decrease_health(player._current_hp)
