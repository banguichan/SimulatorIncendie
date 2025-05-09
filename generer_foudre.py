import random
from parametre import *



def generer_foudre(proba_foudre):
    prob=random.random()                #On génère un réel entre 0 et 1
    if prob<proba_foudre:              #On retourne True si le réel est inferieur à la probabilité que la foudre tombe
        return True
    return False                      #On retourne False sinon


