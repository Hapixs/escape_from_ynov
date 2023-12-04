from dice import Dice
from level import Level

class Character:

    
    def init(self, name: str, max_hp: int = 100 , dice= Dice(), inventory = [], money: int = 0, level = Level()):
        self._name = name
        self._max_hp = max_hp
        self._current_hp = max_hp
        self._dice = dice
        self._inventory = inventory
        self._money = money
        self._level = level

    def __str__(self):
        print(f"{self._name} est {self._level} avec{self._current_hp} hp")


    def is_alive(self):
        return self._current_hp > 0   
    
    def get_money(self):
        print(f"{self._name} a actuellement {self._money} $")
        
    def get_inventory(self):
        print(f"{self._name} a actuellement dans son inventaire : ")          
        if len(self._inventory) > 0:
            inventory_dict = {}
            for item in self._inventory:
                if item in inventory_dict:
                    inventory_dict[item] += 1
                else:
                    inventory_dict[item] = 1

            for item, count in inventory_dict.items():
                print(f"{item} x {count}")
        




