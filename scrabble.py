import random
import csv
import pygame

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
Joueur1 = Joueur()
Joueur1.add_letters()

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

pygame.init()
taille_fenetere = (800, 600)
fenetre = pygame.display.set_mode(taille_fenetere)
lettres = []
for i in Joueur1.letters:
    lettres.append(i.nom)

u = 50
position_lettres = []
for i in range(len(lettres)):
    x = (i * u) + 50
    y = 50
    position_lettres.append((x, y))
font = pygame.font.SysFont('Comic Sans MS', 30)
for i in range(len(lettres)):
    letter = lettres[i]
    position = position_lettres[i]
    text = font.render(letter, True,(255,255,255))
    fenetre.blit(text, position)
pygame.display.flip()
continuer = True
lettre_select,old_position = None, None
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#Pour quitter le jeu
            continuer = False

        elif event.type == pygame.MOUSEBUTTONDOWN:#quand l'utilisateur clique sur son clique gauche on récupere la mosition de la souris
            mouse_x, mouse_y = pygame.mouse.get_pos()

            for i in range(len(lettres)):#on verifie si ca correspond a la position d'une lettre
                x, y = position_lettres[i]
                if (x <= mouse_x <= x + u) and (y <= mouse_y <= y + u):
                    lettre_select = lettres[i]
                    selected_letter_index = i

        elif event.type == pygame.MOUSEBUTTONUP:#si l(utilisateur relache son clique gauche on recupere la position de la souris
            mouse_x, mouse_y = pygame.mouse.get_pos()

            for i in range(len(lettres)):#on vérifie que cette position correspond a la position d'une lettre et on les échanges
                x, y = position_lettres[i]
                if (x <= mouse_x <= x + u) and (y <= mouse_y <= y + u):
                    lettres[selected_letter_index], lettres[i] = lettres[i], lettre_select
                    lettre_select,old_x,old_y = None, None, None

    if not(old_position == None):#efface la lettre qui se déplace pour éviter les traces(les fonctions sont dans cette ordres pour éviter que tous se superpose mal)
        fenetre.fill((0, 0, 0), (old_position[0], old_position[1], 50, 50))

    for i in range(len(lettres)):#on redessine le nouvel ordres des lettres
        x, y = position_lettres[i]
        pygame.draw.rect(fenetre, (0, 0, 0), (x, y, u, u))
        text = font.render(lettres[i], True, (255, 255, 255))
        fenetre.blit(text,(x + (u // 2 - text.get_width() // 2), y + (u // 2 - text.get_height() // 2)))

    if not(lettre_select == None) :#La lettre suit la souris lors du déplacement de la lettre
        mouse_x, mouse_y = pygame.mouse.get_pos()
        text = font.render(lettre_select, True,(255,255,255))
        position = (mouse_x,mouse_y)
        old_position = (mouse_x, mouse_y)
        fenetre.blit(text, position)

    pygame.display.flip()

