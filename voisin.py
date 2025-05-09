def est_voisine(L, ligne, colonne):
    """
    Entrée : Une liste, des coordonnées d'un élément de la liste
    Sortie : Une liste comportant la liste des voisins qui n'ont pas pris feu  de l'élément correspondant aux coordonées placé en paramètre, ainsi que les coordonnées des voisins
    """
    voisine=[]
    for i in range(ligne-1, ligne+2):                     #On parcours la liste placé en paramètre entre les lignes l-1 et l+1 et les colonnes c-1 et c+1, l et c etant la ligne et la colonne de l'élément dont on cherche le voisin
        for j in range (colonne-1, colonne+2):
            if i>=0 and i<len(L) and j>=0 and j<len(L[i]):        #On vérifie que i est compris entre 0 et la taille de L et que j est compris est compris entre 0 et la taille de L[i]
                if (i!= ligne or j!=colonne) and not L[i][j].est_en_feu() and not L[i][j].vie==False and L[i][j].nature!="eau":               #On vérifie que l'élément que l'on parcours n'est pas l'élément dont on cherche le voisin, n'est pas de l'eau et n'est pas en feu
                    voisine.append([L[i][j],i,j])               #Si l'ensemble de ces conditions sont respectées, on ajoute à la liste des voisines une liste de 3 éléments comprenant la parcelle et les deux coordonnées de la parcelle
    return voisine

def est_voisine_cote(L, ligne, colonne):
    voisine=[]
    for i in range(ligne-1, ligne+2):                 #On parcours la liste placé en paramètre entre les lignes l-1 et l+1 et les colonnes c-1 et c+1, l et c etant la ligne et la colonne de l'élément dont on cherche le voisin
        for j in range (colonne-1, colonne+2):
            if i>=0 and i<len(L) and j>=0 and j<len(L[i]):            #On vérifie que i est compris entre 0 et la taille de L et que j est compris est compris entre 0 et la taille de L[i]
                if (i!= ligne or j!=colonne) and (i==ligne or j==colonne) and not L[i][j].est_en_feu() and not L[i][j].vie==False and L[i][j].nature!="eau":        #On vérifie que l'élément que l'on parcours n'est pas l'élément dont on cherche le voisin, n'est pas de l'eau et n'est pas en feu et est positionné sur le coté de l'élément dont on cheche les voisins. Il se situe sur le coté si il possède une ligne ou une colonne en commun avec l'élément
                    voisine.append([L[i][j],i,j])                  #Si l'ensemble de ces conditions sont respectées, on ajoute à la liste des voisines une liste de 3 éléments comprenant la parcelle et les deux coordonnées de la parcelle
    return voisine

def est_voisine_diag(L,ligne,colonne):
    voisine=[]
    for i in range(ligne-1, ligne+2):                       #On suit le même principe que pour la fonction précédente sauf que l'on ajoute à la liste tous les voisins n'ayant ni ligne si colonne en commun avec la parcelle placé en paramètre
        for j in range (colonne-1, colonne+2):
            if i>=0 and i<len(L) and j>=0 and j<len(L[i]):    
                if (i!=ligne and j!=colonne) and not L[i][j].est_en_feu() and not L[i][j].vie==False and L[i][j].nature!="eau":
                    voisine.append([L[i][j],i,j])
    return voisine