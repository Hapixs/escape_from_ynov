from attack import Attack
from prompting import prompting

class Level ():
    
    def __init__(self, name = "B1", option : str = None, attack = []):
        self._name = name
        self._option = option
        self._attack = attack
        self._xp_requiered = 0
        
    def show_name(self):
        print(f"{self._name}")

    def get_xp_manquant(self, perso):
        if perso._level._name == "B1" :
            return B2()._xp_requiered
        elif perso._level._name == "B2" :
            return B3()._xp_requiered
        elif perso._level._name == "B3" :
            return M1()._xp_requiered
        elif perso._level._name == "M1" :
            return M2()._xp_requiered

    def levelup(self, perso) :
        if perso._level._name == "B1" :
            perso._level = B2()
        elif perso._level._name == "B2" :
            perso._level = B3()
        elif perso._level._name == "B3" :
            perso._level = M1()
        elif perso._level._name == "M1" :
            perso._level = M2()
        perso._xp = 0
        perso._current_hp = 100
    
class B1 (Level):
        
    def __init__(self, name = "B1"):
        self._name = name
        self._xp_requiered = 0
        self._attack= [Attack("Hello World!", 2),Attack("Piscine golang", 100)]
        
class B2 (Level):
        
    def __init__(self, name = "B2"):
        self._name = name
        self._xp_requiered = 100
        self._attack = [Attack("cat file.txt", 3),Attack("git push",5)]
            
class B3 (Level):
        
    def __init__(self, name = "B3", option = "Hardware"):
        self._name = name
        self._option = option
        self._xp_requiered = 250
        self._attack = [Attack("POO python", 5),Attack("New VM", 7)]
        
        
    def setAttack(self):
        if self._option == "Hardware" :
            self._attack.append("Cable hdmi", 10)
        elif self._option == "Robotique" : 
            self._attack.append("Arduino", 10)
        elif self._option == "Web" :
            self._attack.append("css", 10)
        elif self._options == "Cyber" :
            self._attack.append("nmap", 10)
        elif self._options == "Data IA" :
            self._attack.append("Database", 10)
        else :  
            print("Choisit une option")
                
class M1 (Level):
        
    def __init__(self, name = "M1", option = "Hardware"):
        self._name = name
        self._option = option
        self._xp_requiered = 500
        self._attack = [Attack("git branch", 7),Attack("Eloquence", 10)]
        
        
    def setAttack(self):
        if self._options == "Hardware" :
            self._attack.append("Cable hdmi", 11)
        elif self._options == "Robotique" :
            self._attack.append( "Arduino", 11)
        elif self._options == "Web" :
            self._attack.append("css", 11)
        elif self._options == "Cyber" :
            self._attack.append("nmap", 11)
        elif self._options == "Data IA" :
            self._attack.append("Database", 11)
        else :
            print("Choisit une option")

class M2 (Level):
        
    def __init__(self, name = "M2", option = "Hardware"):
        self._name = name
        self._option = option
        self._xp_requiered = 1000
        self._attack = [Attack("Managment",10),Attack("Jet de pc",11)]
        
            
    def setAttack(self):
        if self._options == "Hardware" :
            self._attack.append(("Cable hdmi", 14), ("CPU", 15))
        elif self._options == "Robotique" :
            self._attack.append(("Arduino" , 14), ("Wall-e", 15))
        elif self._options == "Web" :
            self._attack.append(("css",14),("html", 15))
        elif self._options == "Cyber" :
            self._attack.append(("nmap",14),("Hacking", 15))
        elif self._options == "Data IA" :
            self._attack.append(("Database",14),("Chatgpt", 15))
        else :
            print("Choisit une option")
            
class Python (Level):
    
    def __init__(self,name="Prof de Python"):
        self._name = name
        self._attack = [Attack("Anti Chatgpt",15),Attack("Projet POO",18)]
    

class Accueil (Level):
    
    def __init__(self,name="Mec de Accueil"):
        self._name = name
        self._attack = [Attack("Passe ton badge",2),Attack("Aigri mood",4)]
        
class Mentor (Level):
    
    def __init__(self,name="Mentor"):
        self._name = name
        self._attack = [Attack("Pas l'heure de pause",5),Attack("20eme Piscine",7)]

class Directeur (Level):
    
    def __init__(self,name="Directeur"):
        self._name = name
        self._attack = [Attack("-7 500$",20),Attack("Redoublement",10)]

        

    

            
            
            
        
    