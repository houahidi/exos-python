saisie = input(" veuillez saisir un chiffre =")
#print("saisie=",saisie )
#print("type=",type(saisie) )
#conversion en un entier de la saisie utilisateur
entier = int(saisie)
#print("type=",type(entier) )
#calcul du reste de la division entiere
reste = entier % 2
#print("reste=",reste)
if reste == 0:
    print("saisie :", saisie, " est pair")
else:
    print("saisie :", saisie, " est impair")