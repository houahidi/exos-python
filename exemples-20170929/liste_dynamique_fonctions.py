
from definition_min_max import minimum, maximum, moyenne

saisie_taille = input("Saisir la taille:")
taille = int(saisie_taille)
liste =[]

for indice in range(0, taille, 1):
    saisie_elem = input("saisir elem " + str(indice) +"=")
    entier = int(saisie_elem)
    liste.append(entier)
print("liste : ", liste)

# appel fonction minimum
resultat_min = minimum(liste)
print("le minimum est : ", resultat_min)
print("min : ", resultat_min)
# appel fonction maximum
resultat_max = maximum(liste)
print("le maximum : ", resultat_max)
print("moyenne : " , moyenne(liste))