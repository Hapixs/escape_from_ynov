from character import Character
class Event:
    
    def __init__(self, event : str, event_type : int = 0, Character : Character = None):
        self.event = event
        self.event_type = event_type
        self.character = Character
    
    
        
    def action(self):
        if self.event_type == 0:
            self.pick("20$")
        elif self.event_type == 1:
            self.pick("40 hp")
        elif self.event_type == 2:
            self.pick("objet hardware")
        elif self.event_type == 3:
            pass
        
    
    def pick(self, item : str):
        if "$" in item:
            for i in range(item, 1):
                money = int(item[i])
            self.character._money += money
            self.character.get_money(money)
        else :
            self.character._inventory.append(item)
            print(f"{self.character._name} a ramasse {item}.")