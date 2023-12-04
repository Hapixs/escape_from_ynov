from character import Character
class Event:
    
    def __init__(self, event : str, event_type : int = 0,):
        self.event = event
        self.event_type = event_type
        
    def action(self):
        if self.event_type == 0:
            pick("20$")
        elif self.event_type == 1:
            pick("40 hp")
    
    def pick(self, item : str):
        if "$" in item:
            for i in range(item, 1):
                money = int(item[i])
            self._money += money
            self.characterget_money(money)
        elif "hp" in item:
            se
        else :
            self._inventory.append(item)
            print(f"{self._name} a ramasse {item}.")