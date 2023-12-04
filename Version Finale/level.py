from attack import Attack
from prompting import prompting

class Level ():
    
    def __init__(self, name = "B1", option : str = None, attack = []):
        self._name = name
        self._option = option
        self._attack = attack
        
    def show_name(self):
        print(f"{self._name}")
        
    
class B1 (Level):
        
    def __init__(self, name = "B1"):
        self._name = name
        self._attack= [Attack("Hello World!", 2),Attack("Piscine golang", 4)]
        
class B2 (Level):
        
    def __init__(self, name = "B2"):
        self._name = name
        self._attack = [Attack("cat file.txt", 3),Attack("git push",5)]
            
class B3 (Level):
        
    def __init__(self, name = "B3", option = "Hardware"):
        self._name = name
        self._option = option
        self._attack = [Attack("POO python", 3),Attack("New VM", 3)]
        
        
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
        
    def __init__(self, name = "M1", option = "Hardware"):
        self._name = name
        self._option = option
        self._attack = [Attack("git branch", 3),Attack("Eloquence", 5)]
        
        
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
        
    def __init__(self, name = "M2", option = "Hardware"):
        self._name = name
        self._option = option
        self._attack = [Attack("Managment",4),Attack("Jet de pc",4)]
        
            
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
            
class Python (Level):
    
    def __init__(self,name="Prof de Python"):
        self._name = name
        self._attack = [Attack("Anti Chatgpt",10),Attack("Projet POO",10)]
    

class Accueil (Level):
    
    def __init__(self,name="Mec de Accueil"):
        self._name = name
        self._attack = [Attack("Passe ton badge",2),Attack("Aigri mood",4)]
        
class Mentor (Level):
    
    def __init__(self,name="Mentor"):
        self._name = name
        self._attack = [Attack("Pas l'heure de pause",2),Attack("20eme Piscine",4)]
    
        

    

            
            
            
        
    