import random
import csv
import pygame
import time

class Joueur:#création d'une class Joueur contenant toutes les infos d'un joueur
    def __init__(self,nom):#création des stats de base du joueur
        self.points = 0
        self.letters = []
        self.nom = nom
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
Joker = Lettres("_",0)
lettres_possible.append(Joker)
class Sac: #création du sac contenant toutes les lettres et n'etant pas infini
    def __init__(self):#définition de toutes les lettres et de leur nombre présente au début du jeu
        self.lettres_dans_le_sac ={Joker:2,A: 9, B: 2, C: 2, D: 4, E: 12, F: 2, G: 3, H: 2,I: 9, J: 1, K: 1, L: 4, M: 2, N: 6, O: 8, P: 2,Q: 1, R: 6, S: 4, T: 6, U: 4, V: 2, W: 2, X: 1,Y: 2, Z: 1}
    def piocher_une_lettre(self):#permet de piocher une lettre aléatoire et du l'enlever du sac
        lettre_piocher = random.choice(list(self.lettres_dans_le_sac.keys()))
        self.lettres_dans_le_sac[lettre_piocher] -= 1
        return lettre_piocher

sac = Sac()

def mot_valible_verif(mot):#vérifier la validité d'un mot
    with open('mots_acceptes.csv', 'r', encoding='utf-8') as fichier:

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


class Lettres_visuel:#définition d'une class lettres visuel étant a part de la classe lettre et gérant juste la partie visuel des lettres
    def __init__(self,nom,points):
        self.nom = nom#nom est une chaine de caractère
        self.coord = (None,None)
        self.points = points
    def afficher_lettre(self,fenetre):#permet d'afficher la lettre a ses coordonée avec ses points
        x,y = self.coord
        u = 50
        pygame.draw.rect(fenetre, (255,255,255), (x, y, u, u))
        font = pygame.font.SysFont('KAZYcase scrabble', 50)
        font_chiffre = pygame.font.SysFont('KAZYcase scrabble', 25)
        lettre = font.render(self.nom, True, (0,0,0))
        points = font_chiffre.render(str(self.points),True,(0,0,0))
        fenetre.blit(lettre, self.coord)
        fenetre.blit(points,(self.coord[0]+30,self.coord[1]+30))

    def suivre_souris(self,fenetre):#permet que la lettre suive la souris lors de la sélection de la lettre
        lettre = font.render(self.nom, True, (0,0,0))
        position = pygame.mouse.get_pos()
        fenetre.blit(lettre, (position[0]-15,position[1]-15))
        return position
    # def verif_relachement_sur_lettre(self,x,y,u,mouse_x,mouse_y,lettre_select):
    #     return (x <= mouse_x <= x + u) and (y <= mouse_y <= y + u) and ((mouse_x,mouse_y) != lettre_select.coord)
historique_lettres = []
historique_cases = []
lettre_double_case = ["A4", "A12", "C7", "C9", "D1", "D8", "D15", "G3", "G7", "G9", "G13", "H4", "H12", "I3", "I7", "I9", "I13", "L1", "L8", "L15", "M7", "M9", "O4", "O12"]
lettre_triple_case = ["B6", "B10", "F2", "F6", "F10", "F14","J2","J6","J10","J14","N6","N10"]
mot_double_case = ["B2", "C3", "D4", "E5", "H8", "E11", "D12", "C13", "B14", "N2", "M3", "L4", "K5", "K11", "L12", "M13", "N14"]
mot_triple_case =["A1", "A8", "A15", "H1", "H15", "O1", "O8", "O15"]
#définition de toute les case spéciale
alphabet = ("Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M")
nombres = ("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16")
case_occupé = []
case_possible = [["H8"],[]]
compteur_lettre_poser_dans_tour = 0
nom_derniere_case_prise = None
case_poser_ce_tour = []

