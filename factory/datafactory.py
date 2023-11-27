from python_easy_json import JSONObject
import re
import os

def saveJsonObject(fileName, obj: JSONObject):
    data = obj.to_json(indent=4)
    obj_class = str(type(obj))
    folderName = _defineFolderFromObject(obj)

    with open(f"./{folderName}/{fileName}", "w") as outfile:
        outfile.write(data) 

def loadJsonObject(fileName, cls: JSONObject):
    folderName = _defineFolderFromObject(cls)
    with open(f"./{folderName}/{fileName}", "r") as infile:
        data = infile.read()
        cls.__init__(data, cast_types=True)
        return cls

def _defineFolderFromObject(obj):
    obj_class = str(type(obj))
    folderName = "./data/templates/"+re.search("^<class 'entities[.](.+)[.].+$", obj_class).group(1)
    try:
        os.makedirs(folderName)
    except OSError:
        pass
    
    return folderName
