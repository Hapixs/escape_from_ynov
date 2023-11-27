from entities.place import Place
from entities.inventory import Inventory
from python_easy_json import JSONObject

class Player(JSONObject): 
    username: str = None
    healthMax: float = None
    health: float = None
    staminaMax: float = None
    stamina: float = None
    inventory: Inventory = None
    sex: str = None
    level: float = None
    money: float = None
    place: Place = None