def case_adjacente_a_une_case(nom_case,alphabet,nombres):
    nom_case_lettre = nom_case[0]
    nom_case_nombre = nom_case[1:]
    pos_lettre_alph = alphabet.index(nom_case_lettre)
    pos_chiffre_nombre = nombres.index(nom_case_nombre)
    case_gauche = alphabet[pos_lettre_alph-1]+nom_case_nombre
    case_droite = alphabet[pos_lettre_alph+1]+nom_case_nombre
    case_haut = nom_case_lettre + (nombres[pos_chiffre_nombre+1])
    case_bas = nom_case_lettre+nombres[pos_chiffre_nombre-1]
    case_adjacentes_lettre = [case_gauche,case_droite]
    case_adjacentes_chiffre=[case_bas,case_haut]
    return case_adjacentes_lettre,case_adjacentes_chiffre

class Case_visuel:#définition de la class case visuel permettant de gérer leur viseul

    def __init__(self,nom,coord,hauteur,epaisseur):

        self.nom = nom
        self.coord = coord
        self.hauteur = hauteur
        self.epaisseur = epaisseur
        self.occupé = None
        self.tour_occupé = None
        def définir_couleur_case_bonus(nom_case) :
            global lettre_double_case,lettre_triple_case,mot_double_case,mot_triple_case
            if nom_case in lettre_double_case:
                return (135,206,235)
            elif nom_case in lettre_triple_case:
                return (0,0,139)
            elif nom_case == "H8":
                return (255,255,0)
            elif nom_case in mot_double_case :
                return (255, 192, 203)
            elif nom_case in mot_triple_case :
                return (255, 0, 0)
            return (255,255,255)
        self.couleur = définir_couleur_case_bonus(self.nom)
    def vérif_relachement_sur_case_plus_ajout_lettre(self,position,lettre_select,case_adjacentes_possible):#vérifie si la position de la souris lors du relachement corespond aux coordonées de la case
        coord_x , coord_y = self.coord[0],self.coord[1]
        global compteur_lettre_poser_total , case_occupé ,case_possible,compteur_lettre_poser_dans_tour,nom_derniere_case_prise,case_poser_ce_tour
        position_x,position_y = position[0],position[1]
        if (coord_x<= position_x <= coord_x+self.epaisseur) and (coord_y<= position_y <= coord_y+self.hauteur):
            if compteur_lettre_poser_total == 0 and self.nom != "H8":#si c'est la premiere lettre de la game elle doit etre au milieu (case jaune) c'est ce qui est vérif
                return False
            elif self.occupé == None:#ajoute la lettre glissé sur la case dans la case pour l'afficher et faire en sorte que l'on puisse plus ajouter de nvl lettre

                case_adjacentes_lettre,case_adjacentes_chiffre = case_adjacente_a_une_case(self.nom,alphabet,nombres)
                nom_case_lettre = self.nom[0]
                nom_case_nombre = self.nom[1:]
                pos_lettre_alph = alphabet.index(nom_case_lettre)
                pos_chiffre_nombre = nombres.index(nom_case_nombre)

                def une_case_adj_dans_case_occupé(case_adjacente,case_occupé):
                    for i in case_adjacente:
                        for u in i:
                            if u in case_occupé:
                                return True
                    return False
                def nom_case_dans_case_possible(nom_case,case_possible):
                    for i in case_possible:
                        if nom_case in i :
                            return True
                    return False
                def vérif_validité_case(nom_case_select,case_adjacentes_lettre ,case_adjacentes_chiffre ,case_occupé ,compteur_lettre_poser_dans_tour,case_possible,compteur_tour,case_poser_ce_tour):
                    if compteur_tour == 0 and compteur_lettre_poser_dans_tour == 0 :
                        return nom_case_select == "H8"
                    elif not(compteur_lettre_poser_dans_tour == 0):
                        return une_case_adj_dans_case_occupé([case_adjacentes_lettre,case_adjacentes_chiffre],case_occupé) and nom_case_dans_case_possible(nom_case_select,case_possible)
                    return False

                if vérif_validité_case(self.nom,case_adjacentes_lettre ,case_adjacentes_chiffre ,case_occupé ,compteur_lettre_poser_dans_tour,case_possible,compteur_tour,case_poser_ce_tour):
                    self.occupé = lettre_select
                    self.tour_occupé = compteur_tour
                    case_occupé.append(self.nom)

                    compteur_lettre_poser_total += 1
                    for i in nombres[1:-1]:
                        nom_case_a_test = nom_case_lettre+i
                        case_adjacentes_lettre,case_adjacentes_nombre = case_adjacente_a_une_case(nom_case_a_test,alphabet,nombres)
                        case_adjacente_a_case_a_test = case_adjacentes_lettre+case_adjacentes_nombre
                        for u in case_adjacente_a_case_a_test:
                            if u in case_occupé and nom_case_a_test not in case_possible[1]:
                                case_possible[1].append(nom_case_a_test)
                    for i in alphabet[0:-2]:
                        nom_case_a_test = i+nom_case_nombre
                        case_adjacentes_lettre,case_adjacentes_nombre = case_adjacente_a_une_case(nom_case_a_test,alphabet,nombres)
                        case_adjacente_a_case_a_test = case_adjacentes_lettre+case_adjacentes_nombre
                        for u in case_adjacente_a_case_a_test :
                            if u in case_occupé and (nom_case_a_test not in case_possible[0]):
                                case_possible[0].append(nom_case_a_test)

                    if not(compteur_lettre_poser_dans_tour == 0):
                        if nom_case_lettre == nom_derniere_case_prise[0]:
                            case_possible[0] = []
                        elif nom_case_nombre == nom_derniere_case_prise[1]:
                             case_possible[1] = []
                    compteur_lettre_poser_dans_tour += 1
                    nom_derniere_case_prise = [nom_case_lettre,nom_case_nombre]
                    return True


                elif not(compteur_tour == 0) and compteur_lettre_poser_dans_tour == 0 :#
                    if une_case_adj_dans_case_occupé([case_adjacentes_lettre,case_adjacentes_chiffre],case_occupé):
                        self.occupé = lettre_select
                        self.tour_occupé = compteur_tour
                        case_occupé.append(self.nom)
                        compteur_lettre_poser_total += 1
                        case_possible[0],case_possible[1] = case_adjacentes_lettre,case_adjacentes_chiffre
                        for i in nombres[1:-1]:
                            nom_case_a_test = nom_case_lettre+i
                            case_adjacentes_lettre,case_adjacentes_nombre = case_adjacente_a_une_case(nom_case_a_test,alphabet,nombres)
                            case_adjacente_a_case_a_test = case_adjacentes_lettre+case_adjacentes_nombre
                            for u in case_adjacente_a_case_a_test:
                                if u in case_occupé and nom_case_a_test not in case_possible[1]:
                                    case_possible[1].append(nom_case_a_test)
                        for i in alphabet[0:-2]:
                            nom_case_a_test = i+nom_case_nombre
                            case_adjacentes_lettre,case_adjacentes_nombre = case_adjacente_a_une_case(nom_case_a_test,alphabet,nombres)
                            case_adjacente_a_case_a_test = case_adjacentes_lettre+case_adjacentes_nombre
                            for u in case_adjacente_a_case_a_test :
                                if u in case_occupé and (nom_case_a_test not in case_possible[0]):
                                    case_possible[0].append(nom_case_a_test)
                    compteur_lettre_poser_dans_tour+=1
                    nom_derniere_case_prise = [nom_case_lettre,nom_case_nombre]
                    return True
                return False
    def afficher_case(self,fenetre):#permet d'afficher la case et la lettre dans cette case s'il y en a une
        x,y = self.coord[0], self.coord[1]
        u = 53
        pygame.draw.rect(fenetre, self.couleur, (x, y, u, u))
        if not(self.occupé == None):#vérifier si la case contient une lettre afin de l'afficher
            font_chiffre = pygame.font.SysFont('KAZYcase scrabble', 25)
            lettre = font.render(self.occupé.nom, True, (0,0,0))
            points = font_chiffre.render(str(self.occupé.points),True,(0,0,0))
            fenetre.blit(lettre, (x+9,y+9))
            fenetre.blit(points,(x+35,y+35))

