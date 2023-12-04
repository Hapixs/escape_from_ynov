from message import *
from map import *
from npc import *
from action import *
from Rez_de_chausse import *
from etg import *

# f = open("./Samy/Map/RDC.txt", "r")
# content = f.read()
# print(content)

import keyboard 
abc = True
def run_func():
    Floor = "RDC"
    whereIAm = "RDC"
    OpenMessageRoom(Floor, 'base')
    OpenMessageRoom(Floor, 'RDC')
    RDC(Floor, whereIAm)

print('To start press S')
while abc:
  if keyboard.is_pressed('S'): 
    run_func()
    abc = False