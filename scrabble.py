import random
import csv
import pygame
import time
aff = []
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
        self.letters = []
        global lettres_possible
        for p in nouvel_ordre:
            for u in  lettres_possible:
                if p == u.nom:
                    self.letters.append(u)


class Lettres:#création d'une classe lettres contenant la lettre ,le nombre de points
    def __init__(self,nom,points):
        self.nom = nom
        self.points = points

#Création des les lettres possible avec le nombres de points correspondant
lettres_possible = []
lettres_1_points = ["A","E","I","N","O","R","S","T","U","L"]
lettres_2_points = ["D","G","M"]
lettres_3_points = ["B","C","P"]
lettres_4_points = ["F","H","V"]
lettres_8_points = ["J","Q"]
lettres_10_points= ["K", "W", "X", "Y", "Z"]
for i in lettres_1_points:
    locals()[i]=Lettres(i, 1)
    lettres_possible.append(locals()[i])
for i in lettres_2_points:
    locals()[i]=Lettres(i, 2)
    lettres_possible.append(locals()[i])
for i in lettres_3_points:
    locals()[i]=Lettres(i, 3)
    lettres_possible.append(locals()[i])
for i in lettres_4_points:
    locals()[i]=Lettres(i, 4)
    lettres_possible.append(locals()[i])
for i in lettres_8_points:
    locals()[i]=Lettres(i, 8)
    lettres_possible.append(locals()[i])
for i in lettres_10_points:
    locals()[i]=Lettres(i, 10)
    lettres_possible.append(locals()[i])

class Sac: #création du sac contenant toutes les lettres et n'etant pas infini
    def __init__(self):#définition de toutes les lettres présente au début du jeu
        self.lettres_dans_le_sac ={A: 9, B: 2, C: 2, D: 4, E: 12, F: 2, G: 3, H: 2,I: 9, J: 1, K: 1, L: 4, M: 2, N: 6, O: 8, P: 2,Q: 1, R: 6, S: 4, T: 6, U: 4, V: 2, W: 2, X: 1,Y: 2, Z: 1}
    def piocher_une_lettre(self):#permet de piocher une lettre aléatoire et du l'enlever du sac
        lettre_piocher = random.choice(list(self.lettres_dans_le_sac.keys()))
        self.lettres_dans_le_sac[lettre_piocher] -= 1
        return lettre_piocher

sac = Sac()
Joueur1 = Joueur()
Joueur2 = Joueur()
Joueur3 = Joueur()
Joueur1.add_letters()
Joueur2.add_letters()
Joueur3.add_letters()
Joueurs = [Joueur1,Joueur2,Joueur3]
nbr_joueur = 3

def mot_valible_verif(mot):#vérifier la validité d'un mot
    with open('mots_acceptes.csv', 'r', encoding='utf-8') as fichier:
        csv_reader = csv.reader(fichier)
        for ligne in csv_reader:
            if mot.upper() in ligne:
                return True
    return False

def ajouter_au_mot_valides(mot):#ajoute le mot aux mots valides
    with open('mots_acceptes.csv', 'a', encoding='utf-8') as fichier:
        csv_writer = csv.writer(fichier)
        csv_writer.writerow([mot.upper()])

def ajouter_aux_mots_invalide(mot):#ajoute le mot aux mots invaldes
    with open('mots_refuses.csv', 'a', encoding='utf-8') as fichier:
        csv_writer = csv.writer(fichier)
        csv_writer.writerow([mot])
#coté utilisateur
# mot_a_verif = input("Entrez le mot à vérifier: ")

# if mot_valible_verif(mot_a_verif):
#     print("Le mot est valide.")
# else:
#     ajout_mot = input("Le mot n'est pas valide. Voulez-vous l'ajouter à la liste des mots valides? (o/n)")
#     if ajout_mot.lower() == 'o':
#         ajouter_au_mot_valides(mot_a_verif)
#         print("Le mot a été ajouté à la liste des mots valides.")
#     else:
#         ajouter_aux_mots_invalide(mot_a_verif)
#         print("Le mot a été ajouté à la liste des mots refusés.")


