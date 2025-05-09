from Parcelle_def import *
from generer_vent import *
from generer_pluie import *
from generer_foudre import *
from parametre import *
from voisin import *
from operation_simulation import *
from generation_map import *
import random
import time
import copy
import sys
import os
import pygame
import random
import sys


pygame.init()  # Initialise Pygame.
screen = pygame.display.set_mode([500, 500])  # Crée une fenêtre d'affichage de 500x500 pixels.
running = True  # Variable pour contrôler la boucle principale du jeu.

# Remplit l'écran avec une couleur blanche.
screen.fill((255, 255, 255))

# Définition des couleurs utilisées dans le dessin des carrés.
orange_c = (255, 165, 0, 255)
orange_f = (255, 69, 0, 255)
rouge = (205, 0, 0, 255)
noir = (0, 0, 0, 255)
jaune = (238, 220, 130, 255)
vert = (84, 139, 84, 255)
bleu = (99, 184, 255, 255)
marron = (139, 90, 43, 255)


# Définition d'une fonction pour afficher la grille.
def affichage(grid):
    for i in range(taille_grille):  # Parcours les lignes de la grille.
        for j in range(taille_grille):  # Parcours les colonnes de la grille.
            square_x = i * 5  # Calcule la position x du carré.
            square_y = j * 5  # Calcule la position y du carré.
            square_size = 5  # Taille du carré.
            
            # Dessine un carré en fonction de la nature de la case dans la grille.
            if grid[i][j].nature == "maison" and grid[i][j].intensite == 0 and grid[i][j].vie: #En fionction de l'état de la case on peux assiger après des couleur
                pygame.draw.rect(screen, marron, (square_x, square_y, square_size, square_size))#Dessine un pixel dans la couleur demander
            elif grid[i][j].nature == "eau":
                pygame.draw.rect(screen, bleu, (square_x, square_y, square_size, square_size))
            elif grid[i][j].nature == "foret" and grid[i][j].intensite == 0 and grid[i][j].vie:
                pygame.draw.rect(screen, vert, (square_x, square_y, square_size, square_size))
            elif grid[i][j].nature == "plaine" and grid[i][j].intensite == 0 and grid[i][j].vie:
                pygame.draw.rect(screen, jaune, (square_x, square_y, square_size, square_size))
            elif grid[i][j].nature == "maison" and 1 <= grid[i][j].intensite <= 4 and not grid[i][j].est_estompe:
                pygame.draw.rect(screen, orange_c, (square_x, square_y, square_size, square_size))
            elif grid[i][j].nature == "maison" and 5 <= grid[i][j].intensite <= 8 and not grid[i][j].est_estompe:
                pygame.draw.rect(screen, orange_f, (square_x, square_y, square_size, square_size))
            elif grid[i][j].intensite > 0 and grid[i][j].est_estompe:
                pygame.draw.rect(screen, rouge, (square_x, square_y, square_size, square_size))
            elif not grid[i][j].vie:
                pygame.draw.rect(screen, noir, (square_x, square_y, square_size, square_size))
            elif grid[i][j].nature == "plaine" and grid[i][j].intensite == 1 and not grid[i][j].est_estompe:
                pygame.draw.rect(screen, orange_c, (square_x, square_y, square_size, square_size))
            elif grid[i][j].nature == "plaine" and grid[i][j].intensite == 2 and not grid[i][j].est_estompe:
                pygame.draw.rect(screen, orange_f, (square_x, square_y, square_size, square_size))
            elif grid[i][j].nature == "foret" and 1 <= grid[i][j].intensite <= 2 and not grid[i][j].est_estompe:
                pygame.draw.rect(screen, orange_c, (square_x, square_y, square_size, square_size))
            elif grid[i][j].nature == "foret" and 3 <= grid[i][j].intensite <= 4 and not grid[i][j].est_estompe:
                pygame.draw.rect(screen, orange_f, (square_x, square_y, square_size, square_size))

def simulation(map):
    

    feu=[]                                #Création d'une liste feu avec toutes les parcelles ayant pris feu
    pos_ant=[]                            #Cette prendra la forme de la map anterieur pour que la simulation s'arête quand aucune parcelle n'a été affecté en une unité de temps
    tour_vent=0                           #Prend la valeur du nombre de tour ou le vent va rester dans tel direction
    tour_pluie=0                          #Prend la valeur du nombre de tour ou restera ou non la pluie
    tour_foudre=0                         #Compte le nombre de tour pour faire évantuellement frapper la foudre tous les 10 tours
    while not est_identique(map,pos_ant):     #On execute la boucle jusqu'à qu'aucune parcelle ne soit modifié en une unité de temps
        
        # Vérifie les événements Pygame.
        for event in pygame.event.get():
            # Si l'utilisateur a cliqué sur le bouton de fermeture de la fenêtre, 'running' est définie sur 'False'.
            if event.type == pygame.QUIT:
                running = False
        
        if tour_vent==0:                      #Lorsque l'on commence la simulation ou que l'on a fini un nombre de tour avec un même sens de vent, on génère un nouveau vent avec des probabilités paramètrable
            vent,tour_vent=generer_vent(proba_vent_haut,proba_vent_bas,proba_vent_gauche,proba_vent_droite,vent_gauche_tour_min,vent_droite_tour_min,vent_haut_tour_min,vent_bas_tour_min,vent_gauche_tour_max,vent_droite_tour_max,vent_haut_tour_max,vent_bas_tour_max,pas_de_vent_tour_min,pas_de_vent_tour_max)
        if tour_pluie==0:                     #On effectue le même principe qu'avec le vent
            pluie,tour_pluie=generer_pluie(proba_pluie, tour_pluie_min, tour_pluie_max,pas_pluie_min,pas_pluie_max)
        if tour_foudre==10:                  #Tous les 10 tours, on génère potentiellement de la foudre
            foudre=generer_foudre(proba_foudre)
            tour_foudre=0                   #Lorsque l'on a atteint les 10 tours, on remet le compteur à 0
            if foudre:                     #Si foudre prend la valeur True, on tire au sort une parcelle de la map 
                lig=randint(0,len(map)-1)            
                col=randint(0,len(map[lig])-1)
                if map[lig][col].nature!="eau" and map[lig][col].vie and map[lig][col].intensite==0:      #elle prend feu si elle n'a jamais été e feu et qu'elle n'est pas de l'eau
                    map[lig][col].intensite=1
                    feu.append([map[lig][col],lig,col])                #On ajoute l'élémet à la liste feu ainsi que ces coordonnées 
        affichage(map)
        pygame.display.flip()
