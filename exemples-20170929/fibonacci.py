fibo = [1, 1]
indices = range(2,10,1)
print("indices elements manquants", list(indices))
for indice in indices:
    element = fibo[indice - 1] + fibo[indice - 2]
    fibo.append(element)
print("suite fibonacci : " , fibo)
#affichage
indice = 0
for elem in fibo:
    print("U" + str(indice), "=", elem)
    indice += 1