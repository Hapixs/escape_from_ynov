import Character

        
class Attack :
        
    def __init__(self, name : string, pts : int):
        self._name = name 
        self._pts = pts
            
class Level (Attack):
    
    def __init__(self, level : string = "B1", option : Option = None):
        self._level = level
        self._option = option
        self._attack : Attack[]
        
    
    class B1 (Level):
        
        def __init__(self, level = "B1",)
            self._level = level
            self._attack= ("Hello World!", 2) + ("Piscine golang", 4)
        
    class B2 (Level):
        
        def __init__(self, level = "B2",)
            self._level = level
            self._attack = ("cat file.txt", 3) + ("git push",5)
            
    class B3 (Level):
        
        def __init__(self, level = "B3", option = "Hardware")
            self._level = level
            self._option = option
            self._attack = ("POO python", 3) + ("New VM", 3)
        
        
        def setAttack(self):
            if self._option == "Hardware" :
                self._attack += ("Cable hdmi", 5)
            else if self._option == "Robotique" :
                self._attack += ("Arduino", 5)
            else if self._option == "Web" :
                self._attack += ("css", 5)
            else if self._options == "Cyber" :
                self._attack += ("nmap", 5)
            else if self._options == "Data IA" :
                self._attack += ("Database", 5)
            else :  
                print("Choisit une option")
                
    class M1 (Level):
        
        def __init__(self, level = "M1", option = "Hardware")
            self._level = level
            self._option = option
            self._attack = ("git branch", 3) +( "Eloquence", 5)
        
        
        def setAttack(self):
            if self._options == "Hardware" :
                self._attack += ("Cable hdmi", 6)
            else if self._options == "Robotique" :
                self._attack +=( "Arduino", 6)
            else if self._options == "Web" :
                self._attack += ("css", 6)
            else if self._options == "Cyber" :
                self._attack += ("nmap", 6)
            else if self._options == "Data IA" :
                self._attack += ("Database", 6)
            else :
                print("Choisit une option")

    class M2 (Level):
        
        def __init__(self, level = "M2", option = "Hardware")
            self._level = level
            self._option = option
            self._attack = ("Managment",4) + ("Jet de pc",4)
        
            
            def setAttack(self):
            if self._options == "Hardware" :
                self._attack += ("Cable hdmi", 6) + ("CPU", 8)
            else if self._options == "Robotique" :
                self._attack += ("Arduino" , 6)+ ("Wall-e", 8)
            else if self._options == "Web" :
                self._attack += ("css",6) + ("html", 8)
            else if self._options == "Cyber" :
                self._attack += ("nmap",6) + ("Hacking", 8)
            else if self._options == "Data IA" :
                self._attack += ("Database",6) + ("Chatgpt", 8)
            else :
                print("Choisit une option")
                
            
            
            
        
    