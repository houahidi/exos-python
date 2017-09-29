
def minimum(uneliste):
    minimum = uneliste[0]
    for elem in uneliste:
        if elem < minimum:
            minimum = elem
    #print("le minimum est : ", minimum)
    return minimum

def maximum(uneliste):
    lemax = uneliste[0] #premier element
    for elem in uneliste:
        if elem > lemax:
            lemax = elem
    #print("le maximum est : ", maximum)
    return lemax

def sommme(uneliste):
    resultat = 0
    for elem in uneliste:
        resultat += elem
    return resultat

def moyenne(uneliste):
    return sommme(uneliste) / len(uneliste)