compteur_tour_Joueur = 0
compteur_lettre_poser_total = 0
def création_de_la_partie(fenetre):
    font = pygame.font.SysFont('KAZYcase scrabble', 25)
    text = font.render("Combien de joueurs etes vous?", True, (255, 255, 255))
    text_2_j = font.render("2", True, (255, 255, 255))
    text_3_j = font.render("3", True, (255, 255, 255))
    text_4_j = font.render("4", True, (255, 255, 255))

    grand_carré = pygame.Rect(270, 310, 300, 150)
    carre_2_j = pygame.Rect(310, 425, 60, 35)
    carre_3_j = pygame.Rect(385, 425, 60, 35)
    carre_4_j = pygame.Rect(460, 425, 60, 35)

    pygame.draw.rect(fenetre, (0, 255, 0), grand_carré)
    fenetre.blit(text, text.get_rect(center = grand_carré.center))
    pygame.draw.rect(fenetre, (0, 0, 0), carre_2_j)
    fenetre.blit(text_2_j, text_2_j.get_rect(center = carre_2_j.center))
    pygame.draw.rect(fenetre, (0, 0, 0), carre_3_j)
    fenetre.blit(text_3_j, text_3_j.get_rect(center = carre_3_j.center))
    pygame.draw.rect(fenetre, (0, 0, 0), carre_4_j)
    fenetre.blit(text_4_j, text_4_j.get_rect(center = carre_4_j.center))

    continuer = True
    while continuer:
        fenetre.fill((128,128,128))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Pour quitter le jeu
                continuer = False
            elif event.type == pygame.MOUSEBUTTONDOWN:#quand l'utilisateur clique sur son clique gauche on récupere la mosition de la souris
                if carre_2_j.collidepoint(event.pos):
                    continuer = False
                    nbr_joueur = 2
                if carre_3_j.collidepoint(event.pos):
                    continuer = False
                    nbr_joueur = 3
                if carre_4_j.collidepoint(event.pos):
                    continuer = False
                    nbr_joueur = 4

        pygame.draw.rect(fenetre, (0, 255, 0), grand_carré)
        fenetre.blit(text, text.get_rect(center = grand_carré.center))
        pygame.draw.rect(fenetre, (0, 0, 0), carre_2_j)
        fenetre.blit(text_2_j, text_2_j.get_rect(center = carre_2_j.center))
        pygame.draw.rect(fenetre, (0, 0, 0), carre_3_j)
        fenetre.blit(text_3_j, text_3_j.get_rect(center = carre_3_j.center))
        pygame.draw.rect(fenetre, (0, 0, 0), carre_4_j)
        fenetre.blit(text_4_j, text_4_j.get_rect(center = carre_4_j.center))

        pygame.display.flip()
    joueurs = []
    for i in range (0,nbr_joueur):
        joueurs.append(Joueur("Joueur "+str(i)))
    return joueurs
