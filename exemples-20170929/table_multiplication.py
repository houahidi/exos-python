
table = input("table de  multiplication :")
chiffre = int(table)
saisie = input("Saisir un chiffre:")
entier = int(saisie)
liste = range(0, entier)
for elem in liste:
    resultat = elem * chiffre
    print(elem," * ", chiffre ,"= ", resultat )