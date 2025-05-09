import random
from random import randint
from parametre import *


def generer_pluie(proba_pluie, tour_pluie_min, tour_pluie_max,pas_pluie_min,pas_pluie_max):
    prob=random.random()                  #On génère un réel entre 0 et 1
    if prob<proba_pluie:                 
        return True, randint(tour_pluie_min,tour_pluie_max)       #Si le réel est inferieur à la probabilité qu'il y est de la pluie, on retourne True et le nombre de tour généré aléatoirement, pendant lequel la pluie tombera.
    else:
        return False, randint(pas_pluie_min,pas_pluie_max)       #Dans le cas contraire, on retourne False et le nombre de tour généré aléatoirement durant lequel la pluie ne tombera pas.
    

def coefficient_pluie(pluie):
    """
    Entrée : Un booléen indiquant si la pluie tombe
    Sortie : Un coéfficient servant à réduire la propagation du feu si la pluie tombe
    """
    if pluie:
        return 0.25                  #Si il y a de la pluie, on diminue la probabilité que le feu se propage d'une parcelle à l'autre de 0.25 fois la proba initial.
    return 0

    

