from typing import Any
from piece import Piece 
from prompting import prompting
import time
from character import Character
from level import B1 , Python, Mentor, Accueil , M2, Directeur
from position import Position
from event import Event
from action import Portiques, Ascenceur
import os
from colorama import *

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
        
    def possible_move(self, mon_etage :str, perso: Character):
        
        up = self.move_up()
        right = self.move_right()
        down = self.move_down()
        left = self.move_left()
        map_str = Fore.BLUE + Style.BRIGHT +f"""
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
        print(Style.RESET_ALL)
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
            self.monter_etage(piece, perso=perso)
        mon_etage.possible_move(mon_etage= mon_etage,perso= perso)
        
    def acse(self, perso) :
        mon_etage = Etage4()
        mon_etage.possible_move(mon_etage=mon_etage,perso= perso)
        
    
    
        
class EtageRDC(Etage):
    Hub = Piece("Hub ", "Tu viens d'arriver dans le Hub, ici on peut se battre contre un autre éleve\n", combat = True,enemy= Character("Eleve presantant son projet de fin d'etude",50, 4, level=M2())) 
    Ascenceur= Piece("Asce", "Sans la carte d'acces on ne peut pas prendre l'ascenceur\n", asce=True, action= Ascenceur)
    Accueil = Piece("Accu" , '''L'accueil est le premier lieu ou nous arrivons pour allez dans le batiment, 
va voir le mec de l'accueil, qui sait ce qu'il va se passer\n''', combat= True, enemy= Character("Mec de l'accueil",50, 4,level=Accueil()))
    Home = Piece("Home", '''Le premier endroit ou tu mettez les pieds,
rien ne se passe mais les autres salles vont être intéressantes.\n''')
    Portiques = Piece("Port", '''J'espere que tu as de la chance, 
ou sinon que tu as trouver ce qu'il faut pour passer facilemet...\n''', action = Portiques)
    Esc1 = Piece("Esc ",'''Les escalier permettent d'aller a tous les étages
Choisie votre étage:\n''', esca=True )

        
    def __init__(self, name = "Rez de Chaussée", nbr = 0 , template = ([Ascenceur, Hub, None,Esc1],
                                                                       [None, Accueil,Home, Portiques]),position = (1,2) ):
        self._template = template
        self._name = name
        self._nbr = nbr
        self._position = position
        
   
class Etage1(Etage):
    P101= Piece("P101", "Ici tu as la possibilité de demonter pc pour voler des composant pour hardware\n")
    P105 = Piece("P105", '''Aie aie aie, tu es arrivé en retard, tu voulais signer sur SWS 
mais le mentor est contre pour 12min, tu engages un combat avec un mentor \n''', combat=True, enemy= Character("Costa", 60, 6, Mentor()) )
    P108 = Piece("P108", "Ici tu trouves Théo , il va te faire un petit cadeau pour l'avoir aider dans son projet")
    Serveur = Piece("Serv", "Si l'option que tu as choisi est la cybersécurité tu es chanceux, tu vas pouvoir entrer et récuperer des objets interresants")
    Esc1 = Piece("Esc ",'''Les escalier permettent d'aller a tous les étages
Choisie votre étage:\n''', esca=True )

        
    def __init__(self, name = "Etage 1", nbr = 1, template = ([None,P101,P105,Esc1],
                                                            [None,None, Serveur, P108]), position = (0,3)):
        self._template = template
        self._name = name
        self._nbr = nbr
        self._position = position

        
class Etage2(Etage):
    Archive= Piece("Arch", "Echanges du matériel contre de l'argent c'est simple ici, bienvenue aux archives\n")
    Leo = Piece('''Léo ", "Dans cette salle on va pas rigoler longtemps, avec les tests de leo, les compétences doublent pour des bonnes réponses
si jamais la chance se présente il ne faut pas oublier le clavier externe de Léo\n''')
    Ytrack = Piece("Ytrac", '''Cette salle a beaucou d'importance, pour tout exo rendu a temps il y a une petite surprise
Vu le nombre d'oublie dans la salle récuperer une souris gaming ne va pas se faire remarquer\n''')
    wc = Piece(" WC ", "Une envie présente, tu auras la chance de trouver quelque chose ici\n") 
    Esc1 = Piece("Esc ",'''Les escalier permettent d'aller a tous les étages
Choisie votre étage:\n''', esca=True )
        
    def __init__(self, name = "Etage 2", nbr = 2, template = ([None,wc, None ,Esc1],
                                                             [None,Archive,Leo, Ytrack]),position = (0,3)):
        self._template = template
        self._name = name
        self._nbr = nbr
        self._position = position

class Etage3(Etage):
    Box= Piece("Box ", "Un bonheur les oraux mais on a pas toujours le choix, face a un mentor de nouveau\n", combat=True, enemy= Character("Valentin", 60, 6, Mentor()) )
    Souk1 = Piece("Souk", "C'est le basard mais au moins il y a des chances de trouver quelque chose d'interéssant\n")
    Souk2 = Piece("Souk","C'est le basard mais au moins il y a des chances de trouver quelque chose d'interéssant\n")
    Souk3 = Piece("Souk","C'est le basard mais au moins il y a des chances de trouver quelque chose d'interéssant\n")
    Robotique = Piece("Robo")
    Esc1 = Piece("Esc ",'''Les escalier permettent d'aller a tous les étages
Choisie votre étage:\n''', esca=True )

        
    def __init__(self, name = "Etage 3", nbr = 3, template = ([Box,None, Souk1 ,Esc1],
                                                             [Robotique,Souk3,Souk2, None]), position = (0,3)):
        self._template = template
        self._name = name
        self._nbr = nbr
        self._position = position
        
class Etage4(Etage):
    Ascenceur = Piece("Asce")
    Admin= Piece("Admi", '''La fin du jeu approche avant d'aller voir le Boss du jeu, le directeur veut une discution assez conflictuelle, nouveau combat !''', combat=True, enemy= Character("Directeur", 100, 6, Directeur()))
    Python = Piece(" PY ", '''L'heure est venu, le combat le plus important est maintenant, il faut tout donner. 
Monsieur Ladrat, le prof de python est face a toi, il risque de te donner une bonne lecon sauf si tu lui en donne une... ''', combat= True,enemy= Character("Monsieur Ladrat", 200, 6, Python()))
    wc = Piece(" WC ", "Une envie présente, tu auras la chance de trouver quelque chose ici\n") 
    Esc1 = Piece("Esc ",'''Les escalier permettent d'aller a tous les étages
Choisie votre étage:\n''', esca=True )

        
    def __init__(self, name = "Etage 4", nbr = 4, template = ([Ascenceur,Python, Admin ,Esc1],
                                                                [None,None,None, wc]),  position = (0,0)):
        self._template = template
        self._name = name
        self._nbr = nbr
        self._position = position
        
