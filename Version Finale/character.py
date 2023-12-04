from level import B1
from prompting import prompting


class Character:
    
    def __init__(self, name: str, max_hp: int = 100 , dice= 6, inventory = [], money: int = 0, level = B1()):
        self._name = name
        self._max_hp = max_hp
        self._current_hp = max_hp
        self._dice = dice
        self._inventory = inventory
        self._money = money
        self._level = level

    def initiali(self):
        prompting(f"{self._name} est en {self._level._name} avec {self._current_hp} hp\n")

    def show_HP(self):
        print(f'{self._name} / PV [{"♥" * (self._current_hp)}{"♡" * (self._max_hp - self._current_hp)}] {self._current_hp}/{self._max_hp}')

    def is_alive(self):
        return self._current_hp > 0   
    
    def get_money(self):
        prompting(f"{self._name} a actuellement {self._money} $\n")
        
    def get_inventory(self):
        prompting(f"{self._name} a actuellement dans son inventaire : ")          
        if len(self._inventory) > 0:
            inventory_dict = {}
            for item in self._inventory:
                if item in inventory_dict:
                    inventory_dict[item] += 1
                else:
                    inventory_dict[item] = 1

            for item, count in inventory_dict.items():
                print(f"{item} x {count}")
        