def changer_tour():#permet de changer de joueur a chaque tour et donc de changer les lettres a afficher
    global nbr_joueur , compteur_tour_Joueur

    if (compteur_tour_Joueur + 1) > nbr_joueur-1 :
        compteur_tour_Joueur = 0
    else:
        compteur_tour_Joueur += 1
    Joueur_actuel = Joueurs[compteur_tour_Joueur]
    lettres = []
    for i in Joueur_actuel.letters:#création des objets lettres_visuel
        if i not in lettres:
            locals()[i.nom]=Lettres_visuel(i.nom,i.points)
            lettres.append(locals()[i.nom])
    épaisseur_et_hauteur_lettres = 50
    for i in range(len(lettres)):#création des coordonées des lettres
        x = (i * épaisseur_et_hauteur_lettres) + 230
        y = 870
        lettres[i].coord = (x,y)
    return lettres,Joueur_actuel
def cacher_ecran_changement_tour(fenetre):
    fenetre.fill((128,128,0))
    message_surface = font.render("cliquer pour continuer", True, (255, 255, 255))
    message_rect = message_surface.get_rect()
    message_rect.center = fenetre.get_rect().center
    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Pour quitter le jeu
                continuer = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                continuer = False
        fenetre.blit(message_surface, message_rect)
        pygame.display.flip()
