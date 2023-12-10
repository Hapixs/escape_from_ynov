from typing import Any
from piece import Piece 
from prompting import prompting
import time
from character import Character
from level import B1 , Python, Mentor, Accueil , M2
from position import Position
from event import Event
from action import Portiques
import os


class Etage: 
    def __init__(self,name,  nbr, template : Piece =[], position = Position(1,2) ) -> None: 
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
        
    def monter_etage(self, pos : Position):
        if pos.x == 0 and pos.y == 3:
            pass

    def possible_move(self, mon_etage :str, perso: Character):
        
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
            prompting(f"Vous etes dans la salle : {self.get_room(self._position)}\n")
            prompting("Déplacements possibles :\n")
            disable_room = ["", None]
            i = 1
            if not self.get_room(up) in disable_room:
                prompting(f"{i} {self.get_room(up)}\n")
                possible_choice.append(str(i))
                i += 1
                enable_room.append(up)
            if not self.get_room(right) in disable_room:
                prompting(f"{i} {self.get_room(right)}\n")
                possible_choice.append(str(i))
                i += 1
                enable_room.append(right)
            if not self.get_room(down) in disable_room:
                prompting(f"{i} {self.get_room(down)}\n")
                possible_choice.append(str(i))
                i += 1
                enable_room.append(down)
            if not self.get_room(left) in disable_room:
                prompting(f"{i} {self.get_room(left)}\n")
                possible_choice.append(str(i))
                i += 1
                enable_room.append(left)
            prompting("Quel est votre choix ? ")
            choix = input()
        prompting(f"Votre choix: {self.get_room(enable_room[int(choix) - 1])}\n")
        time.sleep(1)
        self._position = enable_room[int(choix) - 1]
        self.get_room(self._position).enter_room(mon_etage, perso)
        
        

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
        
    def monter_etage(self, piece, perso):
        os.system("clear||cls")
        prompting(piece._histoire)
        etage = [EtageRDC(), Etage1(), Etage2(), Etage3(), Etage4()]
        a = 1
        for i in etage :
            prompting(f'{a} {i._name}\n') 
            a += 1
        mon_etage=etage[int(input())-1]
        if mon_etage._name == "Etage 4" :
            prompting("Impossible d'y accèder une barrière te bloque\n")
            time.sleep(3)
            self.monter_etage(piece, perso)
        mon_etage.possible_move(mon_etage, perso)
        

   
        
    
    
        
class EtageRDC(Etage):
    Hub = Piece("Hub ", "Vous venez d'arriver dans le Hub, ici on peut se battre contre un autre éleve\n", combat = True,enemy= Character("Eleve presantant son projet de fin d'etude",50, 4, level=M2())) 
    Ascenceur= Piece("Asce", "Sans la carte d'acces on ne peut pas prendre l'ascenceur\n", asce=True)
    Accueil = Piece("Accu" , '''L'accueil est le premier lieu ou nous arrivons pour allez dans le batiment, 
allez voir le mec de l'accueil, qui sait ce qu'il va se passer\n''', combat= True, enemy= Character("Mec de l'accueil",50, 4,level=Accueil()))
    Home = Piece("Home", "Vous venez de faire vos premier pas dans Ynov, a vous de jouer\n")
    Portiques = Piece("Port", '''J'espere que vous avez de la chance, 
ou sinon que vous avez trouver ce qu'il faut pour passer facilemet...\n''', action = Portiques)
    Esc1 = Piece("Esc ",'''Les escalier permettent d'aller a tous les étages
Choisier votre étage:\n''', esca=True )

        
    def __init__(self, name = "Rez de Chaussée", nbr = 0 , template = ([Ascenceur, Hub, None,Esc1],
                                                                       [None, Accueil,Home, Portiques]),position = (1,2) ):
        self._template = template
        self._name = name
        self._nbr = nbr
        self._position = position
        
   
class Etage1(Etage):
    P101= Piece("P101", "Ici vous avez la possibilité de demonter pc pour voler des composant pour hardware\n", Event("P101", 2))
    P105 = Piece("P105", '''Aie aie aie, vous êtes arrivez en retard, vous voulez signez sur SWS 
mais le mentor est contre pour 12min, vous engagez un combat avec un mentor \n''', combat=True, enemy= Character("Costa", 60, 6, Mentor()) )
    P108 = Piece("P108", "Ici tu trouves npc pour monter en competence")
    Serveur = Piece("Serv")
    Esc1 = Piece("Esc ",'''Les escalier permettent d'aller a tous les étages
Choisier votre étage:\n''', esca=True )

        
    def __init__(self, name = "Etage 1", nbr = 1, template = ([None,P101,P105,Esc1],
                                                            [None,None, Serveur, P108]), position = (0,3)):
        self._template = template
        self._name = name
        self._nbr = nbr
        self._position = position

        
class Etage2(Etage):
    Archi= Piece("Arch")
    Leo = Piece("Léo ")
    Ytrack = Piece("Ytrac")
    wc = Piece(" WC ") 
    Esc1 = Piece("esc1")

        
    def __init__(self, name = "Etage 2", nbr = 2, template = ([None,wc, None ,Esc1],
                                                             [None,Archi,Leo, Ytrack]),position = (0,3)):
        self._template = template
        self._name = name
        self._nbr = nbr
        self._position = position

class Etage3(Etage):
    Box= Piece("Box ")
    Souk1 = Piece("Souk")
    Souk2 = Piece("Souk")
    Souk3 = Piece("Souk")
    Esc1 = Piece("esc1")
    Robotique = Piece("Robo")
        
    def __init__(self, name = "Etage 3", nbr = 3, template = ([Box,None, Souk1 ,Esc1],
                                                             [Robotique,Souk3,Souk2, None]), position = (0,3)):
        self._template = template
        self._name = name
        self._nbr = nbr
        self._position = position
        
class Etage4(Etage):
    Ascenceur = Piece("Asce")
    Admin= Piece("Admi")
    Python = Piece(" PY ")
    Esc1 = Piece("esc1")
    wc = Piece(" WC ") 

        
    def __init__(self, name = "Etage 4", nbr = 4, template = ([Ascenceur,Python, Admin ,Esc1],
                                                                [None,None,None, wc]),  position = (0,0)):
        self._template = template
        self._name = name
        self._nbr = nbr
        self._position = position
        
