from character import Character
from prompting import prompting
import random
from dice import Dice


class Combat:
    
    def __init__(self, character: Character, target : Character, room : str):
        self.character = character
        self.target = target 
        self.room = room
    
    def start_attack(self, perso) :
        prompting(f'''Vous etrez dans {self.room}, face a vous {self.target._name}, avec {self.target._current_hp}HP,
un combat va pouvoir commencer :\n\n''')
        while self.character.is_alive() and self.target.is_alive():
            for i in range(0, len(self.character._level._attack)) :
                prompting(f'{i+1}: {self.character._level._attack[i]._name} {self.character._level._attack[i]._pts}\n')
            prompting(f'Choisis une action: ')
            sel = input()
            if sel == "1" or sel == "2" or sel == "3" or sel == "4":
                if (int(sel) <= len(self.character._level._attack)) :
                    if self.character.is_alive() :
                        prompting(f'''\nVous avez choisi pour attaquer {self.character._level._attack[int(sel)-1]._name} avec {self.character._level._attack[int(sel)-1]._pts} points.
il manque le lancer de dé\n''') 
                        self.attack(player=self.target, possible_choice_pts=self.character._level._attack[int(sel)-1]._pts)  
                        self.target.show_HP() 
                    if self.target.is_alive():
                        rand = random.randint(0, len(self.target._level._attack)-1)   
                        prompting(f"{self.target._name} attaque avec {self.target._level._attack[rand]._name} qui fait {self.target._level._attack[rand]._pts} degat\n")
                        self.attack(player=self.character, possible_choice_pts=self.target._level._attack[rand]._pts)
                        self.character.show_HP()
        if self.character.is_alive() :
            if self.target._name == "Mec de l'accueil" :
                self.character._accueil = True
            self.victoire(self.target)
            self.character._xp += self.target._xp
            self.target._xp = 0
            prompting(f'Tu a gagné {self.character._xp}xp\nIl te manque {self.character._level.get_xp_manquant(perso)-self.character._xp}xp pour passer au niveau suivant')
            if self.character._level.get_xp_manquant(perso)-self.character._xp <= 0 :
                self.character._level.levelup(perso)
            return True
        else : 
            self.defete(self.target)
            return False


    def decrease_health(self, target : Character, amount : int):
        target._current_hp -= amount
        if target._current_hp < 0:
            target._current_hp = 0
        
    def attack(self, player : Character, possible_choice_pts):
            roll= Dice(player._dice).roll()
            attack_value = roll + possible_choice_pts
            prompting(f"La puissance de l'attaque sera de {roll} + {possible_choice_pts} soit {attack_value} points\n\n") 
            self.decrease_health(player, amount=attack_value)

    def victoire(self, target : Character):
        if not target.is_alive() :
            prompting(f"\nFélicitation! Victoire contre {self.target._name}\n ")

    def defete(self, target : Character) :
        if target.is_alive() :
            prompting(f"\nMalheuresement tu a perdu face a {self.target._name} !\n GAME OVER \n")