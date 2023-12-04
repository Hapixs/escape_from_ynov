from attack import Attack
class Level ():
    
    def __init__(self, level = "B1", option : str = None, attack : Attack =[]):
        self._level = level
        self._option = option
        self._attack : attack
        
    
class B1 (Level):
        
    def __init__(self, level = "B1",):
        self._level = level
        self._attack= ("Hello World!", 2) + ("Piscine golang", 4)
        
class B2 (Level):
        
    def __init__(self, level = "B2",):
        self._level = level
        self._attack = ("cat file.txt", 3) + ("git push",5)
            
class B3 (Level):
        
    def __init__(self, level = "B3", option = "Hardware"):
        self._level = level
        self._option = option
        self._attack = ("POO python", 3) + ("New VM", 3)
        
        
    def setAttack(self):
        if self._option == "Hardware" :
            self._attack.append("Cable hdmi", 5)
        elif self._option == "Robotique" : 
            self._attack.append("Arduino", 5)
        elif self._option == "Web" :
            self._attack.append("css", 5)
        elif self._options == "Cyber" :
            self._attack.append("nmap", 5)
        elif self._options == "Data IA" :
            self._attack.append("Database", 5)
        else :  
            print("Choisit une option")
                
class M1 (Level):
        
    def __init__(self, level = "M1", option = "Hardware"):
        self._level = level
        self._option = option
        self._attack = ("git branch", 3) +( "Eloquence", 5)
        
        
    def setAttack(self):
        if self._options == "Hardware" :
            self._attack.append("Cable hdmi", 6)
        elif self._options == "Robotique" :
            self._attack.append( "Arduino", 6)
        elif self._options == "Web" :
            self._attack.append("css", 6)
        elif self._options == "Cyber" :
            self._attack.append("nmap", 6)
        elif self._options == "Data IA" :
            self._attack.append("Database", 6)
        else :
            print("Choisit une option")

class M2 (Level):
        
    def __init__(self, level = "M2", option = "Hardware"):
        self._level = level
        self._option = option
        self._attack = ("Managment",4) + ("Jet de pc",4)
        
            
    def setAttack(self):
        if self._options == "Hardware" :
            self._attack.append(("Cable hdmi", 6), ("CPU", 8))
        elif self._options == "Robotique" :
            self._attack.append(("Arduino" , 6), ("Wall-e", 8))
        elif self._options == "Web" :
            self._attack.append(("css",6),("html", 8))
        elif self._options == "Cyber" :
            self._attack.append(("nmap",6),("Hacking", 8))
        elif self._options == "Data IA" :
            self._attack.append(("Database",6),("Chatgpt", 8))
        else :
            print("Choisit une option")
                
            
            
            
        
    