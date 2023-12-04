

class Histoire():
    
    def __init__(self, nameroom : str, name) -> None:
        self._nameroom = nameroom
        self._name = name
        
    def show(self) -> str:
        print(f"{self._name} est dans {self._nameroom}")

