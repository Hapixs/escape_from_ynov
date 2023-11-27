from entities.item import *
from typing import List
from python_easy_json import JSONObject

class Inventory(JSONObject):
    content: List[Item] = None