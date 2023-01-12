import random
from pygame import *


#tuple de l'alphabet permettant d'ajouter des lettres aux joueurs
lettres_possibles = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

class Joueur:#création d'une class Joueur contenant toutes les infos d'un joueur
    def __init__(self):#création des stats de base du joueur
        self.points = 0
        self.letters = []

    def add_letters(self):#permet de faire piocher des lettre au joueur
        while len(self.letters) < 7:
            self.letters.append(random.choice(lettres_possibles))

    def add_points(self,nbr_points_a_add):#rajoute des points (ou en enleve) au joueur
        self.points += nbr_points_a_add

    def remettre_en_orde(self,nouvel_ordre):#permet a l'utilisateur de remttre ces lettres dans l'orde qu'il veut
        self.letters = (list(nouvel_ordre))

# def drawBoard(mySurface, height, width):
#     for colonne in range (width):
#         for ligne in range (height):
#             pygame.draw.rect(mySurface, color_lines, (10 + ligne*50, 10 + colonne*50, 50, 50), 3)
#
#
#
#
# def verif_validité_du_mots(mot):#vérifier si un mot est valable (et plus tard l'affichera)
#     if mot in liste_valable:
#         return True
#     else :
#         return False





