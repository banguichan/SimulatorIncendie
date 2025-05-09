import random
proba_vent_gauche=0.1
vent_gauche_tour_min=3
vent_droite_tour_min=3
vent_haut_tour_min=3
vent_bas_tour_min=3
vent_gauche_tour_max=10
vent_droite_tour_max=10
vent_haut_tour_max=10
vent_bas_tour_max=10
pas_de_vent_tour_min=3
pas_de_vent_tour_max=10
proba_vent_droite=0.1
proba_vent_haut=0.1
proba_vent_bas=0.1
proba_pluie=0.25
tour_pluie_min=5
tour_pluie_max=20
pas_pluie_min=5
pas_pluie_max=20
proba_foudre=0.5
unite_temps=0.05
# Probabilités pour générer différents types de terrains.
probabilities = [0.35, 0.40, 0.25]
# Définition de la taille de la grille.
taille_grille = 100
# Nombre de chiffres à générer pour représenter le terrain.
nombre_de_chiffres = 10
# Nombre aléatoire de maisons entre 1 et 7.
nombre_de_maisons = random.randint(1, 7)