class Lettres_visuel:
    def __init__(self,nom):
        self.nom = nom#nom est une chaine de caractère
        self.coord = (None,None)

    def afficher_lettre(self,fenetre):
        x,y = self.coord
        pygame.draw.rect(fenetre, (255,255,255), (x, y, u, u))
        font = pygame.font.SysFont('KAZYcase scrabble', 50)
        lettre = font.render(self.nom, True, (0,0,0))
        fenetre.blit(lettre, self.coord)

    def suivre_souris(self,fenetre):
        lettre = font.render(self.nom, True, (0,0,0))
        position = pygame.mouse.get_pos()
        fenetre.blit(lettre, (position[0]-15,position[1]-15))
        return position
    # def verif_relachement_sur_lettre(self,x,y,u,mouse_x,mouse_y,lettre_select):
    #     return (x <= mouse_x <= x + u) and (y <= mouse_y <= y + u) and ((mouse_x,mouse_y) != lettre_select.coord)

lettre_double_case = ["B8", "D4", "F4", "H7", "J4", "N1", "N15", "O2", "O12", "P3", "P13", "Q4", "Q14"]
lettre_triple_case = ["A1", "A8", "H1", "H9", "O1", "O8"]
mot_double_case = ["D1", "D8", "E3", "E6", "G2", "G6", "H3", "H6", "I2", "I6", "L1", "L8", "N1", "N8", "O3", "O6", "R2", "R6", "S1", "S8", "T2", "T6", "U3", "U6"]
mot_triple_case =["B2", "B6", "C3", "C7", "D4", "D7", "E1", "E8", "F3", "F7", "G4", "G7", "H5", "H9"]
class Case_visuel:

    def __init__(self,nom,coord,hauteur,epaisseur):
        self.nom = nom
        self.coord = coord
        self.hauteur = hauteur
        self.epaisseur = epaisseur
        self.occupé = None
        self.couleur = (255,255,255)#vérification des bonus possible de la case et changement couleur
        if self.nom in lettre_double_case:
            self.couleur = (135,206,235)
        elif self.nom in lettre_triple_case:
            self.couleur = (0,0,139)
        elif self.nom == "H8":
            self.couleur = (255,255,0)
        elif self.nom in mot_double_case :
            self.couleur = (255, 192, 203)
        elif self.nom in mot_triple_case :
            self.couleur = (255, 0, 0)
    def vérif_relachement_sur_case_plus_ajout_lettre(self,position,lettre_select):#vérifie si la position de la souris lors du relachement corespond aux coordonées de la case
        coord_x , coord_y = self.coord[0],self.coord[1]
        position_x,position_y = position[0],position[1]
        if (coord_x<= position_x <= coord_x+self.epaisseur) and (coord_y<= position_y <= coord_y+self.hauteur):
            if self.occupé == None:
                self.occupé = lettre_select
                return True
    # def vérif_libérté_case_plus_ajout_lettres_dans_case(self,lettres_select):#vérifie que la case n'est pas déja occupé
    #     if self.occupé == None:
    #         self.occupé = lettres_select
    def afficher_case(self,fenetre):
        x,y = self.coord[0], self.coord[1]
        u = 53
        pygame.draw.rect(fenetre, self.couleur, (x, y, u, u))
        if not(self.occupé == None):
            lettre = font.render(self.occupé.nom, True, (0,0,0))
            fenetre.blit(lettre, (x+12,y+12))



pygame.init()
taille_fenetere = (840, 920)
#fond = pygame.image.load("grille_scrabble.png")
fenetre = pygame.display.set_mode(taille_fenetere)
lettres = []
#fenetre.blit(fond,(-3,0))
for i in Joueur1.letters:#création des objets lettres_visuel
    if i not in lettres:
        locals()[i.nom]=Lettres_visuel(i.nom)
    lettres.append(locals()[i.nom])