def mot_valide_test():
    def remonter_premier_lettre(avance,case):
        place_case_dans_cases_existantes = cases_existantes.index(case)
        case_actuellement_test = case
        case_actuellement_test = cases_existantes[place_case_dans_cases_existantes-avance]
        index_case_actuellement_test = cases_existantes.index(case_actuellement_test)
        while not(case_actuellement_test.occupé == None) and index_case_actuellement_test-avance >=0 :
            case_actuellement_test = cases_existantes[index_case_actuellement_test-avance]
            index_case_actuellement_test = cases_existantes.index(case_actuellement_test)
        case_actuellement_test = cases_existantes[index_case_actuellement_test+avance]
        return case_actuellement_test
    def interpreter_le_mot(avance,case_actuellement_test,compteur_tour,continuee):
        prout = []
        mot_composé_actuellement = []
        while not(case_actuellement_test.occupé == None):
            index_case_actuellement_test_b = None

            mot_composé_actuellement.append(case_actuellement_test.occupé.nom)
            index_case_actuellement_test = cases_existantes.index(case_actuellement_test)
            case_actuellement_test = cases_existantes[index_case_actuellement_test+avance]
            if case_actuellement_test.tour_occupé == compteur_tour and continuee:
                mots_intermédiaire = []
                if avance == 1:
                    avance_2 = 15
                elif avance == 15:
                    avance_2 = 1

                if index_case_actuellement_test_b == None:
                    case_actuellement_test_b = cases_existantes[index_case_actuellement_test+avance]
                else :
                    case_actuellement_test_b = cases_existantes[index_case_actuellement_test_b+avance]
                case_actuellement_test_a = remonter_premier_lettre(avance_2,case_actuellement_test_b)
                mots_intermédiaire += interpreter_le_mot(avance_2,case_actuellement_test_a,compteur_tour,False)
                for p in mots_intermédiaire:
                    if p == []:
                        mots_intermédiaire.remove(p)
                index_case_actuellement_test_b = cases_existantes.index(case_actuellement_test_b)
                if len(mots_intermédiaire) > 1:
                    mot_composé_actuellement.append(mots_intermédiaire)
        if len(mot_composé_actuellement) > 1:
            # mot_principal=[[]]
            # for m in mot_composé_actuellement:
            #     if not(type(m) == list):
            #         mot_principal[0].append(m)
            #         mot_composé_actuellement.remove(m)
            # if not(mot_principal[0] == []):
            #     mot_composé_actuellement+= mot_principal
            # mot_composé_actuellement = [mot_composé_actuellement]
            # mot_composé_actuellement += [prout]
            #print(mot_composé_actuellement,prout)
            iei = []
            for i in mot_composé_actuellement:
                if type(i) == str:
                    iei.append(i)
                    #mot_composé_actuellement.remove(i)
            mot_composé_actuellement.append(iei)
            return mot_composé_actuellement
        return []

    mots_trouver = []
    global cases_existantes
    for i in cases_existantes:
        if i.tour_occupé == compteur_tour:
            place_case_dans_cases_existantes = cases_existantes.index(i)
            case_au_dessus = cases_existantes[place_case_dans_cases_existantes-15]
            case_a_gauche = cases_existantes[place_case_dans_cases_existantes-1]
            nom_case_lettre = i.nom[0]
            nom_case_nombre = i.nom[1:]
            if not(case_au_dessus == None) and not(nom_case_lettre == "A"):
                case_actuellement_test = remonter_premier_lettre(15,i)
                mots_trouver.append(interpreter_le_mot(15,case_actuellement_test,compteur_tour,True))
                # case_actuellement_test = i
                # case_actuellement_test = cases_existantes[place_case_dans_cases_existantes-15]
                # index_case_actuellement_test = cases_existantes.index(case_actuellement_test)
                # while not(case_actuellement_test.occupé == None) and index_case_actuellement_test-15 >=0 :
                #     case_actuellement_test = cases_existantes[index_case_actuellement_test-15]
                #     index_case_actuellement_test = cases_existantes.index(case_actuellement_test)
                # case_actuellement_test = cases_existantes[index_case_actuellement_test+15]
                # while not(case_actuellement_test.occupé == None):
                #     mot_composé_actuellement.append(case_actuellement_test.occupé.nom)
                #     index_case_actuellement_test = cases_existantes.index(case_actuellement_test)
                #     case_actuellement_test = cases_existantes[index_case_actuellement_test+15]
                # if len(mot_composé_actuellement) > 1:
                #     mots_trouver.append(mot_composé_actuellement)
            if not(case_au_dessus == None) and not(nom_case_lettre == "1"):
                case_actuellement_test = remonter_premier_lettre(1,i)
                mots_trouver.append(interpreter_le_mot(1,case_actuellement_test,compteur_tour,True))
                # mot_composé_actuellement = []
                # case_actuellement_test = i
                # case_actuellement_test = cases_existantes[place_case_dans_cases_existantes-1]
                # index_case_actuellement_test = cases_existantes.index(case_actuellement_test)
                # while not(case_actuellement_test.occupé == None) and index_case_actuellement_test-1 >=0 :
                #     case_actuellement_test = cases_existantes[index_case_actuellement_test-1]
                #     index_case_actuellement_test = cases_existantes.index(case_actuellement_test)
                # case_actuellement_test = cases_existantes[index_case_actuellement_test+1]
                # while not(case_actuellement_test.occupé == None):
                #     mot_composé_actuellement.append(case_actuellement_test.occupé.nom)
                #     index_case_actuellement_test = cases_existantes.index(case_actuellement_test)
                #     case_actuellement_test = cases_existantes[index_case_actuellement_test+1]
                #     if case_actuellement_test.tour_occupé == compteur_tour:
                #
                # if len(mot_composé_actuellement) > 1:
                #     mots_trouver.append(mot_composé_actuellement)
            break

    print("m=",mots_trouver)

