###################################################
# Tri dichotomique (en itératif)
def dichotomie(tab, x):
    """
    tab : tableau trié dans l’ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if len(tab) == 0 :
        return False
    # cas où x n'est pas compris entre les valeurs extrêmes
    if (x < tab[0]) or x>tab[len(tab)-1]:
        return False
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut+fin)//2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m-1
    return False

liste_1 = [1,2,38,45,51,61,7484,487981,5151581]
print(dichotomie(liste_1, 38))

###################################################
# Recherche dichotomique (en récursif)
def dicho(tab,x):
    if len(tab) == 0:
        return False
    elif tab[0] > x or x > tab[len(tab)-1]:
        return False
    middle = len(tab)//2 - 1
    
    if x == tab[middle]:
        return True
    elif x > tab[middle]:
        return dicho(tab[middle+1:], x)
    else:
        return dicho(tab[:middle-1], x)
        tabend = middle-1
            
    return False

assert dicho([],4) == False
assert dicho([1,2,3,4,5,6],6) == True
assert dicho ( [1,2,3,4,5,6],1)== True
assert dicho ([1,2,3,4,5,6],5)==True
assert dicho([1,2,3],4) == False
assert dicho([1,2,3] , 2.5) == False

###################################################
# Tri par selection (en itératif)
def tri_selection(tab):
    for i in range(len(tab)):
      # Trouver le min
        min = i
        for j in range(i+1, len(tab)):
            if tab[min] > tab[j]:
                min = j
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
    return tab

tab = [98, 22, 15, 32, 2, 74, 63, 70]
 
tri_selection(tab)
 
print(tab)

###################################################
# Tri par insertion (en itératif)
def tri_insertion(tab): 
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k

tab = [98, 22, 15, 32, 2, 74, 63, 70]
tri_insertion(tab) 

print(tab)

###################################################
