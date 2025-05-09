def unite(p):
    """
    Entrée : une parcelle 
    Sortie : la parcelle après modification de ces paramètres après une unité de temps  
    """
    if p.vie:                         #On vérifie que la parcelle n'est pas calciné
        if not p.est_estompe:         #Si la parcelle n'est pas en train de s'estomper, on incrémente de 1 son intensité
            p.intensite=p.intensite+1     
            if p.intensite==p.intensite_max:        #Lorsque l'on attend l'intensité maximal de la parcelle, on passe la parcelle en phase d'estompement
                p.est_estompe=True
        else:
            p.intensite=p.intensite-1              #Si la parcelle est en phase d'estompement, on décrémente de 1 son intensité
            if p.intensite==0:                     #Si l'intensité arrive à 0, la parcelle devient calciné
                p.calcine()
    return p    

def est_identique(L,M):
    """
    Entrée : deux listes
    Sortie : Un booléen prenant la valeur True si tous les éléments en même position dans les deux listes ont la même intensité
    """
    if len(L)!=len(M):             #On vérifie que les deux listes on la même taille
        return False
    for i in range (len(L)):
        for j in range (len(L[i])):                    #On parcours les deux listes qui dans le contexte de leur utilisation ont la même taille.
            if L[i][j].intensite!=M[i][j].intensite:         #Si une intensité de deux éléments en même position sont différentes, on retourne False
                return False
    return True                             #Si après avoir parcouru tous les éléments, toutes les intensités des éléments en même position sont les mêmes, on retourne True



def proba_feu(distance,voisin):
    """
    Entrée : La Parcelle voisine et la distance se situant entre des deux parcelle (diagonale ou coté)
    Sortie : La probabilité que le feu se propage d'une parcelle à l'autre
    """
    M=0
    N=0
    if distance=="diagonale":               #On attribue des valeurs liés à la position des deux parcelles l'une par rapport à l'autre et à la nature de la parcelle voisine selon l'énoncé
        M=25                       
    elif distance=="cote":
        M=75
    if voisin.nature=="foret":
        N=1
    elif voisin.nature=="plaine" or voisin.nature=="maison":
        N=0.5
    return N*M*(0.75**(voisin.intensite_max-voisin.intensite))         #On retourne la formule de probabilité donné dans l'énoncé

                