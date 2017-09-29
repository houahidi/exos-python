saisie = input("Veuillez saisir un chiffre:")
print("Saisie :", saisie)
taille = len(saisie)
if taille > 0:
    print("l'unite :", saisie[-1])
if taille > 1 :
    print("l'dixieme :", saisie[-2])
if taille > 2 :
    print("l'centieme :", saisie[-3])