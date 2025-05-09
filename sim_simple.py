from Parcelle_def import *
from parametre import *
from random import randint
from voisin import *
from operation_simulation import *
import time
import copy
import sys
import os

p1=Parcelle("plaine")
p2=Parcelle("plaine")
p3=Parcelle("plaine")
p4=Parcelle("plaine")
p5=Parcelle("plaine")
p6=Parcelle("plaine")
p7=Parcelle("plaine")
p8=Parcelle("plaine")
p9=Parcelle("plaine")
p10=Parcelle("plaine")
p11=Parcelle("plaine")
p12=Parcelle("plaine")
p13=Parcelle("plaine")
p14=Parcelle("plaine")
p15=Parcelle("plaine")
p16=Parcelle("plaine")
p17=Parcelle("plaine")
p18=Parcelle("plaine")
p19=Parcelle("plaine")
p20=Parcelle("plaine")
p21=Parcelle("plaine")
p22=Parcelle("plaine")
p23=Parcelle("plaine")
p24=Parcelle("plaine")
p25=Parcelle("plaine")
p26=Parcelle("plaine")
p27=Parcelle("plaine")
p28=Parcelle("plaine")
p29=Parcelle("plaine")
p30=Parcelle("plaine")
p31=Parcelle("plaine")
p32=Parcelle("plaine")
p33=Parcelle("plaine")
p34=Parcelle("plaine")
p35=Parcelle("plaine")
p36=Parcelle("plaine")
p37=Parcelle("plaine")
p38=Parcelle("plaine")
p39=Parcelle("plaine")
p40=Parcelle("plaine")
f1=Parcelle("foret")
f2=Parcelle("foret")
f3=Parcelle("foret")
f4=Parcelle("foret")
f5=Parcelle("foret")
f6=Parcelle("foret")
f7=Parcelle("foret")
f8=Parcelle("foret")
f9=Parcelle("foret")
f10=Parcelle("foret")
f11=Parcelle("foret")
f12=Parcelle("foret")
f13=Parcelle("foret")
f14=Parcelle("foret")
f15=Parcelle("foret")
f16=Parcelle("foret")
f17=Parcelle("foret")
f18=Parcelle("foret")
f19=Parcelle("foret")
f20=Parcelle("foret")
f21=Parcelle("foret")
f22=Parcelle("foret")
f23=Parcelle("foret")
f24=Parcelle("foret")
f25=Parcelle("foret")
f26=Parcelle("foret")
f27=Parcelle("foret")
f28=Parcelle("foret")
f29=Parcelle("foret")
f30=Parcelle("foret")
e1=Parcelle("eau")
e2=Parcelle("eau")
e3=Parcelle("eau")
e4=Parcelle("eau")
e5=Parcelle("eau")
e6=Parcelle("eau")
e7=Parcelle("eau")
e8=Parcelle("eau")
e9=Parcelle("eau")
e10=Parcelle("eau")
e11=Parcelle("eau")
e12=Parcelle("eau")
e13=Parcelle("eau")
e14=Parcelle("eau")
m1=Parcelle("maison")
m2=Parcelle("maison")
m3=Parcelle("maison")
m4=Parcelle("maison")
m5=Parcelle("maison")
m6=Parcelle("maison")


map=[[p1,p2,p3,p4,f1,f2,e7],
   [p5,p6,p7,f3,f4,f5,e9],
   [p8,p9,p10,p11,e1,e2,e10],
   [p12, p13, p14,e3,e4,e5,m2],
   [p15,p16,p17,f6,f7,e6,m3],
   [p18,p19,p20,f8,f9,f10,m1],
   [f11,f12,p21,p22,p23,f13,f14],
   [f15,f16,f17,f18,f19,f20,p24],
   [f21,f22,f23,f24,p25,p26,p27],
   [f25,f26,f27,p28,p29,p30,p31],
   [f28,f29,p32,p33,p34,e11],
   [f30,p35,p36,m4,e12,e13,e14],
   [m5,p37,p38,m6,p39,p40]]

def affichage(map):
    s=""
    for i in range(len(map)):
        s=s+"\n"
        for j in range(len(map[i])):
            s=s+" "+str(map[i][j])
    return s




def simulation(map):
    """
    Entrée : une map
    Sortie : Une simulation simple d'une propagation d'incendie sur cette map
    """
    feu=[]                      #On crée une liste feu comprenant tous les éléments ayant pris feu de la map
    pos_ant=[]                  #On crée une liste pos_ant comportant la map avant la dernière unité de temps
    while not est_identique(map,pos_ant):                  #Le programme s'arête si la map n'a pas changé entre deux unité de temps
        os.system('cls' if os.name == 'nt' else 'clear')  # Efface la sortie précédente
        sys.stdout.write(affichage(map))
        sys.stdout.flush()  # Assure l'affichage immédiat dans la console
        time.sleep(unite_temps)
        sys.stdout.write("\r")  # Retour au début de la ligne
        pos_ant=copy.deepcopy(map)            #On fait une copie non modifiable de la map dans la liste pos_ant
        if len(feu)==0:                      #Si aucun élément n'a pris feu, on choisit aléatoirement les coordonées d'une parcelle qui prendra feu
            lig=randint(0,len(map)-1)
            col=randint(0,len(map[lig])-1)
            while map[lig][col].nature=="eau":       #Si la parcelle tiré au sort est de l'eau, on tire au sort une nouvelle parcelle
                lig=randint(0,len(map)-1)               
                col=randint(0,len(map[lig])-1)
            map[lig][col].intensite=1             #On déclanche le feu à cette parcelle 
            feu.append([map[lig][col],lig,col])       #On ajoute à la liste feu une liste comprenent le nom de la parcelle et les coordonnées de celle ci
            voisin_pot=est_voisine(map,feu[0][1],feu[0][2])         #On ajoute les voisins potentielles de l'élément dans la liste. 
            for j in range(len(voisin_pot)):                        #On parcours les voisins potentiels
                if not voisin_pot[j] in feu:                        #Si le voisin n'a jamais pris feu, on l'ajoute dans la liste feu, pour qu'il prenne feu au prochain tour
                    feu.append(voisin_pot[j])
        else:
            for i in range(len(feu)):
                map[feu[i][1]][feu[i][2]]=unite(feu[i][0])            #Si au moins une des parcelles est en train de bruler, on parcours la liste de tous les éléments de la liste feu et on applique la fonction unite() qui applique à la parcelle les opérations correspondantes
                voisin_pot=est_voisine(map,feu[i][1],feu[i][2])       #On stocke dans une liste tous les voisins de la parcelle en cours de traitement
                for j in range(len(voisin_pot)):
                    if not voisin_pot[j] in feu:      
                        feu.append(voisin_pot[j])                    #On parcours cette liste de voisin. Si ce voisin n'est pas déja dans la liste feu, on l'ajoute afin qu'il prenne feu au prochain tour
    



            


        

        
    
    


    
    



if __name__=='__main__':
    simulation(map)
    













