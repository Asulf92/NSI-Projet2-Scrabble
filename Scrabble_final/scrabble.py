import random,csv,pygame

class Joueur:#création d'une class Joueur contenant toutes les infos d'un joueur
    def __init__(self,nom):#création des stats de base du joueur
        self.points = 0
        self.letters = []
        self.nom = nom
        self.tour_consec=0
    def add_letters(self):#permet de faire piocher des lettre au joueur
        while len(self.letters) < 7:
            self.letters.append(sac.piocher_une_lettre())
    def remettre_en_orde(self,nouvel_ordre):#permet a l'utilisateur de remettre ses lettres dans l'orde qu'il veut
        self.letters = (list(nouvel_ordre))
        self.letters = []
        global lettres_possible
        for p in nouvel_ordre:
            for u in  lettres_possible:
                if p == u.nom:
                    self.letters.append(u)

class Lettres:#définition d'une class lettres visuel étant a part de la classe lettre et gérant juste la partie visuel des lettres
    def __init__(self,nom,points):
        self.nom = nom#nom est une chaine de caractère
        self.coord = (None,None)
        self.points = points
    def afficher_lettre(self,fenetre):#permet d'afficher la lettre a ses coordonée avec ses points
        x,y = self.coord
        u = 50
        pygame.draw.rect(fenetre, (255,255,255), (x, y, u, u),border_radius=1)
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

#Création des lettres possible avec le nombres de points correspondant
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
Joker = Lettres("_", 0)
lettres_possible.append(Joker)

class Sac: #création du sac contenant toutes les lettres et n'etant pas infini
    def __init__(self):#définition de toutes les lettres et de leur nombre présente au début du jeu
        self.lettres_dans_le_sac ={"pour condition":0,Joker:2,A: 9, B: 2, C: 2, D: 4, E: 12, F: 2, G: 3, H: 2,I: 9, J: 1, K: 1, L: 4, M: 2, N: 6, O: 8, P: 2,Q: 1, R: 6, S: 4, T: 6, U: 4, V: 2, W: 2, X: 1,Y: 2, Z: 1}
    def piocher_une_lettre(self):#permet de piocher une lettre aléatoire et du l'enlever du sac
        global Joueurs
        compteur_nombre_lettre_restante = 0
        for i in self.lettres_dans_le_sac.values():
            compteur_nombre_lettre_restante += i

        if compteur_nombre_lettre_restante !=0:
            lettre_piocher = "pour condition"
            lettre_a_piocher = []
            for i,u in self.lettres_dans_le_sac.items():
                if u != 0:
                    lettre_a_piocher.append(i)
                # elif lettre_a_piocher == []:
                #     afficher_vainqueur(joueurs)

            lettre_piocher = random.choice(lettre_a_piocher)
            self.lettres_dans_le_sac[lettre_piocher] -= 1
            return lettre_piocher
        else :
            afficher_vainqueur(Joueurs)
sac = Sac()

