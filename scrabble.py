import random

#tuple de l'alphabet permettant d'ajouter des lettres aux joueurs
lettres_possibles = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

class Joueur:#création d'une class Joueur contenant toutes les infos d'un joueur
    def __init__(self):#création des stats de base du joueur
        self.points = 0
        self.letters = []

    def add_letters(self):#permet de faire piocher des lettre au joueur
        while len(self.letters) < 7:
            self.letters.append(sac.piocher_une_lettre())

    def add_points(self,nbr_points_a_add):#rajoute des points (ou en enleve) au joueur
        self.points += nbr_points_a_add

    def remettre_en_orde(self,nouvel_ordre):#permet a l'utilisateur de remttre ces lettres dans l'orde qu'il veut
        self.letters = (list(nouvel_ordre))
class Lettres:#création d'une classe lettres contenant la lettre ,le nombre de points
    def __init__(self,nom,points):
        self.nom = nom
        self.points = points
#Création des les lettres possible avec le nombres de points correspondant
lettres_1_points = ["A","E","I","N","O","R","S","T","U","L"]
lettres_2_points = ["D","G","M"]
lettres_3_points = ["B","C","P"]
lettres_4_points = ["F","H","V"]
lettres_8_points = ["J","Q"]
lettres_10_points= ["K", "W", "X", "Y", "Z"]
for i in lettres_1_points:
    locals()[i]=Lettres(i, 1)
for i in lettres_2_points:
    locals()[i]=Lettres(i, 2)
for i in lettres_3_points:
    locals()[i]=Lettres(i, 3)
for i in lettres_4_points:
    locals()[i]=Lettres(i, 4)
for i in lettres_8_points:
    locals()[i]=Lettres(i, 8)
for i in lettres_10_points:
    locals()[i]=Lettres(i, 10)

class Sac: #création du sac contenant toutes les lettres et n'etant pas infini
    def __init__(self):#définition de toutes les lettres présente au début du jeu
         self.lettres_dans_le_sac ={A: 9, B: 2, C: 2, D: 4, E: 12, F: 2, G: 3, H: 2,I: 9, J: 1, K: 1, L: 4, M: 2, N: 6, O: 8, P: 2,Q: 1, R: 6, S: 4, T: 6, U: 4, V: 2, W: 2, X: 1,Y: 2, Z: 1}
    def piocher_une_lettre(self):#permet de piocher une lettre aléatoire et du l'enlever du sac
        lettre_piocher = random.choice(list(self.lettres_dans_le_sac.keys()))
        self.lettres_dans_le_sac[lettre_piocher] -= 1
        return lettre_piocher

sac = Sac()





