###################################################
# Classe File (version professeur)

class File():
    """Création de la classe permettant de créer des objets de type file"""
    def __init__(self):
            self.liste =[]
            
    def EstVide (self):
         return len(self.liste) == 0
    def Enfiler (self,a): 
        self.liste.append(a) 
        return self.liste
    def Defiler (self):
        if self.EstVide():
            return 'impossible, la file est vide'
        else:
            self.liste.pop(0)
            return self.liste
    def Acceder (self):
         if self.EstVide():
            return 'impossible, la file est vide'
         else:
            return self.liste[len(self.liste)-1]
    def Comptage(self):
        return len(self.liste)

###################################################
# Classe File (version élève)

class File():
    def __init__(self, queue):
        self.queue = queue
        
    def ajouter(self, ticket):
        self.queue.insert(0, ticket)
        self.queue.pop(len(self.queue)-1)
    

            
            
file_1 = File([5,58,14,1,2,5,1,4,8,1,9,0,1,2,3,1])
print(file_1.queue)
print("+------------------------------+")
file_1.ajouter(4)

print(file_1.queue)    
