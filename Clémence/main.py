import os

class Piece: 

    def __init__(self, name, histoire=None, combat=None) -> None:
         self._name = name
         self._histoire = histoire
         self._combat = combat
    
    def __str__(self) -> str:
        return f"{self._name}".upper() 
    
    def __repr__(self) -> str: 
        return self.__str__() 

    def enter_room(self):
        print(f"You are in the room {self._name}")
        # self.show_histoire()
        # self.start_combat()
        
class Etage: 
    def __init__(self, template) -> None: 
        self._template = [] 
        self._position = (1, 1) 
        self.build_floor(template) 
        
    def build_floor(self, template): 
        self._template = template 
        
    def show_position(self): 
        print(f"Position actuelle: {self._position}") 
        print(self._template) 
        print(self._template[self._position[0]][self._position[1]]) 
        
    def get_room(self, pos):
        # print(pos)
        if pos:
            return self._template[pos[0]][pos[1]]
        else:
            return ""

    def possible_move(self):
        
        up = self.move_up()
        right = self.move_right()
        down = self.move_down()
        left = self.move_left()
        map_str = f"""
Carte:
┌──────┐──────┐──────┐──────┐
│ {self.get_room((0, 0))} │ {self.get_room((0, 1))} │ {self.get_room((0, 2))} │ {self.get_room((0, 3))} │
├──────┼──────┴──────┐──────┼
│ {self.get_room((1, 0))} │ {self.get_room((1, 1))} │ {self.get_room((1, 2))} │ {self.get_room((1, 3))} │
└──────┴──────┴──────┴──────┘

"""

    # Remplacer l'emplacement actuel par une croix
        map_str = map_str.replace(f"{self.get_room(self._position)}", "✖️")

    # Effacer l'écran avant d'afficher la nouvelle carte
        os.system("clear||cls")

    # Afficher la carte mise à jour
        print(map_str)
        
        enable_room = []
        possible_choice = []
        choix = ""
        while choix not in possible_choice:
            print(f"Vous etes dans la salle :{self.get_room(self._position)}")
            print("Déplacements possibles :")
            disable_room = ["", None]
            i = 1
            if not self.get_room(up) in disable_room:
                print(f"{i} {self.get_room(up)}")
                possible_choice.append(str(i))
                i += 1
                enable_room.append(up)
            if not self.get_room(right) in disable_room:
                print(f"{i} {self.get_room(right)}")
                possible_choice.append(str(i))
                i += 1
                enable_room.append(right)
            if not self.get_room(down) in disable_room:
                print(f"{i} {self.get_room(down)}")
                possible_choice.append(str(i))
                i += 1
                enable_room.append(down)
            if not self.get_room(left) in disable_room:
                print(f"{i} {self.get_room(left)}")
                possible_choice.append(str(i))
                i += 1
                enable_room.append(left)
            choix = input("Quel est votre choix ? ")
        print(f"Votre choix: {self.get_room(enable_room[int(choix) - 1])}")
        self._position = enable_room[int(choix) - 1]
        self.get_room(self._position).enter_room()

    def move_up(self):
        if self._position[0] - 1 < 0:
            return None 
        else:
            return (self._position[0] - 1, self._position[1])
   
    def move_right(self):
        length = len(self._template[self._position[0]])
        right_edge = length - 1
        if self._position[1] + 1 > right_edge:
            return None 
        else:
            return (self._position[0], self._position[1] + 1)
   
    def move_down(self):
        length = len(self._template)
        bottom_edge = length - 1
        if self._position[0] + 1 > bottom_edge:
            return None 
        else: 
            return (self._position[0] + 1, self._position[1])
   
    def move_left(self):
        if self._position[1] - 1 < 0:
            return None 
        else:
            return (self._position[0], self._position[1] - 1)
       
hub = Piece("Hub") 
couloir = Piece("Couloir") 
wc = Piece("WC") 
labo = Piece("Labo") 
salle201 = Piece("Salle 201") 
salle_boss = Piece("Salle BOSS") 
Ascenceur= Piece("Asce")
Accueil = Piece("Accu")
Home = Piece("Home")
Portiques = Piece("Port")
Esc1 = Piece("esc1")
Esc2 = Piece("esc2")

mon_etage = Etage( [ [Ascenceur,Esc1, Accueil ,None],
                     [None,Home,Esc2, Portiques], ] ) 
while True:
    mon_etage.possible_move()

                # hub (0, 1) 
# None (1, 0) # couloir (1,1) # labo (1, 2)
#               # wc (2, 1) 
