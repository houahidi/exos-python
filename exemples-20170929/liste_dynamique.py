saisie_taille = input("Saisir la taille:")
taille = int(saisie_taille)
liste =[]

for indice in range(0, taille, 1):
    saisie_elem = input("saisir elem " + str(indice) +"=")
    liste.append(saisie_elem)
print("liste : ", liste)