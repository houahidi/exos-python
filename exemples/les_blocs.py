""" Demo bloc"""
i = raw_input("Veuillez saisir une valeur :")
print i , type(i)
try:
    i = int(i)
    if i > 0 :
        print "Valeur positive"
    else:
        print "Valeur negative"

    print "factoriel ", i," = "
    fact = 1
    for elem in range(2,i+1):
        fact *= elem  #fact = fact * elem
    print fact

    print "les {0} termes de suite fibonacci ".format(i)
    fib = [1, 1]
    for indice in range(2,i):
        fib.append(fib[indice - 1 ] + fib[indice - 2 ])
    print fib


except :
    print "Merci de saisir une valeur numerique"

