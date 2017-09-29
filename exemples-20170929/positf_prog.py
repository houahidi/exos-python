saisie = input("Veuillez saisir un chiffre:")
#print("Saisie :", saisie)
entier = int(saisie)
if entier > 0:
    print("le chiffre ", entier, "est positif")
elif entier < 0:
    print("le chiffre ", entier, "est négatif")
else:
    print("le chiffre == 0 ")