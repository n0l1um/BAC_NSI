###################################################
# Les fonctions de random

# Randint

from random import *

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    def attributes(self):
        return (self.valeur, self.couleur)

couleurs = ["pique", "carreau", "coeur", "trèfle"]

carte_1 = Carte(15, "coeur")
random_carte = Carte(randint(1, 52), couleurs[randint(0, 3)])
print(random_carte.attributes())

# Randrange

print("Random number between 0 and 100: ", randrange(100))
print("Random number between 50 and 100: ", randrange(50, 100))
print("Random number between 0 and 100, with a step of 2: ", randrange(0, 100, 2))

###################################################
# Les fonctions de math

# Racine

from math import *

trois = sqrt(9)

# Pi
pi_stored = pi

print(pi_stored)

###################################################
# L'assert
def addition(n1, n2):
    return n1 + n2

assert addition(4, 6) == 10
