saisie_debut = input("le debut :")
debut = int(saisie_debut)
#si l'utilisateur saisit un chiffre impair
if debut % 2 != 0 :
    debut += 1
saisie_fin = input("la fin :")
fin = int(saisie_fin)
indice = 1
for elem in range(debut, fin, 2):
    print("element ", indice," = ", elem)
    indice += 1

