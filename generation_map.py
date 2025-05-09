from Parcelle_def import * 
import random 
from parametre import *

# Initialisation d'une grille remplie de points.
grid = [['.' for _ in range(taille_grille)] for _ in range(taille_grille)]

# Liste pour stocker les coordonnées des cases remplacées.
coordonnees_remplacees = []

# Fonction pour générer le terrain initial.
def generer_terrain(grid):
    for _ in range(nombre_de_chiffres):
        # Génère des coordonnées aléatoires.
        x = random.randint(0, taille_grille - 1)
        y = random.randint(0, taille_grille - 1)
        
        # Choix aléatoire d'un chiffre en fonction des probabilités.
        chiffre = str(random.choices([1, 2, 3], weights=probabilities)[0])
        
        # Place le chiffre dans la grille et met à jour les cases voisines.
        grid[x][y] = chiffre
        for i in range(max(0, x - 1), min(taille_grille, x + 2)):
            for j in range(max(0, y - 1), min(taille_grille, y + 2)):
                grid[i][j] = chiffre
                coordonnees_remplacees.append((i, j))

# Fonction pour générer des maisons.
def generer_maison(grid):
    # Nombre aléatoire de maisons entre 1 et 7.
        
    for _ in range(nombre_de_maisons):
        # Génère des coordonnées aléatoires pour la maison.
        x = random.randint(0, taille_grille - 10)  # Assure qu'il y a de la place pour une maison de 10x10.
        y = random.randint(0, taille_grille - 10)
        
        # Place la maison dans la grille.
        for i in range(x, x + 10):
            for j in range(y, y + 10):
                grid[i][j] = '4'  # '4' représente la maison dans la grille.

# Fonction pour générer les voisins des cellules.
def generer_voisin(grid):
    global coordonnees_remplacees  # Déclaration pour accéder à la variable globale coordonnees_remplacees.
    
    # Boucle tant que la liste des coordonnées à remplacer n'est pas vide.
    while coordonnees_remplacees:
        nouvelle_liste = []  # Initialise une nouvelle liste pour stocker les nouvelles coordonnées à remplacer.
        
        # Parcours de toutes les coordonnées dans la liste des coordonnées à remplacer.
        for coord in coordonnees_remplacees:
            x, y = coord  # Récupère les coordonnées x et y.
            chiffre = grid[x][y]  # Récupère le chiffre à la position (x, y).
            
            # Parcours des cellules voisines de la cellule à la position (x, y).
            for i in range(max(0, x - 1), min(taille_grille, x + 2)):
                for j in range(max(0, y - 1), min(taille_grille, y + 2)):
                    if grid[i][j] == '.':  # Vérifie si la cellule est vide.
                        grid[i][j] = chiffre  # Remplace la cellule vide par le même chiffre que la cellule d'origine.
                        nouvelle_liste.append((i, j))  # Ajoute les nouvelles coordonnées à la liste.
        
        coordonnees_remplacees = nouvelle_liste  # Met à jour la liste des coordonnées à remplacer avec la nouvelle liste.


# Fonction pour créer la grille de parcelles à partir de la grille de chiffres.
def creation_terrain(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                grid[i][j] = Parcelle("plaine")
            elif grid[i][j] == '2':
                grid[i][j] = Parcelle("foret")
            elif grid[i][j] == '3':
                grid[i][j] = Parcelle("eau")
            elif grid[i][j] == '4':
                grid[i][j] = Parcelle("maison")

# Fonction principale pour générer la carte.
def generer_map(grid):
    generer_terrain(grid)  # Génère le terrain initial.
    generer_maison(grid)   # Génère des maisons.
    generer_voisin(grid)   # Génère les voisins des cellules.
    creation_terrain(grid)  # Crée la grille de parcelles à partir de la grille de chiffres.
    return grid

# Appel de la fonction principale pour générer la carte.
generer_map(grid)
