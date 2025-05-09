import time

class Parcelle:             #On définit un objet parcelle, que l'on mettra dans la grille final et qui représente un type d'environnement.

    def __init__(self,nature):
        self.nature=nature               #On définit la parcelle avec une nature (Plaine, foret, eau, maison)
        self.vie=True                    #Si la parcelle n'est pas encore calciné, on considère qu'elle est encore en vie
        self.est_estompe=False           #L'attribut prend la valeur False de base, et prend la valeur True lorsque l'intensité du feu diminue
        self.intensite=0                 #L'intensité du feu en question sur une parcelle est modélisé par un attribut intensité
        if self.nature=="plaine":
            self.intensite_max=2         #En fonction de la nature de la parcelle, on détermine une intensité maximal représentant la vitesse avec laquelle un environnement se calcine.
        elif self.nature=="foret":
            self.intensite_max=4
        elif self.nature=="maison":
            self.intensite_max=8
    
    def __str__(self):
        RED = '\033[91m'
        GREEN = '\033[32m'
        RESET = '\033[0m'
        if self.vie and not self.est_en_feu():
            s=str(self.nature)+str(self.intensite)
        elif self.vie and self.est_en_feu():
            s=GREEN+str(self.nature)+str(self.intensite)+RESET
        else:
            s=RED+str(self.nature)+RESET
        return s
    




    def calcine(self):                  #On crée une fonction calcine que l'on appliquera quand la parcelle se calcine.
        self.vie=False                  #On indique que la parcelle se calcine en changeant la valeur du booléen  
        self.intensite=0                #On passe l'intensité à 0
    


        


    def est_en_feu(self):             #On crée une fonction est_en_feu retournant un booléen prenant la valeur True si la parcelle est en feu et False sinon 
        return self.intensite!=0







    
if __name__=='__main__':
    parcelle=Parcelle("eau")
    print (parcelle)

        

    
    







    










    
    