u = 50
for i in range(len(lettres)):#création des coordonée des lettres
    x = (i * u) + 230
    y = 870
    lettres[i].coord = (x,y)

cases_plateaux = []
coord = [0,-53]
for i in range(1, 16):
    coord[1] += 55
    coord[0] = 5
    for j in range(ord('A'), ord('P')):
        nom = chr(j) + str(i)
        coord[0] += 2
        cases_plateaux.append(Case_visuel(nom, (coord[0],coord[1]+2), 50, 50))
        coord[0] += 53
button_tour_validé = validate_button = pygame.Rect(650, 850, 150, 50)
compteur_tour = 0
def changer_tour():
    global nbr_joueur , compteur_tour
    if (compteur_tour + 1) > nbr_joueur :
        compteur_tour = 0
    else:
        compteur_tour += 1
    Joueur_actuel = Joueurs[compteur_tour]
    for i in Joueur_actuel.letters:#création des objets lettres_visuel
        if i not in lettres:
            locals()[i.nom]=Lettres_visuel(i.nom)
    lettres.append(locals()[i.nom])
font = pygame.font.SysFont('KAZYcase scrabble', 50)
pygame.display.flip()
continuer = True
lettre_select= None
font_valid = pygame.font.Font(None, 24)
text_valid = font_valid.render("Valider votre tour", True, (255, 255, 255))
text_rect = text_valid.get_rect(center = validate_button.center)
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#Pour quitter le jeu
            continuer = False

        elif event.type == pygame.MOUSEBUTTONDOWN:#quand l'utilisateur clique sur son clique gauche on récupere la mosition de la souris
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if validate_button.collidepoint(event.pos):
                changer_tour()
                time.sleep(0.2)

            #if (x <= mouse_x <= x + u) and (y <= mouse_y <= y + u):
            else:
                for i in lettres:#on verifie si ca correspond a la position d'une lettre
                        x, y = i.coord
                        if (x <= mouse_x <= x + u) and (y <= mouse_y <= y + u):
                            lettre_select = i

        elif event.type == pygame.MOUSEBUTTONUP:#si l(utilisateur relache son clique gauche on recupere la position de la souris
            if lettre_select == None:
                break
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i in lettres:#on vérifie que cette position correspond a la position d'une lettre et on les échanges
                x, y = i.coord
                if (x <= mouse_x <= x + u) and (y <= mouse_y <= y + u) and ((mouse_x,mouse_y) != lettre_select.coord):
                    lettre_select.coord, i.coord = i.coord, lettre_select.coord
                    lettre_select= None
                    break
            for i in cases_plateaux:
                if i.vérif_relachement_sur_case_plus_ajout_lettre((mouse_x,mouse_y),lettre_select):
                    compteur = 0
                    for i in Joueur1.letters:
                        compteur += 1
                        if lettre_select.nom == i.nom:
                            Joueur1.letters.remove(i)
                            lettres.remove(lettres[compteur-1])
                    break
            lettre_select = None

    # for i in range(len(lettres)):#création des coordonée des lettres
    #     x = (i * u) + 230
    #     y = 870
    #     lettres[i].coord = (x,y)
    for lettre in lettres :#affiche les lettres
        lettre.afficher_lettre(fenetre)

    if len(lettres)!=7:
        nombre_carre_noir = 7-len(lettres)
        x = 0
        for i in range (len(lettres)):
            x = (i * u) + 230
            y = 870
            lettres[i].coord = (x,y)
        for i in range (1,nombre_carre_noir+1):
            x = 580 - (50 * i)
            y = 870
            pygame.draw.rect(fenetre, (0,0,0), (x, y, 50,50))


    for i in cases_plateaux :#affiche les case
        i.afficher_case(fenetre)
        #i.occupé = lettre_select

    if not(lettre_select == None) :
        lettre_select.suivre_souris(fenetre)
    pygame.draw.rect(fenetre, (0, 255, 0), button_tour_validé)
    fenetre.blit(text_valid, text_rect)
    pygame.display.flip()

