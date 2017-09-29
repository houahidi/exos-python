print("manipulation d'une liste")
liste = [1,4]
print("liste = ", liste, "type :", type(liste))
liste.append(100)
print("liste = ", liste)
liste.insert(1, -40)
print("liste = ", liste)
dernier = liste.pop()
print("dernier : ", dernier)
print("liste = ", liste)
taille = len(liste)
print("taille : ", taille)
liste.reverse()
print("liste = ", liste)
liste.sort()
liste.reverse()
print("liste = ", liste)
liste.append(-40)
print("liste = ", liste)
nombre = liste.count(1)
print("nombre d'occurrence de 1 = ", nombre)
indice = liste.index(-40, 0, len(liste))
print("Deuxieme indice de -40 = ", indice)

print("les tuples : listes non modifiables")
liste = [1,5]
print("liste=",liste)
a = 5
tuple = (a, 9, liste)
a += 100
print("tuple[0]=",tuple[0])
print("tuple = ",tuple)
tuple[2].append(6) # === liste.append(6)
print("liste=",liste)
print("tuple = ",tuple)


