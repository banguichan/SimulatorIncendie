import random
from random import randint
from parametre import *

def voisin_droite(p,voisin):
    """
    Entrée : une parcelle et un voisin de cette parcelle
    Sortie : un booléen prend la valeur True si le voisin se situe à droite de la parcelle
    """
    return p[2]==voisin[2]+1            #Si la coordonée de la colonne du voisin est superieur à celui de la parcelle de 1, alors le voisin se situe à droite de la parcelle  

def voisin_gauche(p,voisin):
    """
    Entrée : une parcelle et un voisin de cette parcelle
    Sortie : un booléen prend la valeur True si le voisin se situe à gauche de la parcelle
    """
    return p[2]==voisin[2]-1           #Si la coordonée de la colonne du voisin est inferieur à celui de la parcelle de 1, alors le voisin se situe à gauche de la parcelle  

def voisin_haut(p,voisin):
    """
    Entrée : une parcelle et un voisin de cette parcelle
    Sortie : un booléen prend la valeur True si le voisin se situe en haut de la parcelle
    """
    return p[1]==voisin[1]-1         #Si la coordonée de la ligne du voisin est inferieur à celui de la parcelle de 1, alors le voisin se situe en haut de la parcelle  

def voisin_bas(p,voisin):
    """
    Entrée : une parcelle et un voisin de cette parcelle
    Sortie : un booléen prend la valeur True si le voisin se situe en bas de la parcelle
    """
    return p[1]==voisin[1]+1        #Si la coordonée de la ligne du voisin est superieur à celui de la parcelle de 1, alors le voisin se situe en bas de la parcelle  


def generer_vent(proba_vent_haut,proba_vent_bas,proba_vent_gauche,proba_vent_droite,vent_gauche_tour_min,vent_droite_tour_min,vent_haut_tour_min,vent_bas_tour_min,vent_gauche_tour_max,vent_droite_tour_max,vent_haut_tour_max,vent_bas_tour_max,pas_de_vent_tour_min,pas_de_vent_tour_max):
    prob=random.random()                        #On génère un réel entre 0 et 1
    if prob<proba_vent_droite:                 
        return 'gd',randint(vent_droite_tour_min,vent_droite_tour_max)         #On regarde la probabilité d'avoir un vent à droite. Si le réel est inferieur à cette probabilité, alors on retourne le sens du vent (une chaine de deux caractère montrant la direction du vent comme 'gd' si le vent va de gauche à droite) et un nombre de tour défini aléatoirement entre un minimum et un maximum paramètrable.
    elif prob>proba_vent_droite and prob<=proba_vent_bas+proba_vent_droite:     #On suit le même procédé pour les autres directions du vent. Cette fois ci, on regarde si le réel généré est compris entre la probabilité du vent de droite et la probabilité du vent en haut. 
        return 'hb',randint(vent_bas_tour_min,vent_bas_tour_max)
    elif prob>proba_vent_bas+proba_vent_droite and prob<=proba_vent_bas+proba_vent_droite+proba_vent_gauche:    #Le procédé est exactement le même pour toutes les autres directions du vent y compris la probabilité qu'il n'y ai pas de vent.
        return 'dg',randint(vent_droite_tour_min,vent_gauche_tour_max)
    elif prob>proba_vent_bas+proba_vent_droite+proba_vent_gauche and prob<=proba_vent_bas+proba_vent_droite+proba_vent_gauche+proba_vent_haut:
        return 'bh',randint(vent_haut_tour_min,vent_haut_tour_max)
    else:
        return None,randint(pas_de_vent_tour_min,pas_de_vent_tour_max)             #Si il n'y a pas de de vent, on retourne None et le nombre de tour pendant lequel il n'y aura pas de vent.
 
def coefficient_vent(vent,p,voisin):
    """
    Entrée : la direction du vent, une parcelle et sa voisine
    Sortie : Un coéfficient par lequel on multiplie la probabilité qu'un voisin prenne feu en fonction de la position du voisin et du sens du vent
    """
    if (vent=='dg' and voisin_droite(p,voisin))or (vent=='gd' and voisin_gauche(p,voisin))or(vent=='hb' and voisin_haut(p,voisin))or(vent=='bh' and voisin_bas(p,voisin)):    # Si le voisin est dans la direction du vent, on multiplie par 1.25 sa probabilité de prendre feu
        return 1.25
    elif (vent=='dg' and voisin_gauche(p,voisin))or (vent=='gd' and voisin_droite(p,voisin))or(vent=='bh' and voisin_haut(p,voisin))or(vent=='hb' and voisin_bas(p,voisin)):   # Si le voisin est dans la direction opposé du vent, il n'a aucune chance de prendre feu. On multiplie donc le nombre par 0
        return 0
    return 1                  #Sinon, la probabilité ne change pas.