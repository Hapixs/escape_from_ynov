from dice import Dice
import Level


class Character:

    def init(self, name: str, max_hp: int, max_stamina: int, dice: Dice, gender: str, inventory = [], money: int = 0, level = Level()):
        self._name = name
        self._max_hp = max_hp
        self._current_hp = max_hp
        self._max_stamina = max_stamina
        self._current_stamina = max_stamina
        self._dice = dice
        self._gender = gender
        self._inventory = inventory
        self._money = money
        self._level = level

    def str(self):
        return f'''{self._name} est {self._gender}, 
        niveau : {self._level}
        vie    : {self._current_hp} hp'''

    def pick(self, item):
        self._inventory.append(item)
        print(f"{self._name} a ramasse {item}.")


    def show_inventory(self):
        print(f"{self._name} a dans son inventaire : ")          
        if len(self._inventory) > 0:
            inventory_dict = {}

            for item in self._inventory:
                if item in inventory_dict:
                    inventory_dict[item] += 1
                else:
                    inventory_dict[item] = 1

            for item, count in inventory_dict.items():
                print(f"{item} x {count}")



if  __name__ == "main":
    Salim = Character("Salim", 100, 50, Dice(6), "un homme")
    Manon = Character("Manon", 100, 49, Dice(6), "Une femme")
    print(Salim)
    print(Manon)

    Manon.pick("des fleurs")
    Manon.pick("des fleurs")
    Manon.pick("des framboises")
    Manon.pick("un livre")
    Manon.show_inventory()



