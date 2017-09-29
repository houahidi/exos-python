saisie_taille = input("Saisir la taille:")
taille = int(saisie_taille)
liste =[]

for indice in range(0, taille, 1):
    saisie_elem = input("saisir elem " + str(indice) +"=")
    entier = int(saisie_elem)
    liste.append(entier)
print("liste : ", liste)

maximum = liste[0] #premier element
minimum = liste[0] #premier element
#sousliste = liste[1:] # sous liste contenant les elements
#                      # autre que le premier
somme = 0
for elem in liste:
    if elem > maximum:
        maximum = elem

    if elem < minimum:
        minimum = elem

    #ajouter a somme l'element de l'iteration
    #somme = somme + elem
    somme += elem
#sousliste = liste[1:] # sous liste contenant les elements
print("le maximum est : ", maximum)
print("le minimum est : ", minimum)
print("la somme   est : ", somme)
moyenne = somme / len(liste)
print("la moyenne est : ", moyenne)