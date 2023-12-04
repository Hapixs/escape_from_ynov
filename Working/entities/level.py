from python_easy_json import JSONObject
from entities.capacity import Capacity 


class Level(JSONObject):
    name: str = None
    option: str = None
    capcities: list[Capacity] = None