saisie_chiffre = input("Saisir le chiffre1:")
chiffre1 = int(saisie_chiffre)
saisie_chiffre = input("Saisir le chiffre2:")
chiffre2 = int(saisie_chiffre)

def factoriel(chiffre):
    resultat = 1
    liste = range(chiffre,0,-1)
    liste = list(liste)
    #print(liste)
    for elem in liste:
        resultat = resultat * elem
    print("factoriel de ",chiffre, "=", resultat)

factoriel(chiffre1)
factoriel(chiffre2)
factoriel(20)
factoriel(58)
