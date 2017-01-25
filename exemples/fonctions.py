""" Demo fonctions"""

def factoriel(n):
    " Calcul du factoriel de n "
    fact = 1
    for elem in range(2, n + 1):
        fact *= elem  # fact = fact * elem
    return fact

def factRecursif(n):
    if n == 1:
        return 1
    else:
        return n * factRecursif(n-1)

if __name__ == "__main__":
    try:
        i = int(raw_input("Veuillez saisir une valeur :"))
        resultat = factoriel(i)
        print "factoriel({0}) = {1}".format(i, resultat)
        resultat = factRecursif(i)
        print "factoriel recursif({0}) = {1}".format(i, resultat)
    except :
        print "Merci de saisir une valeur numerique"