#        time.sleep(unite_temps)             #On définit à une seconde une unité de temps
        
        pos_ant=copy.deepcopy(map) 
        
                #On copie la map dans pos_ant
        if len(feu)==0:                   #Si aucune parcelle n'a pris feu, on met le feu à une parcelle aléatoire
            lig=randint(0,len(map)-1)
            col=randint(0,len(map[lig])-1)
            while map[lig][col].nature=="eau":      #Si la parcelle tiré au sort est de l'eau, on retire au sort une parcelle.
                lig=randint(0,len(map)-1)
                col=randint(0,len(map[lig])-1)
            map[lig][col].intensite=1              #On met le feu à la parcelle en question
            feu.append([map[lig][col],lig,col])        #On ajoute a la liste feu, une liste avec la parcelle et les coordonnés de celle ci
        else:
            for i in range(len(feu)):                #On suit un principe similaire ensuite pour chaque parcelle en feu et pour chaque tour de boucle.
                if feu[i][0].vie:                                 #Si la parcelle prend toujours feu, on effectue l'opération correspondante
                    
                    voisin_pot_cote=est_voisine_cote(map,feu[i][1],feu[i][2])              #On stocke dans une variable les voisins de la parcelle en cours de traitement se situant sur le coté    
                    voisin_pot_diag=est_voisine_diag(map,feu[i][1],feu[i][2])              #On stocke dans une autre variable les voisins de la parcelle en cours de traitement se situant en diagonal   
                    for j in range(len(voisin_pot_cote)):                          #On parcours les voisins de côté. 
                        if not voisin_pot_cote[j] in feu:                  #Si le voisin n'a pas pris feu, on génère un réel aléatoirement entre 0 et 1
                            prob=random.random()
                            if prob<(proba_feu("cote",voisin_pot_cote[j][0])*coefficient_vent(vent,feu[i],voisin_pot_cote[j])-(proba_feu("cote",voisin_pot_cote[j][0])*coefficient_pluie(pluie)))/100:          #On calcule la probabilité que la parcelle voisine prenne feu grâce à la formule de l'énoncé.
                                feu.append(voisin_pot_cote[j])                     #Si le réel est infieur à la probabilité calculé, on ajoute cet élément à la liste feu
                                voisin_pot_cote[j][0].intensite=1                  #On met un feu d'intensité 1 à cette parcelle
                    
                    for k in range(len(voisin_pot_diag)):                       #On suit le même principe pour les voisins potentiels en diagonal.
                        if not voisin_pot_diag[k] in feu:
                            prob=random.random()
                            if prob<(proba_feu("diagonale",voisin_pot_diag[k][0])*coefficient_vent(vent,feu[i],voisin_pot_diag[k])-(proba_feu("cote",voisin_pot_diag[k][0])*coefficient_pluie(pluie)))/100:
                                feu.append(voisin_pot_diag[k])
                                voisin_pot_diag[k][0].intensite=1
                    map[feu[i][1]][feu[i][2]]=unite(feu[i][0])                   #On applique à la parcelle en cours de traitement les opérations nécessaire défini par la fonction unite().
        
        tour_vent=tour_vent-1                                  #On décrémente 1 à tour_vent pour compter le nombre de tour durant lequel le vent est dans le même sens
        tour_pluie=tour_pluie-1                                #On décrémente 1 à tour_pluie pour compter le nombre de tour durant lequel la pluie tombe ou non.
        tour_foudre=tour_foudre+1                              #On compte incrémente 1 à tour_foudre à chaque tour de boucle pour que la foudre tombe évantuellement tous les 10 unités de temps  







# Boucle principale qui s'exécute tant que la variable 'running' est vraie.
while running:
    # Affiche la grille en appelant la fonction 'affichage(grid)'.
    #affichage(grid)
    
    # Met à jour l'affichage.
    pygame.display.flip()
    
    # Effectue une simulation en appelant la fonction 'simulation(grid)'.
    simulation(grid)
    
    # Vérifie les événements Pygame.
    for event in pygame.event.get():
        # Si l'utilisateur a cliqué sur le bouton de fermeture de la fenêtre, 'running' est définie sur 'False'.
        if event.type == pygame.QUIT:
            running = False




