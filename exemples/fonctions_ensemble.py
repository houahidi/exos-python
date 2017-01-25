
def minimum(liste):
    min = liste[0]
    for elem in liste[1:]:
        if elem < min :
            min = elem
    return min

def moyenne(liste):
    return sum(liste)/len(liste)

if __name__ == "__main__":
    liste  = [3,6,7]
    m = moyenne(liste)
    print "moyenne de {0} est {1}".format(liste , m)
    m = minimum(liste)
    print "minimum de {0} est {1}".format(liste, m)