pygame.init()
taille_fenetere = (840, 920)
fenetre = pygame.display.set_mode(taille_fenetere)
fenetre.fill((128,128,0))#couleur du fond
lettres = []
Joueurs = création_de_la_partie(fenetre)
nbr_joueur = len(Joueurs)
for u in Joueurs:
    u.add_letters()
for i in Joueurs[0].letters:#création des objets lettres_visuel
    if i not in lettres:
        locals()[i.nom]=Lettres_visuel(i.nom,i.points)
    lettres.append(locals()[i.nom])
épaisseur_et_hauteur_lettres = 50
for i in range(len(lettres)):#création des coordonée des lettres
    x = (i * épaisseur_et_hauteur_lettres) + 230
    y = 870
    lettres[i].coord = (x,y)

cases_existantes = []
coord = [0,-53]
for i in range(1, 16):#création des objets case_visuel avec les bonnes coordonées
    coord[1] += 55
    coord[0] = 5
    for j in range(ord('A'), ord('P')):
        nom = chr(j) + str(i)
        coord[0] += 2
        cases_existantes.append(Case_visuel(nom, (coord[0], coord[1] + 2), 50, 50))
        coord[0] += 53

font = pygame.font.SysFont('KAZYcase scrabble', 50)
pygame.display.flip()

