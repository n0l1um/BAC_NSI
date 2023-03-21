from random import sample
from matplotlib.colors import same_color


class Arbre:
    def __init__(self, valeur, sag=None, sad=None):
        self.valeur = valeur
        self.sag = sag
        self.sad = sad
    
def hauteur(arbre):
    if arbre == None:
        return 0
    return max(1 + hauteur(arbre.sag), 1 + hauteur(arbre.sad))

def taille(arbre):
    if arbre == None:
        return 0
    return 1 + taille(arbre.sag) + taille(arbre.sad)

def parcours_prefixe(arbre):
    if arbre == None:
        return 0
    print(arbre.valeur)
    parcours_prefixe(arbre.sag)
    parcours_prefixe(arbre.sad)

def parcours_prefixe(arbre):
    if arbre != None:
        print(arbre.valeur)
        parcours_prefixe(arbre.sag)
        parcours_prefixe(arbre.sad)

def parcours_infixe(arbre):
    if arbre != None:
        parcours_infixe(arbre.sag)
        print(arbre.valeur)
        parcours_infixe(arbre.sad)

def parcours_postfixe(arbre):
    if arbre != None:
        parcours_postfixe(arbre.sag)
        parcours_postfixe(arbre.sad)
        print(arbre.valeur)

def parcours_largeur(arbre):
    return "non"

    
sample_tree = Arbre(28, Arbre(14, Arbre(7, Arbre(5, Arbre(3), Arbre(6))), Arbre(16)), Arbre(37, Arbre(34, Arbre(32), Arbre(36)), Arbre(49, Arbre(40), Arbre(74))))

"""
Parcours:
Largeur = 28, 14, 37, 7, 16, 34, 49, 5, 32, 36, 40, 74, 3, 6
Préfixe = 28, 14, 7, 5, 3, 6, 16, 37, 34, 32, 36, 49, 40, 74
Postfixe = 3, 6, 5, 7, 16, 14, 32, 36, 34, 40, 74, 49, 37, 28
Infixe = 3, 5, 6, 7, 14, 16, 28, 32, 34, 36, 37, 40, 49, 74
"""

print(hauteur(sample_tree))
print(taille(sample_tree))
print("--------------------")
print("Parcours largeur")
print(parcours_largeur(sample_tree))
print("--------------------")
print("Parcours prefixe")
print(parcours_prefixe(sample_tree))
print("--------------------")
print("Parcours infixe")
print(parcours_infixe(sample_tree))
print("--------------------")
print("Parcours postfixe")
print(parcours_postfixe(sample_tree))