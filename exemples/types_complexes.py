""" Demo type complexes ou objets"""
# Liste : ensemble d'objets modifiable avec doublons
liste = [1,3,5,1,1,6,7]
print "liste: ", liste, type(liste)
print "1er element :", liste[0]
print "dernier element :", liste[-1]
print "taille :", len(liste), liste.__len__()
liste[0] = "1000"
print "liste : " , liste
# ajouter un nouveau element
liste.extend( [True,False])
print "taille :", len(liste)
print "liste : " , liste
print "indice de 1 : ", liste.index(3,1,7)
elem = liste.pop()
print "liste : " , liste
print "elem :", elem
liste.insert(2,elem)
print "liste : " , liste
liste.remove("1000")
print "liste : " , liste
liste.reverse()
print liste

print 1 in liste
print liste.__contains__(1)

liste.sort()
print liste

# ffectation par reference
listeBis = liste[:]
nouvelleListe = list(liste)
print "liste :", liste
print "listeBis :", listeBis
print "nouvelleListe :", nouvelleListe
liste.pop()
print "liste :", liste
print "listeBis :", listeBis
print "nouvelleListe :", nouvelleListe

# tuple : ensemble avec doublon non modifiable
liste.append([1,4])
tuple1 = tuple(liste)
print "tuple : ",tuple1
tuple1[-1].append(5)
print "tuple : ",tuple1
del tuple1[-1]






