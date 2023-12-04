
from character import Character

class Histoire():
    
    def __init__(self, nameroom : str, Character = Character()) -> None:
        self._nameroom = nameroom
        self._name = Character
        
    def __str__(self) -> str:
        print(f"{self._name} est dans {self._nameroom}")

