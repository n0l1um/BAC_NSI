###################################################
# Classe Pile (version professeur)

class Pile():
    """ Création de la classe permettant de créer des objets de type pile"""
    
    def __init__(self,liste =[]):
            self.liste =liste
            
    def EstVide (self):
         return len(self.liste) == 0
    def Empiler (self,a): 
        self.liste.append(a)    #~Remarque , dans une liste  du type [2,3,1], le sommet de la pile est 1
        return self.liste
    def Depiler (self):
        if self.EstVide():
            return 'impossible, la pile est vide'
        else:
            return self.liste.pop()
    def Acceder (self,rang):
         if self.EstVide():
            return 'impossible, la pile est vide'
         elif rang>len(self.liste)-1:
                return "Vous cherchez un rang à l'extérieur de la liste"
         else:
                return self.liste[rang]
    def Comptage(self):
        return len(self.liste)
    def Affichage(self):
        return f"Voici l'état de la pile {self.liste}"
P= Pile([82,4,51,8,1])
P.Acceder(3)

###################################################
# Classe Pile (version élève)
class Pile():
    def __init__(self, disks):
        self.disks = disks
        
    def empiler(self, disk):
        self.disks.append(disk)
    
    def depiller(self):
        self.disks.pop(len(self.disks)-1)
    
    def compter(self):
        return len(self.disks)
    
    def acceder(self, idx):
        for i in range(idx, len(self.disks)-1):
            self.disks[i], self.disks[i+1] = self.disks[i+1], self.disks[i]
            
            
pile_1 = Pile([5,58,14,1,2,5,1,4,8,1,9,0,1,2,3,1])
print(pile_1.disks)
print("+------------------------------+")
pile_1.empiler(4)
print(pile_1.disks)
print("+------------------------------+")
pile_1.depiller()
print(pile_1.disks)
print("+------------------------------+")
count = pile_1.compter()
print(count)
print("+------------------------------+")
pile_1.acceder(1)
print(pile_1.disks)

###################################################
# Classe Pile avec liste chaînée

class Cellule:
    def __init__(self,valeur, adresse):
        self.valeur = valeur
        self.adresse = adresse
        
class Pile:
    def __init__(self):
        self.contenu = None
    def EstVide(self):
        return self.contenu is None
    def Empiler(self,valeur):
        self.contenu = Cellule(valeur,self.contenu)
    def Depiler(self):
        if self.EstVide():
            raise IndexError('pile vide')
        else:
            valeur = self.contenu.valeur
            self.contenu = self.contenu.adresse
            return valeur
    
        
    def Comptage(self):
        stock = Pile()
        compteur = 0
        while not self.EstVide():
            stock.Empiler(self.Depiler())
            compteur = compteur+1
        while not stock.EstVide():
            self.Empiler(stock.Depiler())
        return compteur