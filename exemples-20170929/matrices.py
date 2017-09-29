matrice = []
colonne1 = [2, 3]
colonne2 = [10, 12]
matrice.append(colonne1)
matrice.append(colonne2)
liste = [1, 4.8, "bonjour", True]
print(liste[3])
print(liste[0])
print(len(liste))
print(len(matrice))
print(matrice[1][0])
print(matrice)
print(matrice.index(colonne2))
print(colonne2.index(10))
matrice.extend(colonne1)
print(matrice)
print(matrice.count(2))
