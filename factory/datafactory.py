from python_easy_json import JSONObject

def saveJsonObject(fileName, folderName, obj: JSONObject):
    data = obj.to_json(indent=4)
    with open(f"./{folderName}/{fileName}", "w") as outfile:
        outfile.write(data)

def loadJsonObject(fileName, folderName, cls: JSONObject):
    with open(f"./{folderName}/{fileName}", "r") as infile:
        data = infile.read()
        cls.__init__(data, cast_types=True)
        return cls