#création de tout les boutons valide et de leurs texte associer
font_boutton = pygame.font.Font(None, 24)
button_tour_validé = pygame.Rect(625, 850, 150, 50)
text_valid = font_boutton.render("Valider votre mot", True, (255, 255, 255))
text_rect = text_valid.get_rect(center = button_tour_validé.center)
button_tour_passe = pygame.Rect(65, 850, 150, 50)
text_pass = font_boutton.render("passer votre tour", True, (255, 255, 255))
text_rect_pass = text_pass.get_rect(center = button_tour_passe.center)

image_poubelle = pygame.image.load("icons8-poubelle-50.png")
button_suppr_letres = pygame.Rect(0, 870, 50, 50)
text_rect_supr = text_pass.get_rect(center = button_suppr_letres.center)

image_fleche = pygame.image.load('icons8-flèche-bas-50.png')
button_ramene_lettre = pygame.Rect(775,850,50,50)
text_rect_supr = text_pass.get_rect(center = button_ramene_lettre.center)


#création des variables nécessaire pour la boucle principale
Joueur_actuel = Joueurs[0]
lettre_select= None
compteur_tour_une_action = None
compteur_tour = 0
autorisation_poser_lettre,autorisation_suppr_lettre,autorisation_passer_tour = True,True,True
case_adjacentes_possible = []
continuer = True
while continuer:#boucle principale du jeu
    fenetre.fill((128,128,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#Pour quitter le jeu
            continuer = False

        elif event.type == pygame.MOUSEBUTTONDOWN:#quand l'utilisateur clique sur son clique gauche on récupere la mosition de la souris
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_tour_validé.collidepoint(event.pos):#vérifie si l'utilisateur clique sur le bouton tour validé
                if mot_valide_test():
                    Joueur_actuel.add_letters()
                    lettres,Joueur_actuel = changer_tour(fe)

            elif button_tour_passe.collidepoint(event.pos):#vérifie si l'utilisateur clique sur le bouton passer le tour
                Joueur_actuel.add_letters()
                lettres,Joueur_actuel = changer_tour()
                cacher_ecran_changement_tour(fenetre)

                # compteur_tour += 1
                # autorisation_poser_lettre,autorisation_suppr_lettre = True,True
                # compteur_lettre_poser_dans_tour = 0
                #
                # historique_cases = []
                # historique_lettres
                # historique_joueur = None
                # for i in lettres :
                #     historique_lettres.append(i)
                # for u in cases_existantes :
                #     historique_cases.append(u)
                # historique_joueur = Joueur_actuel
            # elif button_ramene_lettre.collidepoint(event.pos):
            #     print("éaaa")
            #     aa = []
            #     bb = []
            #     cc = []
            #     for i in historique_lettres:
            #         aa.append(i.nom)
            #     for i in lettres:
            #         bb.append(i.nom)
            #     # print(aa)
            #     # print(bb)
            #     lettres = []
            #     for i in historique_lettres:
            #         lettres.append(i)
            #     pygame.draw.rect(fenetre, (0, 255, 0), pygame.Rect(230, 870, 350, 50))
            #     pygame.display.flip()
            #     for i in lettres:
            #         cc.append(i.nom)
            #     print(cc)
            #     for lettre in lettres :#affiche les lettres
            #         lettre.afficher_lettre(fenetre)
            #     break
            # print(cc)
            # Joueur_actuel = historique_joueur
            # cases_plateaux = historique_cases
            else:
                for i in lettres:#on verifie si ca correspond a la position d'une lettre et on stocke la lettre correspondante
                    x, y = i.coord
                    if (x <= mouse_x <= x + épaisseur_et_hauteur_lettres) and (y <= mouse_y <= y + épaisseur_et_hauteur_lettres):
                        lettre_select = i

        elif event.type == pygame.MOUSEBUTTONUP:#si l'utilisateur relache son clique gauche on recupere la position de la souris
            if lettre_select == None:#pour éviter cerrtain bug
                break
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if button_suppr_letres.collidepoint(event.pos) and autorisation_suppr_lettre :#si l'utilisateur relache la lettre sur la poubelle on supprime la lettre de la variable lettre et des lettres du joueur
                if lettre_select == None:#éviter certains bugs
                    break
                else :
                    autorisation_poser_lettre = False
                    autorisation_passer_tour = False
                    compteur_a = 0
                    for i in lettres :
                        compteur_a +=1
                        if i.nom == lettre_select.nom:
                            #lettres.remove(i)
                            #Joueur_actuel.letters.remove(i)
                            lettres.remove(lettres[compteur_a-1])
                            compteur_b = 0
                            for pp in Joueur_actuel.letters:
                                compteur_b += 1
                                if pp.nom == lettre_select.nom:
                                    Joueur_actuel.letters.remove(Joueur_actuel.letters[compteur_b-1])
                            break
            for i in lettres:#on vérifie que cette position correspond a la position d'une lettre et on les échanges permet donc de changer l'orde des lettres
                x, y = i.coord
                if (x <= mouse_x <= x + épaisseur_et_hauteur_lettres) and (y <= mouse_y <= y + épaisseur_et_hauteur_lettres) and ((mouse_x, mouse_y) != lettre_select.coord):
                    lettre_select.coord, i.coord = i.coord, lettre_select.coord
                    lettre_select= None
                    break
            if autorisation_poser_lettre :
                for i in cases_existantes:#vérifie que la position correspond a la position d'une case
                    if i.vérif_relachement_sur_case_plus_ajout_lettre((mouse_x,mouse_y),lettre_select,case_adjacentes_possible) :#vérifier si la case est occupé et ajout de la lettre dans la case si non
                        compteur = 0
                        for i in Joueur_actuel.letters:#supprime la lettre glissé des lettres du joeur et d'es lettres afficher
                            compteur += 1
                            if lettre_select.nom == i.nom:
                                Joueur_actuel.letters.remove(i)
                                lettres.remove(lettres[compteur-1])
                                autorisation_suppr_lettre = False
                                autorisation_passer_tour = False
                                break
                        break
            lettre_select = None

    #dessine tous les boutons
    pygame.draw.rect(fenetre, (0, 255, 0), button_tour_validé)
    pygame.draw.rect(fenetre, (0, 255, 0), button_tour_passe)
    fenetre.blit(text_valid, text_rect)
    fenetre.blit(text_pass, text_rect_pass)
    pygame.draw.rect(fenetre,(128, 128, 128),button_suppr_letres)
    fenetre.blit(image_poubelle, button_suppr_letres)
    pygame.draw.rect(fenetre,(255, 0, 0),button_ramene_lettre)
    fenetre.blit(image_fleche,button_ramene_lettre)
    for lettre in lettres :#affiche les lettres
        lettre.afficher_lettre(fenetre)
    if len(lettres)!=7:#si il a moins de 7 lettres les remets d'affilé pour éviter les trous dans le porte-lettres
        nombre_carre_noir = 7-len(lettres)
        x = 0
        for i in range (len(lettres)):
            x = (i * épaisseur_et_hauteur_lettres) + 230
            y = 870
            lettres[i].coord = (x,y)
        for i in range (1,nombre_carre_noir+1):
            x = 580 - (50 * i)
            y = 870
            pygame.draw.rect(fenetre, (128,128,0), (x, y, 50,50))
    ao = []
    for i in cases_existantes :#affiche les case
        i.afficher_case(fenetre)
        ao.append(i.nom)
        #i.occupé = lettre_select

    if not(lettre_select == None) :#si l'utilisateur selectionne une lettre on la fait suivre la souris
        lettre_select.suivre_souris(fenetre)
    #print(compteur_lettre_poser_dans_tour)
    pygame.display.flip()
