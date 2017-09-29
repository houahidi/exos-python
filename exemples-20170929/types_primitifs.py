print("manipulation des entiers")
# initialisation de la variable i de type int avec la valeur 2
i = 2
print("i =", i)
i = i * 12
print("i * 12 =", i)
print("manipulation des reels")
# initialisation de la variable j de type float avec la valeur 3.0
j = 3.0
print("j =", j)
j = j * 12
print("j * 12 =", j)
print("manipulation des booleans")
# initialisation de la variable b de type bool avec la valeur True
b = True
print("b =", b)
b = not b
print("inverse de b == not b =", b)
print("manipulation des chaine de caractères")
# initialisation de la variable chaine de type str avec la valeur "bonjour"
chaine = "bonjour"
print("chaine =",chaine)
# concatenation
public = "tout le monde"
chaine = chaine + " " + public
print("chaine  + ' ' + public=",chaine)

print("affectation par copie des types primitifs = simples")
new_chaine = chaine
chaine = "autre chaine"
print("chaine =", chaine, "et new_chaine=",new_chaine)
