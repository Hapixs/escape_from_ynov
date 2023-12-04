
from typing import Any
from piece import Piece 
from prompting import prompting
import time
from character import Character
from level import Level
from position import Position


class Etage: 
    def __init__(self,name,  nbr, template : Piece =[], position = Position(1,1) ) -> None: 
        self._name = name
        self._nbr = nbr
        self._template = template
        self._position = position

        
    def show_position(self): 
        print(f"Position actuelle: {self._position}\n") 
        print(self._template) 
        print(self._template[self._position[0]][self._position[1]]) 

    def get_nbr(self):
        return self._nbr
    
    def get_floor(self):
        return self._name
     
    def get_room(self, pos : Position):
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
{self.get_floor()}
┌──────────┐──────────┐──────────┐──────────┐
│          │          │          │          │
│   {self.get_room((0, 0))}   │   {self.get_room((0, 1))}   │   {self.get_room((0, 2))}   │   {self.get_room((0, 3))}   │
│          │          │          │          │
├──────────┼──────────┼──────────┼──────────┼
│          │          │          │          │
│   {self.get_room((1, 0))}   │   {self.get_room((1, 1))}   │   {self.get_room((1, 2))}   │   {self.get_room((1, 3))}   │
│          │          │          │          │
└──────────┴──────────┴──────────┴──────────┘

"""

        # Remplacer l'emplacement actuel par une croix
        map_str = map_str.replace(f"{self.get_room(self._position)}", " ✖️  ")

        # Effacer l'écran avant d'afficher la nouvelle carte
        # os.system("clear||cls")

        # Afficher la carte mise à jour
        print(map_str)

        enable_room = []
        possible_choice = []
        choix = ""
        while choix not in possible_choice:
            prompting(f"Vous etes dans la salle :{self.get_room(self._position)}\n")
            prompting("Déplacements possibles :\n")
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
            prompting("Quel est votre choix ? ")
            choix = input()
        prompting(f"Votre choix: {self.get_room(enable_room[int(choix) - 1])}\n")
        time.sleep(1)
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
        
class EtageRDC(Etage):
    Hub = Piece("Hub ", "Vous venez d'arriver dans le Hub, ici on peut se battre contre un autre éleve\n",enemy=Character("Eleve",50, 4,[], 0), combat=True) 
    Ascenceur= Piece("Asce", "Sans la carte d'acces on ne peut pas prendre l'ascenceur\n")
    Accueil = Piece("Accu" , ''' L'accueil est le premier lieu ou nous arrivons pour allez dans le batiment, 
allez voir le mec de l'accueil, qui sait ce qu'il va se passer\n''', Character("Mec de l'accueil",50, 4,[], 0, Level() ))
    Home = Piece("Home", "Vous venez de faire vos premier pas dans Ynov, a vous de jouer\n")
    Portiques = Piece("Port", '''J'espere que vous avez de la chance, 
ou sinon que vous avez trouver ce qu'il faut pour passer facilemet...\n''')
    Esc1 = Piece("esc1",'''Les escalier 1 permettent d'aller a tous les étages
pour cela il faut y être autorisé
Trouver le moyen d'y arriver en allant dans les salles d'Ynov\n''' )
    Esc2 = Piece("esc2", '''Les escalier 2 permettent d'aller a tous les étages
pour cela il faut y être autorisé
Trouver le moyen d'y arriver en allant dans les salles d'Ynov\n''')
        
    def __init__(self, name = "Rez de Chaussée", nbr = 0 , template = ([Ascenceur,Esc1, Accueil ,None],
                     [Hub,Home,Esc2, Portiques]),position = (1,1) ):
        self._template = template
        self._name = name
        self._nbr = nbr
        self._position = position
        
    
    
        
class Etage1(Etage):
    P101= Piece("P101")
    P105 = Piece("P105")
    P108 = Piece("P108")
    Serveur = Piece("Serv")
    Esc1 = Piece("esc1")
    Esc2 = Piece("esc2")
        
    def __init__(self, name = "Etage 1", nbr = 1, template = ([P101,Esc1, None ,P105],
                     [None,Serveur,Esc2, P108])):
        self._template = template
        self._name = name
        self._nbr = nbr
        
class Etage2(Etage):
    Archi= Piece("Arch")
    Leo = Piece("Léo ")
    Ytrack = Piece("Ytrac")
    wc = Piece(" WC ") 
    Esc1 = Piece("esc1")
    Esc2 = Piece("esc2")
        
    def __init__(self, name = " Etage 2", nbr = 2, template = ([Archi,Esc1, None ,Leo],
                     [wc,None,Esc2, Ytrack])):
        self._template = template
        self._name = name
        self._nbr = nbr

class Etage3(Etage):
    Ascenceur= Piece("Asce")
    Accueil = Piece("Accu")
    Home = Piece("Home")
    Portiques = Piece("Port", "Vous êtes à côté des portiques, cette salle est l'endroit où tout le monde se réunit pour manger et jouer au baby, tiens quelqu'un se trouve au fond, il a l'air évasif")
    Esc1 = Piece("esc1")
    Esc2 = Piece("esc2")
        
    def __init__(self, name = "Etage 3", nbr = 3, template = ([Ascenceur,Esc1, Accueil ,None],
                     [None,Home,Esc2, Portiques])):
        self._template = template
        self._name = name
        self._nbr = nbr
        
class Etage4(Etage):
    Ascenceur= Piece("Asce")
    Accueil = Piece("Accu")
    Home = Piece("Home")
    Portiques = Piece("Port", "Vous êtes à côté des portiques, cette salle est l'endroit où tout le monde se réunit pour manger et jouer au baby, tiens quelqu'un se trouve au fond, il a l'air évasif")
    Esc1 = Piece("esc1")
    Esc2 = Piece("esc2")
        
    def __init__(self, name = "Etage 4", nbr = 4, template = ([Ascenceur,Esc1, Accueil ,None],
                     [None,Home,Esc2, Portiques]) ):
        self._template = template
        self._name = name
        self._nbr = nbr