def mot_valible_verif(mot):#vérifier la validité d'un mot*
    global alphabet
    with open('mots_acceptes.csv', 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
                for a in alphabet:
                    if mot.replace("_",a).upper() in ligne:
                        print(mot.replace("_",a).upper())
                        return True
    return False

def ajouter_au_mot_valides(mot):#ajoute le mot aux mots valides
    print(mot)
    with open('mots_acceptes.csv', 'a', encoding='utf-8') as fichier:
        csv_writer = csv.writer(fichier)
        csv_writer.writerow([mot.upper(),"","","","",""])

def ajouter_aux_mots_invalide(mot):#ajoute le mot aux mots invalides
    with open('mots_refuses.csv', 'a', encoding='utf-8') as fichier:
        csv_writer = csv.writer(fichier)
        csv_writer.writerow([mot.upper(),"","","","",""])
#definition de toutes les variable nécessaire a certaine fonction
score_du_mot = 0
historique_lettres = []
historique_cases = []
lettre_double_case = ["A4", "A12", "C7", "C9", "D1", "D8", "D15", "G3", "G7", "G9", "G13", "H4", "H12", "I3", "I7", "I9", "I13", "L1", "L8", "L15", "M7", "M9", "O4", "O12"]
lettre_triple_case = ["B6", "B10", "F2", "F6", "F10", "F14","J2","J6","J10","J14","N6","N10"]
mot_double_case = ["B2", "C3", "D4", "E5", "H8", "E11", "D12", "C13", "B14", "N2", "M3", "L4", "K5", "K11", "L12", "M13", "N14"]
mot_triple_case =["A1", "A8", "A15", "H1", "H15", "O1", "O8", "O15"]
alphabet = ("Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N","O","P") #Z et P n'existent pas mais leur présence dans la liste et nécessaire pour après
nombres = ("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16") #Meme chose pour 0 et 16
case_occupé = []
case_possible = [["H8"],[]]
compteur_lettre_poser_dans_tour = 0
nom_derniere_case_prise = None
case_poser_ce_tour = []

#sera utiliser pour verifier si le joueur a le droit de poser une lttre sur un case
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

class Case:#définition de la classe case visuel permettant de gérer leur visuel
    def __init__(self,nom,coord,hauteur,epaisseur):
        self.nom = nom
        self.coord = coord
        self.hauteur = hauteur
        self.epaisseur = epaisseur
        self.occupé = None
        self.tour_occupé = None
        if self.nom in lettre_double_case:#definition de toutes les cases avec des bonus et de leur caractéristiques
            self.couleur = (55, 197, 250)
            self.multiplicateur_lettre = 2
            self.multiplicateur_mot = 1
        elif self.nom in lettre_triple_case:
            self.couleur = (0,20,170)
            self.multiplicateur_lettre = 3
            self.multiplicateur_mot = 1
        elif self.nom == "H8":
            self.multiplicateur_lettre = 1
            self.multiplicateur_mot = 2
            self.couleur = (255,255,0)
        elif self.nom in mot_double_case :
            self.multiplicateur_lettre = 1
            self.multiplicateur_mot = 2
            self.couleur = (174, 135, 196)
        elif self.nom in mot_triple_case :
            self.multiplicateur_lettre = 1
            self.multiplicateur_mot = 3
            self.couleur = (220,0,0)
        else:
            self.multiplicateur_lettre = 1
            self.multiplicateur_mot = 1
            self.couleur = (255,255,255)

    def verif_autorisation_poser_et_ajout_de_la_lettre_dans_la_case(self,position,lettre_select,case_adjacentes_possible):#vérifie si la position de la souris lors du relachement corespond aux coordonées de la case
        def case_adj_dans_case_occupé(case_adjacente,case_occupé):
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
        def verif_autorisation_de_poser(nom_case_select,case_adjacentes_lettre ,case_adjacentes_chiffre ,case_occupé ,compteur_lettre_poser_dans_tour,case_possible,compteur_tour,case_poser_ce_tour):
            if compteur_tour == 0 and compteur_lettre_poser_dans_tour == 0 :
                return nom_case_select == "H8"
            elif not(compteur_lettre_poser_dans_tour == 0):
                return case_adj_dans_case_occupé([case_adjacentes_lettre,case_adjacentes_chiffre],case_occupé) and nom_case_dans_case_possible(nom_case_select,case_possible)
            return False

        coord_x , coord_y = self.coord[0],self.coord[1]
        global compteur_lettre_poser_total , case_occupé ,case_possible,compteur_lettre_poser_dans_tour,nom_derniere_case_prise,case_poser_ce_tour,case_occupé_ce_tour
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
                if verif_autorisation_de_poser(self.nom,case_adjacentes_lettre ,case_adjacentes_chiffre ,case_occupé ,compteur_lettre_poser_dans_tour,case_possible,compteur_tour,case_poser_ce_tour):
                    index_case_occupé_ce_tour = cases_existantes.index(self)
                    case_occupé_ce_tour.append(index_case_occupé_ce_tour)
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
                    if case_adj_dans_case_occupé([case_adjacentes_lettre,case_adjacentes_chiffre],case_occupé):
                        index_case_occupé_ce_tour = cases_existantes.index(self)
                        case_occupé_ce_tour.append(index_case_occupé_ce_tour)
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
        pygame.draw.rect(fenetre, self.couleur, (x, y, u, u),border_radius=2)
        if not(self.occupé == None):#vérifier si la case contient une lettre afin de l'afficher
            font_chiffre = pygame.font.SysFont('KAZYcase scrabble', 25)
            lettre = font.render(self.occupé.nom, True, (0,0,0))
            points = font_chiffre.render(str(self.occupé.points),True,(0,0,0))
            fenetre.blit(lettre, (x+9,y+9))
            fenetre.blit(points,(x+35,y+35))


def création_de_la_partie(fenetre):
    global taille_y,taille_x,couleur_fond
    pygame.display.set_caption("SCRABBLE")
    font = pygame.font.SysFont('KAZYcase scrabble', 25)
    font2=pygame.font.SysFont('KAZYcase scrabble', 35)
    font3=pygame.font.SysFont('KAZYcase scrabble', 45)
    font4=pygame.font.SysFont('KAZYcase scrabble', 100)

    carre_2_j = pygame.Rect(((taille_x-60)/2)-120,((taille_y-35)/2-100), 60, 50)
    carre_3_j = pygame.Rect(((taille_x-60)/2),((taille_y-35)/2-100), 60, 50)
    carre_4_j = pygame.Rect(((taille_x-60)/2)+120,((taille_y-35)/2-100), 60, 50)

    continuer = True
    while continuer: #Affichages des règles / choses à savoir
        fenetre.fill(couleur_fond)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                continuer=False
            if event.type==pygame.KEYDOWN:
                continuer=False

        règles=font4.render("Règles :", True, (255, 255, 255))
        fenetre.blit(règles,(((taille_x-règles.get_width())/2), 30))

        règle11=font3.render("-Il faut d'abord avoir défaussé", True, (255, 255, 255))
        règle12=font3.render(" une tuile pour passer son tour :", True, (255, 255, 255))
        image_poubelle = pygame.transform.scale(pygame.image.load("poubelle.png"),(80,70))
        fenetre.blit(règle11,(((taille_x-règle11.get_width())/2)-50,150))
        fenetre.blit(règle12,(((taille_x-règle12.get_width())/2)-50,185))
        fenetre.blit(image_poubelle,(((taille_x-règles.get_width())/2)+325,145))

        règle21=font3.render("-Pour ramener les tuiles défaussées ou", True, (255, 255, 255))
        règle22=font3.render(" placées ce tour vers votre chevalet :", True, (255, 255, 255))
        image_fleche = pygame.transform.scale(pygame.image.load('icons8-flèche-bas-50.png'),(70,68))
        rouge = pygame.Rect(((taille_x-67)/2)+260,267,67,70)
        pygame.draw.rect(fenetre,(180,0,0),rouge,border_radius=10)
        fenetre.blit(règle21,(((taille_x-règle21.get_width())/2)-80,270))
        fenetre.blit(règle22,(((taille_x-règle22.get_width())/2)-80,305))
        fenetre.blit(image_fleche,image_fleche.get_rect(center = rouge.center))

        règle31=font3.render("-La partie se termine quand il n'y a plus de ", True, (255, 255, 255))
        règle32=font3.render(" tuiles dans le sac ou à la fin du tour après ", True, (255, 255, 255))
        règle33=font3.render(" qu'un joueur ait passer son tour 3 fois", True, (255, 255, 255))
        fenetre.blit(règle31,(((taille_x-règle31.get_width())/2)-20,390))
        fenetre.blit(règle32,(((taille_x-règle32.get_width())/2)-20,425))
        fenetre.blit(règle33,(((taille_x-règle33.get_width())/2)-20,460))

        valider=font3.render("Appuyer sur une touche pour continuer",True, (255, 255, 255))
        valide = pygame.Rect((taille_x-610)/2,taille_y-100,610,55)
        pygame.draw.rect(fenetre,(0,130,0),valide,border_radius=14)
        fenetre.blit(valider,valider.get_rect(center = valide.center))

        pygame.display.flip()

    continuer = True
    while continuer: #Choix du nombre de joueur
        fenetre.fill(couleur_fond)
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

        text = font3.render("Combien de joueurs êtes vous?", True, (255, 255, 255))
        text_2_j = font2.render("2", True, (255, 255, 255))
        text_3_j = font2.render("3", True, (255, 255, 255))
        text_4_j = font2.render("4", True, (255, 255, 255))

        fenetre.blit(text, ((taille_x-text.get_width())/2,(taille_y-text.get_height())/2-20))


        pygame.draw.rect(fenetre, (0, 0, 0), carre_2_j,border_radius=10)
        fenetre.blit(text_2_j, text_2_j.get_rect(center = carre_2_j.center))
        pygame.draw.rect(fenetre, (0, 0, 0), carre_3_j,border_radius=10)
        fenetre.blit(text_3_j, text_3_j.get_rect(center = carre_3_j.center))
        pygame.draw.rect(fenetre, (0, 0, 0), carre_4_j,border_radius=10)
        fenetre.blit(text_4_j, text_4_j.get_rect(center = carre_4_j.center))

        pygame.display.flip()

    nom_carré=pygame.Rect((taille_x-400)/2,((taille_y-30)/2)-100, 400, 30)
    nomjoueur=''
    continuer=True
    joueurs=[]
    nomsjoueurs=[]
    r=0
    while continuer and r!=nbr_joueur: #Choix des pseudos des joueurs
        fenetre.fill(couleur_fond)
        text=font3.render(" Entrez le nom des joueurs dans l'ordre",True,(255,255,255))
        text2=font3.render("des tours (8 caractères maximum)",True,(255,255,255))
        fenetre.blit(text,(((taille_x-text.get_width())/2),((taille_y-text.get_height())/2)-45))
        fenetre.blit(text2,(((taille_x-text2.get_width())/2),((taille_y-text2.get_height())/2)))
        for i in range (0,nbr_joueur):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    continuer=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                        if len(nomjoueur)<=8:
                            if nomjoueur=="":
                                nomjoueur=f"Joueur {r+1}"
                            nomsjoueurs.append(nomjoueur)
                            nomjoueur=""
                            r+=1
                        else:
                            nomjoueur=""
                    elif event.key==pygame.K_BACKSPACE:
                        nomjoueur=nomjoueur[:-1]
                    else:
                        nomjoueur+=event.unicode
        if len(nomjoueur)>8:
            text_affiché=font.render(nomjoueur+"| Invalide (trop long) ",True,(255,130,130))
        else:
            text_affiché=font.render(nomjoueur+"|",True,(255,255,255))
        fenetre.blit(text_affiché,(((taille_x-400)/2)+6,((taille_y-30)/2)-94))
        pygame.draw.rect(fenetre,(255,255,255),nom_carré,3)
        pygame.display.flip()
    for i in range (0,nbr_joueur):
        joueurs.append(Joueur(nomsjoueurs[i]))
    return joueurs

def changer_tour():#permet de changer de joueur a chaque tour et donc de changer les lettres a afficher
    global nbr_joueur,historique_point_Joueur ,compteur_tour,autorisation_passer_tour, compteur_tour_Joueur,case_occupé,historique_cases_occupé , case_occupé_ce_tour,historique_lettres

    historique_cases_occupé = list(case_occupé)
    case_occupé_ce_tour = []
    if (compteur_tour_Joueur + 1) > nbr_joueur-1 :
        compteur_tour_Joueur = 0
    else:
        compteur_tour_Joueur += 1
    Joueur_actuel = Joueurs[compteur_tour_Joueur]
    historique_point_Joueur=Joueur_actuel.points
    lettres = []
    autorisation_passer_tour=False
    for i in Joueur_actuel.letters:#création des objets lettres_visuel
        épaisseur_et_hauteur_lettres = 50
        if i not in lettres:
            locals()[i.nom]=Lettres(i.nom, i.points)
            lettres.append(locals()[i.nom])
    épaisseur_et_hauteur_lettres = 50
    Joueur_actuel.letters.append(locals()[i.nom])
    for i in range(len(lettres)):#création des coordonées des lettres
        x = (i * épaisseur_et_hauteur_lettres) + 285
        y = 840
        lettres[i].coord = (x,y)
    historique_lettres = list(lettres)
    return lettres,Joueur_actuel

def cacher_ecran_changement_tour(fenetre): #afficher un ecran noir a chaque changement de tour pour éviter la triche
    fenetre.fill(couleur_fond)
    voyelles=("a","e","i","o","u","y")
    if Joueur_actuel.nom.lower()!="":
        if Joueur_actuel.nom.lower()[0] in voyelles:
            message_surface = font.render(f"Au tour d'{Joueur_actuel.nom}", True, (255, 255, 255))
        else :
            message_surface = font.render(f"Au tour de {Joueur_actuel.nom}", True, (255, 255, 255))
    else :
        message_surface = font.render(f"Au tour du joueur suivant", True, (255, 255, 255))
    continuer = True
    texte_x = (fenetre.get_width() - message_surface.get_width()) // 2
    texte_y = (fenetre.get_height() - message_surface.get_height()) // 2
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Pour quitter le jeu
                continuer = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                continuer = False
        fenetre.blit(message_surface,(texte_x,texte_y-50))
        pygame.display.flip()

def test_mot_valide():
    def trouver_mot_ecris():

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
            mots_comp = []
            score_du_mot = 0
            multiplicateur_du_mot = 1
            mot_composé_actuellement = []
            while not(case_actuellement_test.occupé == None):
                index_case_actuellement_test_b = None

                mot_composé_actuellement.append(case_actuellement_test.occupé.nom)
                score_du_mot += case_actuellement_test.occupé.points * case_actuellement_test.multiplicateur_lettre
                multiplicateur_du_mot *= case_actuellement_test.multiplicateur_mot

                index_case_actuellement_test = cases_existantes.index(case_actuellement_test)
                if index_case_actuellement_test+avance<=225:
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
                        if not(mots_intermédiaire==[]):
                            mots_comp += mots_intermédiaire
                else :
                    break
            if len(mot_composé_actuellement) > 1:
                Joueur_actuel.points += score_du_mot*multiplicateur_du_mot
                mot_composé_actuellement = [mot_composé_actuellement]
                mot_composé_actuellement += mots_comp
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
                    mot_trouver = interpreter_le_mot(15,case_actuellement_test,compteur_tour,True)
                    mots_trouver.append(mot_trouver)
                if not(case_au_dessus == None) and not(nom_case_lettre == "1"):
                    case_actuellement_test = remonter_premier_lettre(1,i)
                    mots_trouver.append(interpreter_le_mot(1,case_actuellement_test,compteur_tour,True))
                break
        # if len(mots_trouver[1]) == 0 or len(mots_trouver[1]) == 0:
        #     return []
        if len(mots_trouver[0]) > len(mots_trouver[1]):
            mots_trouver = mots_trouver[0]
        elif len(mots_trouver[1])>len(mots_trouver[0]):
            mots_trouver = mots_trouver[1]
        return mots_trouver

    def vérif_validité_des_mots(lst_mots):
        print(lst_mots)
        for mot in lst_mots:
            mot_test_actuel = ""
            for lettre in mot:
                if not(type(lettre) == list):#empecher certain bug
                    mot_test_actuel += lettre
                else:
                    return False
            if mot_valible_verif(mot_test_actuel):
                return True
            else :

                compteurMotAccept = 0
                font = pygame.font.SysFont('KAZYcase scrabble', 35)
                font2 = pygame.font.SysFont('KAZYcase scrabble', 45)
                text = font2.render(f"Voulez vous ajouter ce mot au dictionnaire : {mot_test_actuel} ?", True, (255, 255, 255))
                text_oui = font.render("oui", True, (255, 255, 255))
                text_non = font.render("non", True, (255, 255, 255))
                carr_oui = pygame.Rect((taille_x-80)/2-55, (taille_y-55)/2, 63, 45)
                carr_non = pygame.Rect((taille_x-80)/2+55, (taille_y-55)/2, 63, 45)

                continuer = True
                while continuer:
                    fenetre.fill(couleur_fond)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:#Pour quitter le jeu
                            continuer = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:#quand l'utilisateur clique sur son clique gauche on récupere la mosition de la souris
                            if carr_oui.collidepoint(event.pos):
                                ajouter_au_mot_valides(mot_test_actuel)
                                compteurMotAccept +=1
                                if compteurMotAccept == len(lst_mots):
                                    return True
                                continuer = False
                            if carr_non.collidepoint(event.pos):
                                ajouter_aux_mots_invalide(mot_test_actuel)
                                retour_debut_du_tour()
                                return False

                    fenetre.blit(text, ((taille_x-text.get_width())/2,(taille_y-text.get_height())/2-70))
                    pygame.draw.rect(fenetre, (0,0,0), carr_oui,border_radius=15)
                    fenetre.blit(text_oui, text_oui.get_rect(center = carr_oui.center))
                    pygame.draw.rect(fenetre, (0, 0, 0), carr_non,border_radius=15)
                    fenetre.blit(text_non, text_non.get_rect(center = carr_non.center))
                    pygame.display.flip()

    a = trouver_mot_ecris()
    return vérif_validité_des_mots(a)
#permet de revenir au début du tour en cas de mot non valide ou si le joueur clique sur le bouton
def retour_debut_du_tour():
    global lettres,historique_point_Joueur,Joueur_actuel,case_occupé,case_occupé_ce_tour,historique_lettres,compteur_lettre_poser_dans_tour,autorisation_passer_tour,autorisation_poser_lettre,autorisation_suppr_lettre
    Joueur_actuel.points=historique_point_Joueur
    for i in case_occupé_ce_tour:
        cases_existantes[i].occupé = None
    case_occupé_ce_tour = []
    lettres = []
    Joueur_actuel.letters = []
    for i in historique_lettres:#création des objets lettres_visuel
        if i not in lettres:
            locals()[i.nom]=Lettres(i.nom, i.points)
            lettres.append(locals()[i.nom])
            Joueur_actuel.letters.append(locals()[i.nom])
    épaisseur_et_hauteur_lettres = 50
    for i in range(0,len(lettres)):#création des coordonée des lettres
        x = (i * épaisseur_et_hauteur_lettres) + 285
        y = 840
        lettres[i].coord = (x,y)
    case_occupé = historique_cases_occupé
    compteur_lettre_poser_dans_tour = 0
    autorisation_poser_lettre = True
    autorisation_suppr_lettre = True
    autorisation_passer_tour = False

def definir_couleur_bouton_passer_tour(autorisation_passer_tour):
    if autorisation_passer_tour :
        return (70, 201, 31)
    else:
        return (105,105,105)

def verif_autorisation_valid_mot(compteur_lettre_poser_dans_tour,compteur_tour):
    return (compteur_lettre_poser_dans_tour >= 2 and compteur_tour == 0) or (compteur_lettre_poser_dans_tour >=1 and not(compteur_tour==0))

def definir_couleur_bouton_valider_mot(compteur_lettre_poser_tour,compteur_tour):
    if verif_autorisation_valid_mot(compteur_lettre_poser_dans_tour,compteur_tour) :
        return (70, 201, 31)
    else:
        return (105,105,105)

def afficher_points_joueurs(fenetre):
    y_points=100
    entete_points = pygame.font.SysFont('KAZYcase scrabble', 52).render("Scores", True, (255,255,255))
    pygame.draw.rect(fenetre, (5,25,15), pygame.Rect(845, 25, 190, (len(Joueurs)+1)*70 +5),border_radius=8)
    fenetre.blit(entete_points, (878,45))

    for i in Joueurs:
        points=i.nom+" : "+str(i.points)
        texte_points = font_pts.render(points, True, (255,255,255))
        pygame.draw.rect(fenetre, (10,50,25), pygame.Rect(860, y_points, 160, 50),border_radius=8)
        fenetre.blit(texte_points, texte_points.get_rect(center = pygame.Rect(860, y_points, 150, 50).center))
        y_points+=70

def afficher_aide(fenetre): #affichage des aides pour correspondance multiplicateurs<=>couleurs
    font_aide=pygame.font.SysFont('KAZYcase scrabble', 23)

    entete_aides = pygame.font.SysFont('KAZYcase scrabble', 50).render("Aides", True, (255,255,255))
    pygame.draw.rect(fenetre, (5,25,15), pygame.Rect(845, 400, 190, 355),border_radius=8)
    fenetre.blit(entete_aides, (878,420))

    texteldb = font_aide.render("Lettre compte double", True, (0,0,0))
    pygame.draw.rect(fenetre, (55, 197, 250), pygame.Rect(860, 470, 160, 50),border_radius=8)
    fenetre.blit(texteldb, texteldb.get_rect(center = pygame.Rect(860, 470, 160, 50).center))

    textelct = font_aide.render("Lettre compte triple", True, (250,250,250))
    pygame.draw.rect(fenetre, (0,20,170), pygame.Rect(860, 540, 160, 50),border_radius=8)
    fenetre.blit(textelct, textelct.get_rect(center = pygame.Rect(860, 540, 160, 50).center))

    textemcd = font_aide.render("Mot compte double", True, (0,0,0))
    pygame.draw.rect(fenetre, (174, 135, 196), pygame.Rect(860, 610, 160, 50),border_radius=8)
    fenetre.blit(textemcd, textelct.get_rect(center = pygame.Rect(860, 610, 160, 50).center))

    textemct = font_aide.render("Mot compte triple", True, (250,250,250))
    pygame.draw.rect(fenetre, (190, 0, 0), pygame.Rect(860, 680, 160, 50),border_radius=8)
    fenetre.blit(textemct, textelct.get_rect(center = pygame.Rect(860, 680, 170, 50).center))

def afficher_les_boutons(fenetre,button_tour_validé,button_tour_passe,button_suppr_letres,button_ramene_lettre,button_fin_partie):
    font_boutton = pygame.font.Font(None, 45)
    font_boutton2 = pygame.font.Font(None, 35)
    text_valid = font_boutton.render("Valider", True, (255, 255, 255))
    text_rect = text_valid.get_rect(center = button_tour_validé.center)
    text_pass = font_boutton.render("Passer", True, (255, 255, 255))
    text_rect_pass = text_pass.get_rect(center = button_tour_passe.center)
    image_poubelle = pygame.transform.scale(pygame.image.load("poubelle.png"),(67,65))
    text_rect_supr = text_pass.get_rect(center = button_suppr_letres.center)
    image_fleche = pygame.transform.scale(pygame.image.load('icons8-flèche-bas-50.png'),(70,68))
    text_rect_supr = text_pass.get_rect(center = button_ramene_lettre.center)
    pygame.draw.rect(fenetre, definir_couleur_bouton_valider_mot(compteur_lettre_poser_dans_tour,compteur_tour), button_tour_validé,border_radius=8)
    pygame.draw.rect(fenetre, definir_couleur_bouton_passer_tour(autorisation_passer_tour), button_tour_passe,border_radius=8)
    fenetre.blit(text_valid, text_rect)
    fenetre.blit(text_pass, text_rect_pass)
    pygame.draw.rect(fenetre,(90, 90, 90),button_suppr_letres,border_radius=8)
    fenetre.blit(image_poubelle, button_suppr_letres)
    pygame.draw.rect(fenetre,(220,0,0),button_ramene_lettre,border_radius=8)
    fenetre.blit(image_fleche,button_ramene_lettre)
    text_joueur=font_boutton2.render(Joueur_actuel.nom, True, (255, 255, 255))
    rect=pygame.Rect(350,898, 220, 30)
    rectt=pygame.draw.rect(fenetre,(0,50,0),rect,border_radius=8)
    fenetre.blit(text_joueur,text_joueur.get_rect(center = rectt.center))

def afficher_vainqueur(joueurs):
    BLANC = (255, 255, 255)
    NOIR = (0, 0, 0)
    taille_fenetre = (1040, 920)
    fenetre = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Affichage du vainqueur")

    points_max = max([joueur.points for joueur in joueurs])
    joueurs_points_max = [joueur for joueur in joueurs if joueur.points == points_max]

    if len(joueurs_points_max) == 1: #Si il y a un gagnant
        vainqueur = joueurs_points_max[0]
        points_vainqueur = vainqueur.points
        nom_vainqueur = vainqueur.nom

        font = pygame.font.SysFont(None, 60)
        texte = font.render(f"{nom_vainqueur} a gagné !", True, NOIR)
        fenetre.fill(BLANC)
        fenetre.blit(texte, ((taille_x-texte.get_width())/2,100))


    else: #si il y en a plusieur
        font = pygame.font.SysFont(None, 50)
        fenetre.fill(BLANC)
        if len(joueurs_points_max)==2:
            text=f"{joueurs_points_max[0].nom} et {joueurs_points_max[1].nom} sont à égalité !"
        if len(joueurs_points_max)==3:
            text=f"{joueurs_points_max[0].nom}, {joueurs_points_max[1].nom} et {joueurs_points_max[2].nom} sont à égalité !"
        if len(joueurs_points_max)==4:
            text=f"Vous êtes tous à égalité !"
        texte=font.render(text,True, (0,0,0))
        fenetre.blit(texte, ((taille_x-texte.get_width())/2, 100))


    entete_points = pygame.font.SysFont('KAZYcase scrabble', 52).render("Tableau des scores", True, (255,255,255))
    pygame.draw.rect(fenetre, (5,25,15), pygame.Rect((taille_x-700)/2, 240, 700, (len(Joueurs)+1)*85 +65),border_radius=16)
    fenetre.blit(entete_points,((taille_x-entete_points.get_width())/2,275))


    rectpts=pygame.Rect((taille_x-700)/2+50,340, 600, 85*len(Joueurs))
    pygame.draw.rect(fenetre, (10,50,25), rectpts ,border_radius=20)

    y_points=380

    joueurs_tries = sorted(joueurs, key=lambda joueur: joueur.points, reverse=True)

    for i in joueurs_tries:
        points=i.nom+"  :  "+str(i.points)+" points"
        texte_points = pygame.font.SysFont('KAZYcase scrabble', 35).render(points, True, (255,255,255))
        fenetre.blit(texte_points,((taille_x-texte_points.get_width())/2,y_points))
        y_points+=75



    pygame.display.flip()

    en_attente = True
    while en_attente:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_attente = False

    pygame.quit()

def verif_fin_de_partie():
    if Joueur_actuel.tour_consec==3:
        afficher_vainqueur(Joueurs)

pygame.init()
taille_x=1050
taille_y=935
fenetre = pygame.display.set_mode((taille_x,taille_y))
couleur_fond = (30,75,40)
fenetre.fill(couleur_fond)#couleur du fond
Joueurs = création_de_la_partie(fenetre)
Joueur_actuel = Joueurs[0]

nbr_joueur = len(Joueurs)
for u in Joueurs:
    u.add_letters()
for i in Joueurs[0].letters:#création des objets lettres_visuel
    lettres = []
for i in Joueur_actuel.letters:#création des objets lettres_visuel
    if i not in lettres:
        locals()[i.nom]=Lettres(i.nom, i.points)
        lettres.append(locals()[i.nom])

épaisseur_et_hauteur_lettres = 50
for i in range(len(lettres)):#création des coordonée des lettres
    x = (i * épaisseur_et_hauteur_lettres) + 285
    y = 840
    lettres[i].coord = (x,y)
    Joueur_actuel.letters[i].coord = (x,y)

cases_existantes = []
coord = [0,-53]
for i in range(1, 16):#création des objets case_visuel avec les bonnes coordonées
    coord[1] += 55
    coord[0] = 5
    for j in range(ord('A'), ord('P')):
        nom = chr(j) + str(i)
        coord[0] += 2
        cases_existantes.append(Case(nom, (coord[0], coord[1] + 2), 50, 50))
        coord[0] += 53

font_pts = pygame.font.SysFont('KAZYcase scrabble', 30)
font = pygame.font.SysFont('KAZYcase scrabble', 50)
pygame.display.flip()

#création de tout les variables nécessaire pour le fonctionnement du jeu

button_fin_partie = pygame.Rect(850, 845, 175, 70)
button_mot_validé = pygame.Rect(735, 845, 175, 70)
button_tour_passe = pygame.Rect(95, 845, 175,  70)
button_suppr_letres = pygame.Rect(10, 845, 70, 70)
button_ramene_lettre = pygame.Rect(650,845,70, 70)
compteur_tour_Joueur = 0
compteur_lettre_poser_total = 0
lettre_select= None
compteur_tour_une_action = None
compteur_tour = 0
autorisation_poser_lettre,autorisation_suppr_lettre = True,True
case_adjacentes_possible = []
continuer = True
historique_cases = list(cases_existantes)
historique_lettres = list(lettres)
historique_cases_occupé = list(case_occupé)
historique_point_Joueur = Joueur_actuel.points
case_occupé_ce_tour = []
autorisation_passer_tour = False

while continuer:#boucle principale du jeu
    fenetre.fill(couleur_fond)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#Pour quitter le jeu
            continuer = False
        elif event.type == pygame.MOUSEBUTTONDOWN:#quand l'utilisateur clique sur son clique gauche on récupere la position de la souris
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_mot_validé.collidepoint(event.pos) and verif_autorisation_valid_mot(compteur_lettre_poser_dans_tour, compteur_tour):#vérifie si l'utilisateur clique sur le bouton tour validé
                if test_mot_valide():
                    if compteur_lettre_poser_dans_tour == 7:
                        Joueur_actuel.points += 50
                    Joueur_actuel.add_letters()
                    lettres,Joueur_actuel = changer_tour()
                    cacher_ecran_changement_tour(fenetre)
                    compteur_tour += 1
                    autorisation_poser_lettre,autorisation_suppr_lettre = True,True
                    compteur_lettre_poser_dans_tour = 0

            elif button_tour_passe.collidepoint(event.pos) and autorisation_passer_tour:#vérifie si l'utilisateur clique sur le bouton passer le tour
                Joueur_actuel.add_letters()
                Joueur_actuel.tour_consec+=1
                lettres,Joueur_actuel = changer_tour()
                cacher_ecran_changement_tour(fenetre)
                compteur_tour += 1
                autorisation_poser_lettre,autorisation_suppr_lettre = True,True
                compteur_lettre_poser_dans_tour = 0
            elif button_ramene_lettre.collidepoint(event.pos):
                retour_debut_du_tour()
            else:
                for i in lettres:#on verifie si ca correspond a la position d'une lettre et on stocke la lettre correspondante
                    x, y = i.coord
                    if (x <= mouse_x <= x + épaisseur_et_hauteur_lettres) and (y <= mouse_y <= y + épaisseur_et_hauteur_lettres):
                        lettre_select = i

        elif event.type == pygame.MOUSEBUTTONUP:
            if lettre_select == None:#pour éviter certain bug
                break
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if button_suppr_letres.collidepoint(event.pos) and autorisation_suppr_lettre :
                if compteur_tour!=0 :
                    autorisation_poser_lettre = False
                    autorisation_passer_tour = True
                    compteur_a = 0
                    for i in lettres :
                        compteur_a +=1
                        if i.nom == lettre_select.nom:
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
                for case in cases_existantes:
                    if case.verif_autorisation_poser_et_ajout_de_la_lettre_dans_la_case((mouse_x,mouse_y),lettre_select,case_adjacentes_possible) :#vérifier si la case est occupé et ajout de la lettre dans la case si non
                        compteur = 0
                        autorisation_passer_tour = False
                        for lettre in Joueur_actuel.letters:#supprime la lettre glissé des lettres du joeur et d'es lettres afficher
                            compteur += 1
                            if lettre_select.nom == lettre.nom:
                                Joueur_actuel.letters.remove(lettre)
                                lettres.remove(lettres[compteur-1])
                                autorisation_suppr_lettre = False
                                break
                        break
            lettre_select = None

    afficher_les_boutons(fenetre, button_mot_validé, button_tour_passe, button_suppr_letres, button_ramene_lettre,button_fin_partie)
    afficher_points_joueurs(fenetre)
    afficher_aide(fenetre)
    verif_fin_de_partie()

    for lettre in lettres :
        lettre.afficher_lettre(fenetre)
    #si il a moins de 7 lettres change les coordonées afin d'eviter les trous entre les lettres
    if len(lettres)!=7:
        nombre_carre_noir = 7-len(lettres)
        x = 0
        for i in range (len(lettres)):
            x = (i * épaisseur_et_hauteur_lettres) + 285
            y = 840
            lettres[i].coord = (x,y)
        for i in range (1,nombre_carre_noir+1):
            x = 635 - (50 * i)
            y = 840
            pygame.draw.rect(fenetre, couleur_fond, (x, y, 50,50))

    for i in cases_existantes :
        i.afficher_case(fenetre)

    #si l'utilisateur selectionne une lettre on la fait suivre la souris
    if not(lettre_select == None) :
        lettre_select.suivre_souris(fenetre)
    pygame.display.flip()
