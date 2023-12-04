import json

 
def OpenMessageRoom(FloorName : str, RoomName: str) :
    f = open("./Samy/Message/Room/"+FloorName+"/"+RoomName+".json", "r")
    content = json.load(f)
    print(content)

def OpenMessageNPC(NPCname : str, ActionName : str) :
    f = open("./Samy/Message/NPC/"+NPCname+"/"+ActionName+".json", "r")
    content = json.load(f)
    print(content)

def OpenMessageElement(ElementName : str) :
    f = open("./Samy/Message/Element/"+ElementName+".json", "r")
    content = json.load(f)
    print(content)

def OpenMessageAction(ActionName : str) :
    f = open("./Samy/Message/Action/"+ActionName+".json", "r")
    content = json.load(f)
    print(content)