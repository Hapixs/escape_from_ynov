from python_easy_json import JSONObject

class Item(JSONObject):
    name: str = None
    durabilityMax: float = 0
    durability: float = 0