from typing import List
from entities.npc import *
from python_easy_json import JSONObject

class Place(JSONObject):
    name: str = None
    npcs: List[Npc] = None
    connected_places: List[str] = None