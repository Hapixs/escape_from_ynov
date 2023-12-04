import os
from typing import Any 

class Action:
    
    def __init__(self) -> None:
        pass
    
    def pick(self, item : str):
        if "$" in item:
            for i in range(item, 1):
                money = int(item[i])
            self._money += money
            self.getmoney(money)
        else :
            self._inventory.append(item)
            print(f"{self._name} a ramasse {item}.")
            